""" 
1- how big is your dataset?
2- what are the names of the columns?


shape and columns method - these methods are used to get the shape and columns of the dataset
"""
import pandas as pd
data={
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve","Frank"],
    "Age": [25, 30, 35, 40, 45, 50],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "Performance": [88, 92, 85, 90, 95, 80]
}
df = pd.DataFrame(data)
print(df)
print(f'shape:{df.shape}')
print(f'columns:{df.columns}')
      
