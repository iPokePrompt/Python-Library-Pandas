import pandas as pd
data={
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve","Frank"],
    "Age": [25, 30, 35, 40, 45, 50],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "Performance": [88, 92, 85, 90, 95, 80]
}
df = pd.DataFrame(data)
print(df)

# df.drop(columns=<column_name>, inplace=True)
#df.drop(columns='City', inplace=True)
#print(df)

# for removing multiple columns
df.drop(columns=['City', 'Performance'], inplace=True)
print(df)