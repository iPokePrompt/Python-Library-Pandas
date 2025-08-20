import pandas as pd
data={
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve","Frank"],
    "Age": [25, 30, 35, 40, 45, 50],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "Performance": [88, 92, 85, 90, 95, 80]
}
df = pd.DataFrame(data)

#  using square bracket df["column_name"]= some data 
print(df)
df['increment_age'] = df['Age'] * 0.1
print(df)

# using insert methods
df.insert(2, 'increment_age_insert', df["Age"]*0.1)
print(df)