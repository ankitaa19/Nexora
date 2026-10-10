import pandas as pd
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DIR = BASE_DIR / "data" / "processed"


# ============================================================
# LOAD DATA
# ============================================================

orders_path = PROCESSED_DIR / "list_of_orders.csv"
details_path = PROCESSED_DIR / "order_details.csv"

orders = pd.read_csv(orders_path)
details = pd.read_csv(details_path)


# ============================================================
# INPUT VALIDATION
# ============================================================

print("=" * 60)
print("INPUT DATA VALIDATION")
print("=" * 60)

print(f"\nOrders rows: {len(orders)}")
print(f"Order Details rows: {len(details)}")

print(
    f"Unique Order IDs in Orders: "
    f"{orders['Order ID'].nunique()}"
)

print(
    f"Unique Order IDs in Details: "
    f"{details['Order ID'].nunique()}"
)


# ============================================================
# MERGE
# ============================================================

merged = orders.merge(
    details,
    on="Order ID",
    how="inner",
    validate="one_to_many"
)


# ============================================================
# MERGE VALIDATION
# ============================================================

print("\n" + "=" * 60)
print("MERGE VALIDATION")
print("=" * 60)

print(f"\nMerged rows: {len(merged)}")

print(
    f"Unique Order IDs in merged data: "
    f"{merged['Order ID'].nunique()}"
)

print("\nMissing values after merge:")
print(merged.isna().sum())


# ============================================================
# CHECK DETAIL RECORD COVERAGE
# ============================================================

detail_ids = set(details["Order ID"])
merged_detail_ids = set(merged["Order ID"])

unmatched_detail_ids = detail_ids - merged_detail_ids

print("\n" + "=" * 60)
print("DETAIL RECORD MATCHING")
print("=" * 60)

print(
    f"\nUnmatched Order IDs from Details: "
    f"{len(unmatched_detail_ids)}"
)

if unmatched_detail_ids:
    print("\nUnmatched IDs:")
    print(sorted(unmatched_detail_ids))


# ============================================================
# CHECK ORDER COVERAGE
# ============================================================

order_ids = set(orders["Order ID"])
merged_order_ids = set(merged["Order ID"])

orders_without_details = order_ids - merged_order_ids

print(
    f"\nOrders without detail records: "
    f"{len(orders_without_details)}"
)

if orders_without_details:
    print("\nOrders without details:")
    print(sorted(orders_without_details))


# ============================================================
# DATA TYPES
# ============================================================

merged["Order Date"] = pd.to_datetime(
    merged["Order Date"]
)

merged["Amount"] = pd.to_numeric(
    merged["Amount"]
)

merged["Profit"] = pd.to_numeric(
    merged["Profit"]
)

merged["Quantity"] = pd.to_numeric(
    merged["Quantity"]
)


# ============================================================
# SAMPLE
# ============================================================

print("\n" + "=" * 60)
print("MERGED DATA SAMPLE")
print("=" * 60)

print(
    merged.head(10).to_string(index=False)
)


# ============================================================
# SAVE
# ============================================================

merged_path = (
    PROCESSED_DIR /
    "merged_order_data.csv"
)

merged.to_csv(
    merged_path,
    index=False
)


print("\n" + "=" * 60)
print("MERGE COMPLETE")
print("=" * 60)

print(
    f"\nMerged dataset saved to:\n{merged_path}"
)
