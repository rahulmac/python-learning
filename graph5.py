import matplotlib.pyplot as plt

ages = [34, 28, 45, 30, 25, 22]
salaries = [60000, 75000, 80000, 72000, 50000, 66000]

plt.scatter(ages, salaries, color='green')
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True)
plt.show()
