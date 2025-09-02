import pandas as pd
data={
    "Name": ["Alice", None, "Charlie", "David", "Eve","Frank"],
    "Age": [25, None, 35, 40, 45, 50],
    "City": ["New York", None, "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "Performance": [88, None, 85, 90, 95, 80]
}
df = pd.DataFrame(data)
print(df)

print(df.isnull())

print(df.isnull().sum())   # Count of missing values in each column
