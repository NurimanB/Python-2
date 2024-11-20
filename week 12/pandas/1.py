import pandas as pd

employees_df = pd.read_csv('D:\VsCode\python-2\week 12\Employee_Dataset.csv')

employees_df['Bonus'] = employees_df['Salary'] * 0.1

filtered_employees = employees_df[employees_df['Salary'] > 50000]

print("Updated Employee DataFrame with Bonus:\n", employees_df)
print("\nFiltered Employees (Salary > 50,000):\n", filtered_employees)
