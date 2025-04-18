import matplotlib.pyplot as plt

ages = [34, 28, 45, 30, 25, 22]

plt.hist(ages, bins=5, color='orange', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
