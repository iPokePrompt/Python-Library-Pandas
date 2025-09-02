
"""
pd.merge(df1,df2, on="Column Name",how="type of join")
types of join - 
"""

import pandas as pd
# customer dataframe
df_customer = pd.DataFrame({
    "Customer Id": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"]
})

# order dataframe
df_order = pd.DataFrame({
    "Order Id": [101, 102, 103],
    "Customer Id": [1, 2, 4],
    "Amount": [250, 150, 200]
})


# merge

df_merge=pd.merge(df_customer, df_order, on="Customer Id", how="inner")
print(df_merge)

df_merge1=pd.merge(df_customer, df_order, on="Customer Id", how="outer")
print(df_merge1)

df_merge2=pd.merge(df_customer, df_order, on="Customer Id", how="left")
print(df_merge2)

df_merge3=pd.merge(df_customer, df_order, on="Customer Id", how="right")
print(df_merge3)

df_merge4=pd.merge(df_customer, df_order, on="Customer Id", how="cross")
print(df_merge4)


""""
cross join

df1= m
df2 = n
cross =m*n

"""