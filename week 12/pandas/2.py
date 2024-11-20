import pandas as pd

sales_df = pd.read_csv('D:\VsCode\python-2\week 12\Sales_Dataset.csv')

total_sales = sales_df['Sales'].sum()

avg_sales = sales_df['Sales'].mean()

max_sales = sales_df[sales_df['Sales'] == sales_df['Sales'].max()]
min_sales = sales_df[sales_df['Sales'] == sales_df['Sales'].min()]

print("Total Sales:", total_sales)
print("Average Sales Per Day:", avg_sales)
print("\nDay with Maximum Sales:\n", max_sales)
print("\nDay with Minimum Sales:\n", min_sales)
