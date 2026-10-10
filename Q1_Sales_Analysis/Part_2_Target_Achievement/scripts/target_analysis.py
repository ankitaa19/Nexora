import pandas as pd
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[1]

TARGET_PATH = BASE_DIR / "data/processed/sales_target_clean.csv"
SALES_PATH = (
    BASE_DIR
    / "../Part_1_Sales_Profitability/data/processed/merged_order_data.csv"
)

OUTPUT_PATH = BASE_DIR / "outputs/tables/furniture_target_analysis.csv"


# -----------------------------
# Load target data
# -----------------------------
targets = pd.read_csv(TARGET_PATH)

furniture_targets = targets[
    targets["Category"] == "Furniture"
].copy()

furniture_targets["Month"] = pd.to_datetime(
    furniture_targets["Month"],
    format="%b-%y"
)

# Calculate month-over-month target change
furniture_targets["MoM_Target_Change_%"] = (
    furniture_targets["Target"].pct_change() * 100
)


# -----------------------------
# Load actual sales data
# -----------------------------
sales = pd.read_csv(SALES_PATH)

sales["Order Date"] = pd.to_datetime(sales["Order Date"])

furniture_sales = sales[
    sales["Category"] == "Furniture"
].copy()

# Monthly actual Furniture sales
monthly_sales = (
    furniture_sales
    .groupby(furniture_sales["Order Date"].dt.to_period("M"))["Amount"]
    .sum()
    .reset_index()
)

monthly_sales.columns = ["Month", "Actual_Sales"]

monthly_sales["Month"] = monthly_sales["Month"].dt.to_timestamp()


# -----------------------------
# Merge target and actual
# -----------------------------
analysis = furniture_targets.merge(
    monthly_sales,
    on="Month",
    how="left"
)

# Target achievement
analysis["Achievement_%"] = (
    analysis["Actual_Sales"]
    / analysis["Target"]
    * 100
)

# Actual sales minus target
analysis["Gap"] = (
    analysis["Actual_Sales"]
    - analysis["Target"]
)

# Absolute percentage-point deviation from 100%
analysis["Achievement_Deviation_%"] = (
    analysis["Achievement_%"] - 100
)


# -----------------------------
# Identify significant target
# fluctuations
# -----------------------------
# A target increase greater than 1.5%
# is treated as a significant fluctuation
analysis["Significant_Target_Fluctuation"] = (
    analysis["MoM_Target_Change_%"].abs() > 1.5
)


# -----------------------------
# Format month
# -----------------------------
analysis["Month"] = analysis["Month"].dt.strftime("%b-%y")


# -----------------------------
# Save results
# -----------------------------
OUTPUT_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)

analysis.to_csv(
    OUTPUT_PATH,
    index=False
)


# -----------------------------
# Display results
# -----------------------------
print("\nFurniture Target Analysis:\n")

print(
    analysis[
        [
            "Month",
            "Target",
            "Actual_Sales",
            "MoM_Target_Change_%",
            "Achievement_%",
            "Gap",
            "Significant_Target_Fluctuation",
        ]
    ].to_string(
        index=False,
        formatters={
            "MoM_Target_Change_%": lambda x:
                "—" if pd.isna(x) else f"{x:.2f}%",
            "Achievement_%": lambda x:
                f"{x:.1f}%",
            "Gap": lambda x:
                f"₹{x:,.0f}",
        }
    )
)

print(f"\nSaved analysis to:")
print(OUTPUT_PATH)
