import pandas as pd
data={
  "Time": [1, 2, 3, 4, 5],
  "Value": [10, None, 30,None, 50]
}
df = pd.DataFrame(data)
print(df)
df.interpolate(method='linear', inplace=True)
print(df)

"""
uses -
1- timer series data
2- numeric data with trend
3- avvoid dropping rows
4- 
"""