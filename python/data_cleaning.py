import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd


# Project paths
BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "data" / "raw"
PROCESSED = BASE / "data" / "processed"
REPORTS = BASE / "reports"
DB = BASE / "database" / "mis.db"

PROCESSED.mkdir(parents=True, exist_ok=True)
REPORTS.mkdir(parents=True, exist_ok=True)
DB.parent.mkdir(parents=True, exist_ok=True)


# 1. Load raw datasets
orders_raw = pd.read_csv(RAW / "olist_orders_dataset.csv")
items_raw = pd.read_csv(RAW / "olist_order_items_dataset.csv")
customers_raw = pd.read_csv(RAW / "olist_customers_dataset.csv")
payments_raw = pd.read_csv(RAW / "olist_order_payments_dataset.csv")
reviews_raw = pd.read_csv(RAW / "olist_order_reviews_dataset.csv")
products_raw = pd.read_csv(RAW / "olist_products_dataset.csv")
sellers_raw = pd.read_csv(RAW / "olist_sellers_dataset.csv")
translation = pd.read_csv(RAW / "product_category_name_translation.csv")


# 2. AUDIT BEFORE CLEANING
# Capture issues before removing duplicates or filling missing values.
raw_payment_values = pd.to_numeric(
    payments_raw["payment_value"], errors="coerce"
)
raw_payment_summary = (
    payments_raw.assign(_payment_value=raw_payment_values)
    .groupby("order_id")["_payment_value"]
    .sum(min_count=1)
)

raw_audit_checks = [
    ("Duplicate Order IDs", int(orders_raw["order_id"].duplicated().sum())),
    ("Missing Purchase Dates", int(orders_raw["order_purchase_timestamp"].isna().sum())),
    (
        "Orders Without Payment Records",
        int((~orders_raw["order_id"].isin(payments_raw["order_id"])).sum()),
    ),
    ("Orders With Missing Payment Totals", int(raw_payment_summary.isna().sum())),
    ("Missing Customer IDs", int(orders_raw["customer_id"].isna().sum())),
    (
        "Delivered Orders Without Delivery Date",
        int(
            (
                orders_raw["order_status"].eq("delivered")
                & orders_raw["order_delivered_customer_date"].isna()
            ).sum()
        ),
    ),
    ("Negative Payment Values", int((raw_payment_values < 0).sum())),
    (
        "Duplicate Order Item Keys",
        int(items_raw.duplicated(["order_id", "order_item_id"]).sum()),
    ),
]
audit = pd.DataFrame(raw_audit_checks, columns=["Check", "Count"])
audit.to_csv(PROCESSED / "data_audit.csv", index=False)


# 3. Remove duplicate records using appropriate keys
orders = orders_raw.drop_duplicates("order_id").copy()
items = items_raw.drop_duplicates(["order_id", "order_item_id"]).copy()
customers = customers_raw.drop_duplicates("customer_id").copy()
payments = payments_raw.drop_duplicates(
    ["order_id", "payment_sequential"]
).copy()
products = products_raw.drop_duplicates("product_id").copy()
sellers = sellers_raw.drop_duplicates("seller_id").copy()
reviews = reviews_raw.drop_duplicates("review_id").copy()


# 4. Convert dates
date_cols = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]
for col in date_cols:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")


# 5. Clean numerical columns (after the audit)
items["price"] = pd.to_numeric(items["price"], errors="coerce").fillna(0)
items["freight_value"] = pd.to_numeric(
    items["freight_value"], errors="coerce"
).fillna(0)
payments["payment_value"] = pd.to_numeric(
    payments["payment_value"], errors="coerce"
).fillna(0)
reviews["review_score"] = pd.to_numeric(
    reviews["review_score"], errors="coerce"
)


# 6. Aggregate order items
item_summary = items.groupby("order_id").agg(
    total_items=("order_item_id", "count"),
    item_revenue=("price", "sum"),
    freight_total=("freight_value", "sum"),
    seller_count=("seller_id", "nunique"),
).reset_index()


# 7. Aggregate payments
payment_summary = payments.groupby("order_id").agg(
    payment_total=("payment_value", "sum")
).reset_index()


# 8. Aggregate reviews
review_summary = reviews.groupby("order_id").agg(
    review_score=("review_score", "mean")
).reset_index()


# 9. Combine order-level information
df = orders.merge(
    customers[["customer_id", "customer_city", "customer_state"]],
    on="customer_id",
    how="left",
)
df = df.merge(item_summary, on="order_id", how="left")
df = df.merge(payment_summary, on="order_id", how="left")
df = df.merge(review_summary, on="order_id", how="left")


# 10. Fill appropriate missing numerical values
for col in ["total_items", "item_revenue", "freight_total", "seller_count"]:
    df[col] = df[col].fillna(0)
df["payment_total"] = df["payment_total"].fillna(0)


# 11. Delivery calculations
df["delivery_days"] = (
    df["order_delivered_customer_date"] - df["order_purchase_timestamp"]
).dt.total_seconds() / 86400
df["delay_days"] = (
    df["order_delivered_customer_date"] - df["order_estimated_delivery_date"]
).dt.total_seconds() / 86400
df["on_time"] = np.where(
    df["order_status"].eq("delivered") & df["delay_days"].notna(),
    df["delay_days"] <= 0,
    np.nan,
)


# 12. Date dimensions
df["purchase_date"] = df["order_purchase_timestamp"].dt.strftime("%Y-%m-%d")
df["year_month"] = df["order_purchase_timestamp"].dt.strftime("%Y-%m")
df["week_start"] = (
    df["order_purchase_timestamp"]
    .dt.to_period("W-SUN")
    .dt.start_time.dt.strftime("%Y-%m-%d")
)


# 13. Save order-level MIS data
df.to_csv(PROCESSED / "orders_mis.csv", index=False)


# 14. Category-level report
category_items = items.merge(
    products[["product_id", "product_category_name"]],
    on="product_id",
    how="left",
)
category_items = category_items.merge(
    translation,
    on="product_category_name",
    how="left",
)
category_items["category"] = (
    category_items["product_category_name_english"].fillna("Unknown")
)
category_mis = category_items.groupby("category").agg(
    total_items=("order_id", "count"),
    unique_orders=("order_id", "nunique"),
    revenue=("price", "sum"),
    freight=("freight_value", "sum"),
).reset_index()
category_mis.to_csv(PROCESSED / "category_mis.csv", index=False)


# 15. Seller-level report
seller_items = items.merge(
    orders[
        [
            "order_id",
            "order_purchase_timestamp",
            "order_status",
            "order_delivered_customer_date",
            "order_estimated_delivery_date",
        ]
    ],
    on="order_id",
    how="left",
)
seller_mis = seller_items.groupby("seller_id").agg(
    total_items=("order_id", "count"),
    unique_orders=("order_id", "nunique"),
    revenue=("price", "sum"),
    freight=("freight_value", "sum"),
).reset_index()
seller_mis = seller_mis.merge(
    sellers[["seller_id", "seller_city", "seller_state"]],
    on="seller_id",
    how="left",
)
seller_mis.to_csv(PROCESSED / "seller_mis.csv", index=False)


# 16. Save cleaned tables and pre-cleaning audit to SQLite
with sqlite3.connect(DB) as conn:
    df.to_sql("orders_mis", conn, if_exists="replace", index=False)
    category_mis.to_sql("category_mis", conn, if_exists="replace", index=False)
    seller_mis.to_sql("seller_mis", conn, if_exists="replace", index=False)
    audit.to_sql("data_audit", conn, if_exists="replace", index=False)

print("Data cleaning completed successfully!")
print("Order records:", len(df))
print("Pre-cleaning audit:", PROCESSED / "data_audit.csv")
print("Database:", DB)
print("Next, run: python python/data_validation.py")
