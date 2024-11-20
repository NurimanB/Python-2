import pandas as pd
import matplotlib.pyplot as plt

employees_df = pd.read_csv('D:\VsCode\python-2\week 12\Employee_Dataset.csv')

salary_distribution = employees_df.groupby('Department')['Salary'].sum()

# Plotting the bar chart
salary_distribution.plot(kind='bar', title='Salary Distribution Across Departments', ylabel='Total Salary', xlabel='Department')
plt.show()

