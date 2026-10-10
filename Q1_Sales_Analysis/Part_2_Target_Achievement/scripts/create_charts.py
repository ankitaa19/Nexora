import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

INPUT_PATH = BASE_DIR / "outputs/tables/furniture_target_analysis.csv"
CHART_DIR = BASE_DIR / "outputs/charts"

CHART_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_PATH)

df["Month"] = pd.to_datetime(df["Month"], format="%b-%y")


# --------------------------------
# 1. Target vs Actual Sales
# --------------------------------
plt.figure(figsize=(11, 6))

plt.plot(
    df["Month"],
    df["Target"],
    marker="o",
    label="Target Sales"
)

plt.plot(
    df["Month"],
    df["Actual_Sales"],
    marker="o",
    label="Actual Sales"
)

plt.title("Furniture: Target vs Actual Sales")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.xticks(df["Month"], df["Month"].dt.strftime("%b-%y"), rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig(
    CHART_DIR / "furniture_target_vs_actual.png",
    dpi=150
)

plt.close()


# --------------------------------
# 2. Target Achievement %
# --------------------------------
plt.figure(figsize=(11, 6))

plt.plot(
    df["Month"],
    df["Achievement_%"],
    marker="o"
)

plt.axhline(
    100,
    linestyle="--",
    label="100% Target Achievement"
)

plt.title("Furniture Target Achievement by Month")
plt.xlabel("Month")
plt.ylabel("Achievement (%)")
plt.xticks(df["Month"], df["Month"].dt.strftime("%b-%y"), rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig(
    CHART_DIR / "furniture_target_achievement.png",
    dpi=150
)

plt.close()


# --------------------------------
# 3. MoM Target Change
# --------------------------------
plt.figure(figsize=(11, 6))

plt.plot(
    df["Month"],
    df["MoM_Target_Change_%"],
    marker="o"
)

plt.axhline(
    1.5,
    linestyle="--",
    label="Significant fluctuation threshold"
)

plt.title("Furniture Month-over-Month Target Change")
plt.xlabel("Month")
plt.ylabel("MoM Target Change (%)")
plt.xticks(df["Month"], df["Month"].dt.strftime("%b-%y"), rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig(
    CHART_DIR / "furniture_mom_target_change.png",
    dpi=150
)

plt.close()


print("Charts created successfully:")
print(CHART_DIR / "furniture_target_vs_actual.png")
print(CHART_DIR / "furniture_target_achievement.png")
print(CHART_DIR / "furniture_mom_target_change.png")
