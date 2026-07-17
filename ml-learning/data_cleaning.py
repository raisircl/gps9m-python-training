import pandas as pd

df = pd.read_csv("dirty_student_performance.csv")

#print(df)
#print(df.head())
print("Rows and Columns:")
print(df.shape)

print("Column Names:")
print(df.columns)

print("Dataset Info:")
print(df.info())

print("Count missing values in each column:")
print(df.isnull().sum())

print("Count total missing values:")
print(df.isnull().sum().sum())

print("Show Missing rows:")
print(df[df.isnull().any(axis=1)])

# 1. Remove the '%' sign and convert to float
df["attendance"] = (
    df["attendance"].astype(str).str.replace("%", "")
)
df["attendance"] = (
    df["attendance"].astype(str).str.replace("zero", "0")
)
df["attendance"] = (
    df["attendance"].astype(str).str.replace("na", "0").astype(float)
)
df['attendance'] = df['attendance'].fillna(0)
df['attendance'] = df['attendance'].fillna(df['attendance'].mean())


print("after attendance fill with 0")
print(df)

