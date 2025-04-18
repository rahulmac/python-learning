import pandas as pd



read = pd.read_excel('video.xlsx')

#print(read)
#print(read.tail())

#print(read[10:20])
print(read.shape) #number of rows and clumns
print(len(read)) # total lenght
print(read.columns) # first row as table header