import pandas as pd
data={
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve","Frank"],
    "Age": [25, 30, 35, 40, 45, 50],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "Performance": [88, 92, 85, 90, 95, 80]
}
df = pd.DataFrame(data)

# .loc[]
# df.loc[<row_index>, <column_name>] = <new_value>
df.loc[0, 'Age'] = 26
print(df)

# increasing performance by 5%
df['Performance']=df['Performance']*1.05
print(df)