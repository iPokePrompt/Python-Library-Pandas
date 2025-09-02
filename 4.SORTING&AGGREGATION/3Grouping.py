"""
grouped = df.groupby("Column Name")

"""

import pandas as pd
data ={
  "Name":['Arun','Varun','Karun','Narun','Marun'],
  "Age":[28,32,22,34,28],
  "Salary":[50000,60000,70000,52000,48000]
 }

df = pd.DataFrame(data)

grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

"""
df.groupby("Age")
age = 22>[45000]
age = 28 [50000,48000] = 98000
age = 32 [60000] = 60000
age = 34 [52000] = 52000
"""

"""
sum()
mean()
median()
min()
max()
std()  standard deviation - definition - measures the amount of variation or dispersion of a set of values.
"""