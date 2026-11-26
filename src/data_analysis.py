
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reports"

# Create reports folder
REPORT_DIR.mkdir(exist_ok=True)


def analyse_data():

    # 1. Load dataset
    file_path = DATA_DIR / "sales.csv"
    df = pd.read_csv(file_path)

    print("\n========== ORIGINAL DATA ==========")
    print(df)

    # 2. Data cleaning
    df["Date"] = pd.to_datetime(df["Date"])

    df["Product"] = df["Product"].fillna("Unknown")
    df["Category"] = df["Category"].fillna("Unknown")

    df["Quantity"] = df["Quantity"].fillna(
        df["Quantity"].median()
    )

    df["Price"] = df["Price"].fillna(
        df["Price"].median()
    )

    # Remove duplicate records
    df = df.drop_duplicates()

    # 3. Data manipulation using NumPy
    df["Revenue"] = np.where(
        df["Quantity"] > 0,
        df["Quantity"] * df["Price"],
        0
    )

    # 4. Data analysis using Pandas
    total_revenue = df["Revenue"].sum()
    average_revenue = df["Revenue"].mean()
    total_sales = df["Quantity"].sum()

    print("\n========== CLEANED DATA ==========")
    print(df)

    print("\n========== DATA ANALYSIS ==========")
    print("Total Revenue:", total_revenue)
    print("Average Revenue:", average_revenue)
    print("Total Quantity Sold:", total_sales)

    # 5. Product-wise sales
    product_sales = df.groupby(
        "Product"
    )["Revenue"].sum().sort_values(ascending=False)

    print("\n========== PRODUCT-WISE SALES ==========")
    print(product_sales)

    # 6. Save cleaned dataset
    df.to_csv(
        REPORT_DIR / "cleaned_sales.csv",
        index=False
    )

    # 7. Product-wise bar chart
    plt.figure(figsize=(10, 5))

    product_sales.plot(kind="bar")

    plt.title("Product-wise Revenue")
    plt.xlabel("Product")
    plt.ylabel("Revenue (INR)")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(REPORT_DIR / "sales_chart.png")
    plt.close()

    # 8. City-wise revenue chart
    city_sales = df.groupby(
        "City", as_index=False
    )["Revenue"].sum()

    plt.figure(figsize=(9, 5))

    sns.barplot(
        data=city_sales,
        x="City",
        y="Revenue"
    )

    plt.title("Total Revenue by City")
    plt.xlabel("City")
    plt.ylabel("Total Revenue (INR)")
    plt.xticks(rotation=20)
    plt.tight_layout()

    plt.savefig(REPORT_DIR / "city_chart.png")
    plt.close()

    # 9. Generate analysis report
    top_product = product_sales.idxmax() if not product_sales.empty else "No data"

    report = f"""
PYTHON DATA ANALYSIS REPORT
===========================

Total Revenue: {total_revenue}
Average Revenue: {average_revenue:.2f}
Total Quantity Sold: {total_sales}

Total Records After Cleaning: {len(df)}

Top Selling Product:
{top_product}

Product-wise Revenue:
{product_sales.to_string()}
"""

    # Save text report
    with open(
        REPORT_DIR / "analysis_report.txt",
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report)

    print("\nAnalysis completed successfully!")
    print("Check the reports folder for output files.")

    return df
