#pi chart pass fail percentage
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("students_performance.csv")

# Scatter plot: StudyHours vs FinalMarks
plt.figure(figsize=(8, 5))

plt.scatter(
    df["StudyHours"],
    df["FinalMarks"],
    color="purple"
)

plt.title("Study Hours vs Final Marks")
plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.grid(True)
plt.show()
