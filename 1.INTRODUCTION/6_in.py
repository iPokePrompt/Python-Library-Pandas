import pandas as pd
df = pd.read_csv("abc.csv")
print('Displaying the info of data set')
print(df.info())

data={
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df =pd.DataFrame(data)
print(df.info())