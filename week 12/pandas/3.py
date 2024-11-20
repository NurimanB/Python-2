import pandas as pd

employees_df = pd.read_csv('D:\VsCode\python-2\week 12\Employee_Dataset.csv')

grouped = employees_df.groupby('Department')

avg_salary = grouped['Salary'].mean()

total_emp = grouped["Name"].count()

print('Average salary per department:/n', avg_salary)
print('/nTotal amount of employees:/n', total_emp)