import pandas as pd
 

 # head(n)- returns the first n rows of the DataFrame
 # tail(n )- returns the last n rows of the DataFrame
 # if we not pass n , # it returns the first 5 rows by default
df = pd.read_csv("abc.csv")

print('First 3 rows of the DataFrame:')
print(df.head(3))
print('\nLast 3 rows of the DataFrame:')
print(df.tail(3))

