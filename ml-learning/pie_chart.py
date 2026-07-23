#pi chart pass fail percentage
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("students_performance.csv")

result_count = df["Result"].value_counts()
plt.figure(figsize=(6, 6))

plt.pie(result_count, labels=result_count.index, autopct='%5.2f%%', startangle=90, colors=['green', 'red'])
plt.title("Pass/Fail Percentage")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
