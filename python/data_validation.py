import sqlite3
from pathlib import Path

import pandas as pd


# Project paths
BASE = Path(__file__).resolve().parents[1]
RAW = BASE / "data" / "raw"
PROCESSED = BASE / "data" / "processed"
DB = BASE / "database" / "mis.db"

orders_file = PROCESSED / "orders_mis.csv"
payments_file = RAW / "olist_order_payments_dataset.csv"

if not orders_file.exists():
    raise FileNotFoundError(
        f"{orders_file} not found. Run data_cleaning.py first."
    )
if not payments_file.exists():
    raise FileNotFoundError(
        f"{payments_file} not found. Check your data/raw folder."
    )


# Load cleaned order-level data and raw payments
orders = pd.read_csv(orders_file)
payments = pd.read_csv(payments_file)

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"], errors="coerce"
)
orders["order_delivered_customer_date"] = pd.to_datetime(
    orders["order_delivered_customer_date"], errors="coerce"
)
payments["payment_value"] = pd.to_numeric(
    payments["payment_value"], errors="coerce"
)


# Validation rule 1: order IDs must be unique in orders_mis
duplicate_order_ids = int(orders["order_id"].duplicated().sum())

# Validation rule 2: purchase date must not be missing
missing_purchase_dates = int(
    orders["order_purchase_timestamp"].isna().sum()
)

# Validation rule 3: delivery date must not be before purchase date
delivery_before_purchase = (
    orders["order_delivered_customer_date"].notna()
    & orders["order_purchase_timestamp"].notna()
    & (
        orders["order_delivered_customer_date"]
        < orders["order_purchase_timestamp"]
    )
)
invalid_delivery_dates = int(delivery_before_purchase.sum())

# Validation rule 4: payment values must not be negative
negative_payment_values = int((payments["payment_value"] < 0).sum())


validation = pd.DataFrame(
    [
        ("Order IDs must be unique", duplicate_order_ids),
        ("Purchase date must not be missing", missing_purchase_dates),
        (
            "Delivery date must not be before purchase date",
            invalid_delivery_dates,
        ),
        ("Payment value must not be negative", negative_payment_values),
    ],
    columns=["Validation Rule", "Issue Count"],
)
validation["Status"] = validation["Issue Count"].apply(
    lambda count: "PASS" if count == 0 else "CHECK"
)


# Save validation report as CSV and as a SQLite table
PROCESSED.mkdir(parents=True, exist_ok=True)
validation.to_csv(PROCESSED / "data_validation.csv", index=False)

if DB.exists():
    with sqlite3.connect(DB) as conn:
        validation.to_sql(
            "data_validation",
            conn,
            if_exists="replace",
            index=False,
        )
else:
    print("Warning: Database not found. CSV validation report was saved.")

print("\nData validation completed.")
print(validation.to_string(index=False))
print("\nValidation report:", PROCESSED / "data_validation.csv")
