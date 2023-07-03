import math as m
class Module:
    def function(self):
        try:
            num1=int(input("enter value of a: "))
            num2=int(input("enter value of b: "))
            print("addition:", (num1+num2))
            print("subtraction:", (num1-num2))
            print("multiplication:", (num1*num2))
            print("division:", (num1/num2))
            print(f"Square of {num1} is {m.pow(num1, 2)}")
            print(f"Square of {num2} is {m.pow(num2, 2)}")

        except ValueError:
            print("Invalid input. Please enter integers.")
    
        except InvalidInputError as e:
            print("Invalid input:", str(e))

        finally:
            print("Final block")

f=Module()
f.function()

    


