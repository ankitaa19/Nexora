import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

LIST_ORDERS_PATH = BASE_DIR / "data" / "processed" / "list_of_orders.csv"
MERGED_DATA_PATH = (
    BASE_DIR.parent
    / "Part_1_Sales_Profitability"
    / "data"
    / "processed"
    / "merged_order_data.csv"
)

OUTPUT_DIR = BASE_DIR / "outputs" / "tables"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# --------------------------------------------------
# 1. Load datasets
# --------------------------------------------------

list_orders = pd.read_csv(LIST_ORDERS_PATH)
merged_data = pd.read_csv(MERGED_DATA_PATH)

print("List of Orders shape:", list_orders.shape)
print("Merged Order Data shape:", merged_data.shape)


# --------------------------------------------------
# 2. Create one record per Order ID
# --------------------------------------------------

order_metrics = (
    merged_data
    .groupby("Order ID", as_index=False)
    .agg(
        Total_Sales=("Amount", "sum"),
        Total_Profit=("Profit", "sum")
    )
)

print("Unique orders in order metrics:", order_metrics["Order ID"].nunique())


# --------------------------------------------------
# 3. Attach order-level sales/profit to List of Orders
# --------------------------------------------------

orders = list_orders.merge(
    order_metrics,
    on="Order ID",
    how="left",
    validate="one_to_one"
)

print("Regional dataset shape:", orders.shape)

if orders["Total_Sales"].isna().any():
    raise ValueError("Some orders are missing sales/profit metrics.")

if orders["Total_Profit"].isna().any():
    raise ValueError("Some orders are missing profit metrics.")


# --------------------------------------------------
# 4. State-level analysis
# --------------------------------------------------

state_analysis = (
    orders
    .groupby("State")
    .agg(
        Order_Count=("Order ID", "nunique"),
        Total_Sales=("Total_Sales", "sum"),
        Average_Profit=("Total_Profit", "mean")
    )
    .reset_index()
    .sort_values(
        ["Order_Count", "Total_Sales"],
        ascending=[False, False]
    )
)

top_5_states = state_analysis.head(5).copy()

top_5_states["Total_Sales"] = top_5_states["Total_Sales"].round(2)
top_5_states["Average_Profit"] = top_5_states["Average_Profit"].round(2)

print("\nTop 5 States:")
print(top_5_states.to_string(index=False))


# --------------------------------------------------
# 5. City-level analysis within top 5 states
# --------------------------------------------------

top_states = top_5_states["State"].tolist()

city_analysis = (
    orders[orders["State"].isin(top_states)]
    .groupby(["State", "City"])
    .agg(
        Order_Count=("Order ID", "nunique"),
        Total_Sales=("Total_Sales", "sum"),
        Average_Profit=("Total_Profit", "mean")
    )
    .reset_index()
    .sort_values(
        ["State", "Order_Count"],
        ascending=[True, False]
    )
)

city_analysis["Total_Sales"] = city_analysis["Total_Sales"].round(2)
city_analysis["Average_Profit"] = city_analysis["Average_Profit"].round(2)


# --------------------------------------------------
# 6. Identify city-level improvement candidates
# --------------------------------------------------

improvement_candidates = (
    city_analysis[
        city_analysis["Average_Profit"] < 0
    ]
    .sort_values("Average_Profit")
    .reset_index(drop=True)
)

# --------------------------------------------------
# 7. Save outputs
# --------------------------------------------------

top_5_states.to_csv(
    OUTPUT_DIR / "top_5_states_analysis.csv",
    index=False
)

city_analysis.to_csv(
    OUTPUT_DIR / "top_5_states_city_analysis.csv",
    index=False
)

improvement_candidates.to_csv(
    OUTPUT_DIR / "regional_improvement_candidates.csv",
    index=False
)

print("\nSaved:")
print("- top_5_states_analysis.csv")
print("- top_5_states_city_analysis.csv")
print("- regional_improvement_candidates.csv")
