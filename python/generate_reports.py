
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

DATA = BASE / "data" / "processed"
REPORTS = BASE / "reports"

for folder in ["daily", "weekly", "monthly"]:
    (REPORTS / folder).mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA / "orders_mis.csv")

df["order_purchase_timestamp"] = pd.to_datetime(
    df["order_purchase_timestamp"], errors="coerce"
)

df["purchase_date"] = pd.to_datetime(
    df["purchase_date"], errors="coerce"
)

df["revenue"] = df["payment_total"]

# Include only records with a valid purchase date
df = df.dropna(subset=["order_purchase_timestamp"])

# Calculate delivery and order KPIs
def make_summary(data, group_column):

    result = data.groupby(group_column).agg(
        Total_Orders=("order_id", "nunique"),
        Total_Revenue=("revenue", "sum"),
        Average_Order_Value=("revenue", "mean"),
        Total_Items=("total_items", "sum"),
        Average_Review=("review_score", "mean"),
        Delivered_Orders=(
            "order_status",
            lambda x: (x == "delivered").sum()
        ),
        On_Time_Orders=("on_time", "sum"),
        Average_Delivery_Days=("delivery_days", "mean")
    ).reset_index()

    result["On_Time_Rate"] = (
        result["On_Time_Orders"]
        / result["Delivered_Orders"].replace(0, pd.NA)
        * 100
    )

    return result

# Daily MIS
daily = make_summary(df, "purchase_date")

# Weekly MIS
weekly = make_summary(df, "week_start")

# Monthly MIS
monthly = make_summary(df, "year_month")

# Save CSV reports
daily.to_csv(
    REPORTS / "daily" / "daily_mis.csv", index=False
)

weekly.to_csv(
    REPORTS / "weekly" / "weekly_mis.csv", index=False
)

monthly.to_csv(
    REPORTS / "monthly" / "monthly_mis.csv", index=False
)

# Load other reports
category = pd.read_csv(DATA / "category_mis.csv")
seller = pd.read_csv(DATA / "seller_mis.csv")
audit = pd.read_csv(DATA / "data_audit.csv")

# Create one Excel MIS workbook
with pd.ExcelWriter(
    REPORTS / "MIS_Reports.xlsx",
    engine="openpyxl"
) as writer:

    df.to_excel(
        writer, sheet_name="Orders_Detail", index=False
    )

    daily.to_excel(
        writer, sheet_name="Daily_MIS", index=False
    )

    weekly.to_excel(
        writer, sheet_name="Weekly_MIS", index=False
    )

    monthly.to_excel(
        writer, sheet_name="Monthly_MIS", index=False
    )

    category.to_excel(
        writer, sheet_name="Category_MIS", index=False
    )

    seller.to_excel(
        writer, sheet_name="Seller_MIS", index=False
    )

    audit.to_excel(
        writer, sheet_name="Data_Audit", index=False
    )

print("All MIS reports generated successfully!")
print("Excel file:", REPORTS / "MIS_Reports.xlsx")
