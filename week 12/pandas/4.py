import pandas as pd

sales_data = pd.DataFrame({
    'Item': ['Apple', 'Banana', 'Orange', 'Dragonfruit'],
    'Price': [100, None, None, 300],
    'Stock': [10, 0, None, 3]
})

sales_data['Price'].fillna(sales_data['Price'].mean(), inplace=True)

sales_data['Stock'].fillna(0, inplace=True)

print("Dataset after handling missing data:\n", sales_data)
