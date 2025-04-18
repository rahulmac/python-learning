import matplotlib.pyplot as plt

names = ['Ankit', 'Bhavna', 'Chirag', 'Deepa']
salaries = [60000, 75000, 80000, 72000]

plt.bar(names, salaries, color='skyblue')
plt.title("Salary Comparison")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.show()
