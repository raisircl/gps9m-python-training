import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students_performance.csv")
print(df.head())

plt.figure(figsize=(8, 5))

plt.plot(df["StudentName"], df["FinalMarks"], label="Marks")
plt.plot(df["StudentName"], df["Attendance"], label="Attendance")

plt.title("Marks and Attendance")
plt.xlabel("Student")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.savefig("student_marks_chart.png", dpi=300)

plt.show()
