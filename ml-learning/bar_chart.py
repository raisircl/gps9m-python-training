import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students_performance.csv")
print(df.head())

plt.figure(figsize=(10, 6))

plt.bar(df["StudentName"],df["FinalMarks"], color=['green','blue','orange','red','purple'])
plt.title("Students Final Marks")
plt.xlabel("Student")
plt.ylabel("Marks", fontsize=12, color='blue', fontweight='bold')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()