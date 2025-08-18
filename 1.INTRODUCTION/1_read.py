import pandas as pd;

# read a CSV file with latin1 encoding
# and print the DataFrame
df = pd.read_csv("abc.csv", encoding="latin1")

# df = pd.read_excel("abc.xlsx", engine="openpyxl")

# df = pd.read_json("abc.json")
print(df)


# when there is an error use utf-8 or latin 1 encoding