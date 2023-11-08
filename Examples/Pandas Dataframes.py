import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})
print(df)

# Remove the first 50 rows (assuming the DataFrame has at least 50 rows)
df = df.drop(df.index[:50])
print(df)
