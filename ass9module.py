import math as m
class Module:
    def function(self):
        try:
            num1=int(input("enter value of a: "))
            num2=int(input("enter value of b: "))
            op=int(input("MENU:\n 1.ADD\n2.SUBTRACT\n3.MULTIPLY\n4.DIVIDE\n5.SQUARE\n6.CUBE\n7.FACTORIAL\n8.SIN\n9.COS\n10.TAN\n Choose one operation: "))
            if op==1:
                print("addition:", (num1+num2))
            elif op==2:
                print("subtraction:", (num1-num2))
            elif op==3:
                print("multiplication:", (num1*num2))
            elif op==4:
                print("division:", (num1/num2))
            elif op==5:
                print(f"Square of {num1} is {m.pow(num1, 2)}")
                print(f"Square of {num2} is {m.pow(num2, 2)}")
            elif op==6:
                print(f"Cube of {num1} is {m.pow(num1,3)} and {num2} is {m.pow(num2,3)}")
            elif op==7:
                print(f"Factorial of {num1} is {m.factorial(num1)} & {num2} is {m.factorial(num2)}")
            elif op==8:
                print(f"Sin of {num1} is {m.sin(num1)} & {num2} is {m.sin(num2)}")
            elif op==9:
                print(f"Cos of {num1} is {m.cos(num1)} & {num2} is {m.cos(num2)}")
            elif op==10:
                print(f"Tan of {num1} is {m.tan(num1)} & {num2} is {m.tan(num2)}")

        except ValueError:
            print("Invalid input. Please enter integers.")
    
        except InvalidInputError as e:
            print("Invalid input:", str(e))

        finally:
            print("Final block")

f=Module()
f.function()

    


