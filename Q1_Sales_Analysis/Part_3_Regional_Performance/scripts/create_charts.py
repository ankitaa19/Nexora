from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[3]

TABLES_DIR = BASE_DIR / "Q1_Sales_Analysis" / "Part_3_Regional_Performance" / "outputs" / "tables"
CHARTS_DIR = BASE_DIR / "Q1_Sales_Analysis" / "Part_3_Regional_Performance" / "outputs" / "charts"

CHARTS_DIR.mkdir(parents=True, exist_ok=True)

state_df = pd.read_csv(TABLES_DIR / "top_5_states_analysis.csv")
city_df = pd.read_csv(TABLES_DIR / "top_5_states_city_analysis.csv")


# 1. Order count by state
plt.figure(figsize=(10, 6))
plt.bar(state_df["State"], state_df["Order_Count"])
plt.title("Top 5 States by Order Count")
plt.xlabel("State")
plt.ylabel("Order Count")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(CHARTS_DIR / "orders_by_top_5_states.png", dpi=150)
plt.close()


# 2. Average profit by state
plt.figure(figsize=(10, 6))
plt.bar(state_df["State"], state_df["Average_Profit"])
plt.title("Average Profit per Order — Top 5 States")
plt.xlabel("State")
plt.ylabel("Average Profit per Order (₹)")
plt.xticks(rotation=30, ha="right")
plt.axhline(0, linewidth=1)
plt.tight_layout()
plt.savefig(CHARTS_DIR / "average_profit_by_top_5_states.png", dpi=150)
plt.close()


# 3. City-level profitability
city_df = city_df.sort_values("Average_Profit")

plt.figure(figsize=(11, 7))
plt.barh(
    city_df["City"] + " (" + city_df["State"] + ")",
    city_df["Average_Profit"],
)
plt.title("City-Level Average Profit per Order — Top 5 States")
plt.xlabel("Average Profit per Order (₹)")
plt.ylabel("City")
plt.axvline(0, linewidth=1)
plt.tight_layout()
plt.savefig(CHARTS_DIR / "city_profitability_top_5_states.png", dpi=150)
plt.close()

print("Charts created successfully:")
for path in sorted(CHARTS_DIR.glob("*.png")):
    print(f"- {path.name}")
