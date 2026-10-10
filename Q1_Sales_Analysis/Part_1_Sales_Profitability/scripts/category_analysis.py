import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DIR = BASE_DIR / "data" / "processed"

merged_path = PROCESSED_DIR / "merged_order_data.csv"

df = pd.read_csv(merged_path)

print("Dataset shape:", df.shape)
print("\nCategories:")
print(df["Category"].unique())


# ---------------------------------------------------------
# 1. TOTAL SALES BY CATEGORY
# ---------------------------------------------------------

sales_by_category = (
    df.groupby("Category", as_index=False)["Amount"]
      .sum()
      .rename(columns={"Amount": "Total Sales"})
      .sort_values("Total Sales", ascending=False)
)

print("\n" + "=" * 60)
print("TOTAL SALES BY CATEGORY")
print("=" * 60)

print(sales_by_category.to_string(index=False))


# ---------------------------------------------------------
# 2. AVERAGE PROFIT PER ORDER BY CATEGORY
# ---------------------------------------------------------

order_category_profit = (
    df.groupby(["Order ID", "Category"], as_index=False)["Profit"]
      .sum()
)

avg_profit_by_category = (
    order_category_profit
    .groupby("Category", as_index=False)["Profit"]
    .mean()
    .rename(columns={"Profit": "Average Profit per Order"})
    .sort_values("Average Profit per Order", ascending=False)
)

print("\n" + "=" * 60)
print("AVERAGE PROFIT PER ORDER BY CATEGORY")
print("=" * 60)

print(avg_profit_by_category.to_string(index=False))



# ---------------------------------------------------------
# 3. TOTAL PROFIT MARGIN BY CATEGORY
# ---------------------------------------------------------

profitability_by_category = (
    df.groupby("Category", as_index=False)
      .agg(
          Total_Sales=("Amount", "sum"),
          Total_Profit=("Profit", "sum")
      )
)

profitability_by_category["Profit Margin (%)"] = (
    profitability_by_category["Total_Profit"]
    / profitability_by_category["Total_Sales"]
    * 100
)

profitability_by_category = profitability_by_category.sort_values(
    "Profit Margin (%)",
    ascending=False
)

print("\n" + "=" * 60)
print("PROFIT MARGIN BY CATEGORY")
print("=" * 60)

print(
    profitability_by_category.to_string(
        index=False,
        formatters={
            "Profit Margin (%)": "{:.2f}".format
        }
    )
)


# ---------------------------------------------------------
# 4. SUB-CATEGORY PERFORMANCE
# ---------------------------------------------------------

subcategory_performance = (
    df.groupby(["Category", "Sub-Category"], as_index=False)
      .agg(
          Total_Sales=("Amount", "sum"),
          Total_Profit=("Profit", "sum")
      )
)

subcategory_performance["Profit Margin (%)"] = (
    subcategory_performance["Total_Profit"]
    / subcategory_performance["Total_Sales"]
    * 100
)

subcategory_performance = subcategory_performance.sort_values(
    ["Category", "Total_Sales"],
    ascending=[True, False]
)

print("\n" + "=" * 60)
print("SUB-CATEGORY PERFORMANCE")
print("=" * 60)

print(
    subcategory_performance.to_string(
        index=False,
        formatters={
            "Profit Margin (%)": "{:.2f}".format
        }
    )
)



# ---------------------------------------------------------
# 5. FINAL CATEGORY PERFORMANCE SUMMARY
# ---------------------------------------------------------

category_summary = (
    sales_by_category
    .merge(
        avg_profit_by_category,
        on="Category",
        how="left"
    )
    .merge(
        profitability_by_category[
            ["Category", "Total_Profit", "Profit Margin (%)"]
        ],
        on="Category",
        how="left"
    )
)

category_summary = category_summary[
    [
        "Category",
        "Total Sales",
        "Total_Profit",
        "Average Profit per Order",
        "Profit Margin (%)"
    ]
]

print("\n" + "=" * 60)
print("FINAL CATEGORY PERFORMANCE SUMMARY")
print("=" * 60)

print(
    category_summary.to_string(
        index=False,
        formatters={
            "Average Profit per Order": "{:.2f}".format,
            "Profit Margin (%)": "{:.2f}".format
        }
    )
)


# ---------------------------------------------------------
# 6. SAVE FINAL CATEGORY SUMMARY
# ---------------------------------------------------------

OUTPUT_DIR = BASE_DIR / "outputs" / "tables"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

output_path = OUTPUT_DIR / "category_performance_summary.csv"

category_summary.to_csv(output_path, index=False)

print("\n" + "=" * 60)
print("OUTPUT SAVED")
print("=" * 60)

print(f"\nFinal category summary saved to:\n{output_path}")
