# Handling Missing Data
# dropna()- Remove missing values
# axis=0 : Drop rows with missing values
# axis=1 : Drop columns with missing values
#fillna()- Fill missing values
# df.fillna(value, inplace=True)

import pandas as pd
data={
    "Name": ["Alice", None, "Charlie", "David", "Eve","Frank"],
    "Age": [25, None, 35, 40, 45, 50],
    "City": ["New York", None, "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "Performance": [88, None, 85, 90, 95, 80]
}
df = pd.DataFrame(data)
print(df)


# df.fillna(0, inplace=True)
# print(df)

# df.dropna(axis=0, inplace=True) 
#  print(df)

# now we have no missing values so no rows will be dropped
# and we can fix age mean
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Performance'].fillna(df['Performance'].mean(), inplace=True)
print(df)