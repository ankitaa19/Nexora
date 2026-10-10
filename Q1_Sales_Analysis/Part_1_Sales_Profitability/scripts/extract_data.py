import pdfplumber
import pandas as pd
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# KNOWN STATES
# ============================================================

# The PDF extraction sometimes removes the space between
# State and City, so we use the known state names to identify
# where the State column ends and the City column begins.

STATES = [
    "Andhra Pradesh",
    "Bihar",
    "Delhi",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jammu and Kashmir",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Nagaland",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Uttar Pradesh",
    "West Bengal",
]


# ============================================================
# PDF TEXT EXTRACTION
# ============================================================

def extract_lines(pdf_path):
    """
    Extract all non-empty text lines from a PDF.
    """

    lines = []

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:

                page_lines = [
                    line.strip()
                    for line in text.splitlines()
                    if line.strip()
                ]

                lines.extend(page_lines)

    return lines


# ============================================================
# LIST OF ORDERS PARSER
# ============================================================

def parse_list_of_orders(pdf_path):
    """
    Parse the List of Orders PDF into a DataFrame.
    """

    lines = extract_lines(pdf_path)

    # Remove the header
    lines = [
        line
        for line in lines
        if not line.startswith("Order ID ")
    ]

    records = []

    for line in lines:

        parts = line.split(maxsplit=3)

        if len(parts) != 4:
            raise ValueError(
                f"Unexpected order row: {line}"
            )

        order_id, order_date, customer_name, location = parts

        # ----------------------------------------------------
        # Fix known PDF extraction artifact
        # ----------------------------------------------------
        #
        # Original PDF extraction:
        #
        # Jammu and KashKmairshmir
        #
        # Intended structure:
        #
        # State = Jammu and Kashmir
        # City  = Kashmir
        #
        # Normalize it before identifying the state.
        # ----------------------------------------------------

        location = location.replace(
            "Jammu and KashKmairshmir",
            "Jammu and Kashmir Kashmir"
        )

        # ----------------------------------------------------
        # Identify State and City
        # ----------------------------------------------------

        state = None
        city = None

        # Longest states first so that states such as
        # "Madhya Pradesh" are matched correctly.
        for possible_state in sorted(
            STATES,
            key=len,
            reverse=True
        ):

            if location.startswith(possible_state):

                state = possible_state

                city = location[
                    len(possible_state):
                ].strip()

                break

        # ----------------------------------------------------
        # Validation
        # ----------------------------------------------------

        if state is None:
            raise ValueError(
                f"Could not identify state: {line}"
            )

        if not city:
            raise ValueError(
                f"Could not identify city: {line}"
            )

        # ----------------------------------------------------
        # Store record
        # ----------------------------------------------------

        records.append(
            {
                "Order ID": order_id,
                "Order Date": order_date,
                "CustomerName": customer_name,
                "State": state,
                "City": city,
            }
        )

    return pd.DataFrame(records)


# ============================================================
# ORDER DETAILS PARSER
# ============================================================

def parse_order_details(pdf_path):
    """
    Parse the Order Details PDF into a DataFrame.
    """

    lines = extract_lines(pdf_path)

    # Remove the header
    lines = [
        line
        for line in lines
        if not line.startswith("Order ID ")
    ]

    records = []

    for line in lines:

        parts = line.split()

        if len(parts) < 6:
            raise ValueError(
                f"Unexpected order-detail row: {line}"
            )

        order_id = parts[0]
        amount = parts[1]
        profit = parts[2]
        quantity = parts[3]
        category = parts[4]

        # Sub-category can contain spaces,
        # so join everything after Category.
        sub_category = " ".join(parts[5:])

        records.append(
            {
                "Order ID": order_id,
                "Amount": amount,
                "Profit": profit,
                "Quantity": quantity,
                "Category": category,
                "Sub-Category": sub_category,
            }
        )

    return pd.DataFrame(records)


# ============================================================
# MAIN
# ============================================================

def main():

    # --------------------------------------------------------
    # Input PDF paths
    # --------------------------------------------------------

    orders_pdf = (
        RAW_DIR /
        "List_of_Orders_-_List_of_Orders.pdf"
    )

    details_pdf = (
        RAW_DIR /
        "Order_Details_-_Order_Details.pdf"
    )

    # --------------------------------------------------------
    # Parse PDFs
    # --------------------------------------------------------

    orders = parse_list_of_orders(
        orders_pdf
    )

    details = parse_order_details(
        details_pdf
    )

    # --------------------------------------------------------
    # Convert data types
    # --------------------------------------------------------

    orders["Order Date"] = pd.to_datetime(
        orders["Order Date"],
        format="%d-%m-%Y"
    )

    details["Amount"] = pd.to_numeric(
        details["Amount"]
    )

    details["Profit"] = pd.to_numeric(
        details["Profit"]
    )

    details["Quantity"] = pd.to_numeric(
        details["Quantity"]
    )

    # --------------------------------------------------------
    # Save processed CSV files
    # --------------------------------------------------------

    orders_path = (
        PROCESSED_DIR /
        "list_of_orders.csv"
    )

    details_path = (
        PROCESSED_DIR /
        "order_details.csv"
    )

    orders.to_csv(
        orders_path,
        index=False
    )

    details.to_csv(
        details_path,
        index=False
    )

    # ========================================================
    # VALIDATION
    # ========================================================

    print()
    print("=" * 60)
    print("EXTRACTION VALIDATION")
    print("=" * 60)

    # --------------------------------------------------------
    # Orders validation
    # --------------------------------------------------------

    print()
    print("LIST OF ORDERS")
    print("-" * 60)

    print(
        f"Orders rows: {len(orders)}"
    )

    print(
        f"Unique Order IDs: "
        f"{orders['Order ID'].nunique()}"
    )

    print(
        f"Duplicate Order IDs: "
        f"{orders['Order ID'].duplicated().sum()}"
    )

    # --------------------------------------------------------
    # Order Details validation
    # --------------------------------------------------------

    print()
    print("ORDER DETAILS")
    print("-" * 60)

    print(
        f"Order Details rows: {len(details)}"
    )

    print(
        f"Unique Order IDs: "
        f"{details['Order ID'].nunique()}"
    )

    print(
        f"Duplicate Order IDs: "
        f"{details['Order ID'].duplicated().sum()}"
    )

    # --------------------------------------------------------
    # Column validation
    # --------------------------------------------------------

    print()
    print("ORDERS COLUMNS")
    print("-" * 60)

    print(
        list(orders.columns)
    )

    print()
    print("ORDER DETAILS COLUMNS")
    print("-" * 60)

    print(
        list(details.columns)
    )

    # --------------------------------------------------------
    # Missing value validation
    # --------------------------------------------------------

    print()
    print("MISSING VALUES - ORDERS")
    print("-" * 60)

    print(
        orders.isna().sum()
    )

    print()
    print("MISSING VALUES - ORDER DETAILS")
    print("-" * 60)

    print(
        details.isna().sum()
    )

    # --------------------------------------------------------
    # Data type validation
    # --------------------------------------------------------

    print()
    print("DATA TYPES - ORDERS")
    print("-" * 60)

    print(
        orders.dtypes
    )

    print()
    print("DATA TYPES - ORDER DETAILS")
    print("-" * 60)

    print(
        details.dtypes
    )

    # --------------------------------------------------------
    # Sample records
    # --------------------------------------------------------

    print()
    print("FIRST 5 ORDERS")
    print("-" * 60)

    print(
        orders.head().to_string(index=False)
    )

    print()
    print("FIRST 5 ORDER DETAILS")
    print("-" * 60)

    print(
        details.head().to_string(index=False)
    )

    # --------------------------------------------------------
    # Check Jammu and Kashmir parsing
    # --------------------------------------------------------

    print()
    print("JAMMU AND KASHMIR CHECK")
    print("-" * 60)

    jammu_rows = orders[
        orders["State"] == "Jammu and Kashmir"
    ]

    print(
        jammu_rows[
            ["Order ID", "State", "City"]
        ].to_string(index=False)
    )

    print(
        f"\nJammu and Kashmir rows: "
        f"{len(jammu_rows)}"
    )

    # --------------------------------------------------------
    # Output paths
    # --------------------------------------------------------

    print()
    print("PROCESSED FILES CREATED")
    print("-" * 60)

    print(orders_path)
    print(details_path)

    print()
    print("=" * 60)
    print("EXTRACTION COMPLETE")
    print("=" * 60)


# ============================================================
# SCRIPT ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
