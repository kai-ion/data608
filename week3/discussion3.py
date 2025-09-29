import matplotlib.pyplot as plt
# Create two charts: one that violates principles, one that complies.

# Bad chart: Pie chart with too many slices and 3D effect (violates clarity and data-ink ratio)
bad_chart_path = "week3/bad_chart.png"
plt.figure(figsize=(6, 6))
sizes = [15, 30, 10, 20, 25]
labels = ["A", "B", "C", "D", "E"]
explode = (0.1, 0.1, 0.1, 0.1, 0.1)  # overemphasis
plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, shadow=True, startangle=140)
plt.title("Bad Example: Overcomplicated Pie Chart")
plt.savefig(bad_chart_path)
plt.close()

# Good chart: Simple bar chart with clear labeling (complies with Tufte/Cavalier principles)
good_chart_path = "week3/good_chart.png"
plt.figure(figsize=(6, 4))
plt.bar(labels, sizes, color="skyblue")
plt.title("Good Example: Clear Bar Chart")
plt.xlabel("Category")
plt.ylabel("Value")
plt.tight_layout()
plt.savefig(good_chart_path)
plt.close()

bad_chart_path, good_chart_path
