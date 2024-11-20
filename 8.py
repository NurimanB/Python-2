import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Product": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "A", "B", "C"],
    "Region": ["North", "South", "East", "West", "North", "South", "East", "West", "North", "South", "East", "West"],
    "Sales": [20000, np.nan, 27000, 31000, 35000, 40000, np.nan, 42000, 38000, 45000, 36000, 48000],
    "Price": [300, 250, 320, 300, 250, 320, 300, 250, 320, 300, 250, 320],
    "Date": pd.to_datetime(["2024-01-15", "2024-02-20", "2024-03-10", "2024-04-18", "2024-05-22", "2024-06-05",
                            "2024-07-12", "2024-08-25", "2024-09-07", "2024-10-19", "2024-11-15", "2024-12-01"])
}

df = pd.DataFrame(data)

avg_sales = df["Sales"].mean()
df["Sales"].fillna(avg_sales, inplace=True)

df["Revenue"] = df["Sales"] * df["Price"]


product_summary = df.groupby("Product")[["Sales", "Revenue"]].sum()

region_summary = df.groupby("Region")["Revenue"].sum()

product_avg_revenue = df.groupby("Product")["Revenue"].mean()
top_avg_revenue_product = product_avg_revenue.idxmax()

plt.figure(figsize=(10, 5))
product_summary["Revenue"].plot(kind="bar", color="skyblue")
plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

plt.figure(figsize=(7, 7))
region_summary.plot(kind="pie", autopct='%1.1f%%', startangle=140)
plt.title("Revenue Share by Region")
plt.ylabel("")
plt.show()

print("Product Summary:\n", product_summary)
print("\nRegion Summary:\n", region_summary)
print("\nProduct with the Highest Average Revenue:", top_avg_revenue_product)
