#Interpolation - Fill missing values using interpolation 

"""
10
20
NaN                 estimated value :30
40
50
"""

# use of interpolation - preserve data integrity , smooth trends , fill gaps, maintain consistency, improve accuracy, avoid data loss, 

# interpolate() - Fill missing values using interpolation

import pandas as pd
data={
    "Name": ["Alice", None, "Charlie", "David", "Eve","Frank"],
    "Age": [25, None, 35, 40, 45, 50],
    "City": ["New York", None, "Chicago", "Houston", "Phoenix", "Philadelphia"],
    "Performance": [88, None, 85, 90, 95, 80]
}
df = pd.DataFrame(data)
print(df)

df.interpolate(method='linear',axis=0, inplace=True)
print(df)







# methods- linear,polynomial,time (imp 3), qudratic , cubic , spline