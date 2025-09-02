# sorting data
# a,b,c.....
# sorting data 1 column sort_values()

# df.sort_values(by='column_name', ascending=True/False, inplace=True)

import pandas as pd
data ={
  "Name":['Arun','Varun','Karun'],
  "Age":[28,32,22],
  "Salary":[50000,60000,70000]
 }

df = pd.DataFrame(data)
print(df)


df.sort_values(by='Age', ascending=True, inplace=True)
print(df)

# true - ascending
# false = descending

