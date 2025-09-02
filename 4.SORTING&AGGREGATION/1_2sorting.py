#  df.sort_values(by=['Age','Salary'], ascending=True, inplace=True)

import pandas as pd
data ={
  "Name":['Arun','Varun','Karun'],
  "Age":[28,32,22],
  "Salary":[50000,60000,70000]
 }

df = pd.DataFrame(data)
print(df)


df.sort_values(by=['Age','Salary'], ascending=[False, False], inplace=True)
print(df)