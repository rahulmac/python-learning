import sys
import custom_module

try:
    number1 = int(sys.argv[1])
    number2 = int(sys.argv[2])

    print(custom_module.divide(number1 , number2))
    
except ZeroDivisionError:
    print("Error : You can not divide by Zero")
except ValueError:
    print("Error : Invalid parameters error")
except Exception as e:
    print(e)

finally:
    print("Function at least executed")
