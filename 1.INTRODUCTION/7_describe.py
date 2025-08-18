# describe method - this method is used to describe the dataset
# It provides a summary of the dataset including count, mean, std, min, max, and quartiles
import pandas as pd
data={
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve","Frank"],
    "Age": [25, 30, 35, 40, 45, 50],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "Performance": [88, 92, 85, 90, 95, 80]
}

df = pd.DataFrame(data)
print('Displaying sample dataframe')
print(df)

print("Descriptive Statistics:")
print(df.describe())
