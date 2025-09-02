"""
df["Column Name"].mean()
df["Column Name"].median()
df["Column Name"].std()
...
"""

import pandas as pd
data ={
  "Name":['Arun','Varun','Karun'],
  "Age":[28,32,22],
  "Salary":[50000,60000,70000]
 }

df = pd.DataFrame(data)


avg_salary = df["Salary"].mean()
print(avg_salary)