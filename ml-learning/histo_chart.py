#pi chart pass fail percentage
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("students_performance.csv")

# Histogram: marks distribution
plt.figure(figsize=(8, 5))

plt.hist(
    df["FinalMarks"],
    bins=5,
    color="green",
    edgecolor="black"
)

plt.title("Distribution of Final Marks")
plt.xlabel("Marks Range")
plt.ylabel("Number of Students")
plt.show()
