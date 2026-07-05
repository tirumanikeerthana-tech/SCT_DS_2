import pandas as pd

df = pd.read_csv("C:/Users/Rutanshi/OneDrive/Documents/Titanic-Dataset.csv")

print(df.head())
print(df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].median())

print(df.info())
