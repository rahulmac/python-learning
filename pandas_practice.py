import pandas as pd

data = {
    'Name': ['Ankit', 'Bhavna', 'Chirag', 'Deepa', 'Eshan', 'Riyan'],
    'Age': [34, 28, 45, 30, 25, 22],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', 'Lead'],
    'Salary': [60000, 75000, 80000, 72000, 50000, None]
}

df = pd.DataFrame(data)
#print(df[df['Department'] == 'HR'])
df['Salary'] = df['Salary'] + (df['Salary'] * 0.1)


print(df['Salary'])
print(df[df['Salary'].isnull()])
#print(df.loc[df['Salary'] > 70000, ['Name', 'Salary']])