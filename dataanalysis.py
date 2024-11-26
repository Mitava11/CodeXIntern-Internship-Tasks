import pandas as pd

df = pd.read_csv('data.csv')

# display the first few rows from the data
print(df.head())

# get descriptive statistics for all numerical rows
print(df.describe())

# find missing values in each column
mv = df.isnull().sum()
print("Missing values:\n", mv)

# find the average of a column
avg = df['Age'].mean()
print(f"Average of Age:{avg}")

# find number of unique values from a column
uv = df['Age'].nunique()
print(f"unique values: {uv}")