import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TABLES_DIR = BASE_DIR / "outputs" / "tables"
CHARTS_DIR = BASE_DIR / "outputs" / "charts"

CHARTS_DIR.mkdir(parents=True, exist_ok=True)

summary_path = TABLES_DIR / "category_performance_summary.csv"

df = pd.read_csv(summary_path)

# ---------------------------------------------------------
# 1. TOTAL SALES BY CATEGORY
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(df["Category"], df["Total Sales"])

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales (₹)")

plt.tight_layout()

sales_chart_path = CHARTS_DIR / "total_sales_by_category.png"
plt.savefig(sales_chart_path, dpi=300)
plt.close()

print(f"Sales chart saved to:\n{sales_chart_path}")


# ---------------------------------------------------------
# 2. PROFIT MARGIN BY CATEGORY
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(df["Category"], df["Profit Margin (%)"])

plt.title("Profit Margin by Category")
plt.xlabel("Category")
plt.ylabel("Profit Margin (%)")

plt.tight_layout()

margin_chart_path = CHARTS_DIR / "profit_margin_by_category.png"
plt.savefig(margin_chart_path, dpi=300)
plt.close()

print(f"Profit margin chart saved to:\n{margin_chart_path}")
