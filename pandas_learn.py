import pandas as pd

arr = [1,2,3,4]

print(pd.Series(arr))



data = {
'Name': ['Rahul', 'Gayatri', 'Vedika'],
'Age': [33, 28 , 1],
'City' : ['Jambughoda', 'Koth', 'Ahmedabad']
}


data1 = pd.DataFrame(data)


#print(data1[data1['City'].isin(['Koth'])])

#print(data1[~(data1['City'] == 'Koth')])


##print(df[~(df['City'] == 'Delhi')])















#print(data1[data1['Age'] > 28])

#print(data1[data1['City'].isin(['Jambughoda', 'Ahmedabad'])])



