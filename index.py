import sys
import custom_module


help('modules')

x = int(sys.argv[1])
y = int(sys.argv[2])

print(custom_module.add(x,y))
print(custom_module.greet(sys.argv[3]))

#print(type(x))
#print(type(x))

#a = sys.argv[1]

#print(len(a))
#print(a.lower())
#print(a.upper())
#print(a.replace("hul", "Hope"))

#print(sys.argv[1])

""" age = int(sys.argv[1])

if age >= 18 and age < 60:
    print("you can vote")
elif age < 18 : 
    print("you can not vote")
else : 
    print("you are senior citizen")    
    
for i in range(age):
    print(i)

count = 0
while count < age:
    print(count)
    count +=1 """
    