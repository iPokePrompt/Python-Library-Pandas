import pandas as pd
data={
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve","Frank"],
    "Age": [25, 30, 35, 40, 45, 50],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "Performance": [88, 92, 85, 90, 95, 80]
}

df = pd.DataFrame(data) 
print('Displaying the first 3 rows of the DataFrame:')
print(df)

print("Name( single colummn return series):")
print(df["Name"])

print("SELECTINNG MULTIPE COLUMMN")
print(df[["Name", "Age"]])

print("selecting whose age is greater that 30 and less that 45")
print(df[(df["Age"] > 30) & (df["Age"] < 45)])

print("selecting whose performance is greater than 90")
print(df[df["Performance"] > 90])

print("selecting whose name is charlie")
print(df[df["Name"] == "Charlie"])

print("selecting whose name is not charlie")
print(df[df["Name"] != "Charlie"])

print("selecting employees older than 35 or performance greater than 90")
print(df[(df["Age"] > 35) | (df["Performance"] > 90)])
