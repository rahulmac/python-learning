import sys

try:

    with open("ff.txt") as file:
        content = file.read()
        print(content)
        file.close()
    
    
    with open("a.txt", "w") as file:
        file.write("now ? \n")
        file.close()
    
    with open("b.txt", "a") as file:
        file.write("data appended ? \n")
        file.close()
    
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(e)