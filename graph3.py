import matplotlib.pyplot as plt


labels = ['HR', 'IT', 'Finance', 'Lead']
sizes = [2, 2, 1, 1]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Department Distribution")
plt.axis('equal')  # Makes it a circle
plt.show()
