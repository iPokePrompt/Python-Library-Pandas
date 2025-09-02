"""
concatenation - combining two or more dataframes

vertically or horizontally

pd.concat([df1, df2], axis=0, ignore_index=True)  # vertical concatenation
pd.concat([df1, df2], axis=1, ignore_index=True)  # horizontal concatenation
"""

import pandas as pd

df_Region1 = pd.DataFrame({
    "Customer Id": [1, 2, 3],
    "Name": ['Arun', 'Varun', 'Karun'],
    "Age": [28, 32, 22],
    "Salary": [50000, 60000, 70000]
})

df_Region2 = pd.DataFrame({
    "Customer Id": [4, 5, 6],
    "Name": ['John', 'Doe', 'Smith'],
    "Age": [30, 35, 40],
    "Salary": [80000, 90000, 100000]
})
# vertical concatenation
df = pd.concat([df_Region1, df_Region2], axis=0, ignore_index=True)
print(df)   

# horizontal concatenation
df = pd.concat([df_Region1, df_Region2], axis=1, ignore_index=True)
print(df)


