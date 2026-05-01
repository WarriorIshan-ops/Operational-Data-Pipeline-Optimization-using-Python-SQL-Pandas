"""
Operational Data Pipeline Optimization
Author: Ishan Awasthi

Purpose:
Clean messy supply chain operational data and generate an analysis-ready dataset.
"""

import pandas as pd


RAW_FILE = "data/raw/supply_chain_raw_orders.csv"
OUTPUT_FILE = "data/processed/clean_supply_chain_data.csv"


def load_data(file_path: str) -> pd.DataFrame:
    """Load raw CSV data."""
    return pd.read_csv(file_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform raw operational data."""

    df = df.drop_duplicates()

    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce", format="mixed")
    df["Delivery_Date"] = pd.to_datetime(df["Delivery_Date"], errors="coerce", format="mixed")

    df["Cost"] = pd.to_numeric(df["Cost"], errors="coerce")
    df = df[df["Cost"] >= 0]

    df = df.dropna(subset=["Order_Date", "Delivery_Date"])
    df["Cost"] = df["Cost"].fillna(df["Cost"].mean())

    df["Delay_Days"] = (df["Delivery_Date"] - df["Order_Date"]).dt.days

    df["Delivery_Performance"] = df["Delay_Days"].apply(
        lambda x: "On Time" if x <= 5 else "Delayed"
    )

    df["Order_Date"] = df["Order_Date"].dt.strftime("%Y-%m-%d")
    df["Delivery_Date"] = df["Delivery_Date"].dt.strftime("%Y-%m-%d")

    return df


def save_data(df: pd.DataFrame, output_path: str) -> None:
    """Save cleaned dataset."""
    df.to_csv(output_path, index=False)


def main() -> None:
    df_raw = load_data(RAW_FILE)
    df_clean = clean_data(df_raw)
    save_data(df_clean, OUTPUT_FILE)

    print("ETL pipeline completed successfully.")
    print(f"Raw rows: {len(df_raw)}")
    print(f"Clean rows: {len(df_clean)}")
    print(f"Total delay days: {df_clean['Delay_Days'].sum()}")


if __name__ == "__main__":
    main()
