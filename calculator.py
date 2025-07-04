import os                                                     # use to clear the data
def calculator():                                             # use for start the new calculation
    num1=int(input("Enter the first number:"))
    say=True                                                  # use for repeat the program if it is yes
    while say:                                                # use for repeat the program if it is yes
        op=input("Select any operator which do you want to form(+,-,*,/):")
        num2=int(input("Enter the second number:"))
        if op=='+':
            result=num1+num2
            print(f"The result is:{num1} {op} {num2} = {result}")
        elif op=='-':
            result=num1-num2
            print(f"The result is:{num1} {op} {num2} = {result}")
        elif op=='*':
            result=num1*num2
            print(f"The result is:{num1} {op} {num2} = {result}")
        elif op=='/':
            result=num1/num2
            print(f"The result is:{num1} {op} {num2} = {result}")
        ask=input(f"Enter 'y' to continue the calculation with {result} or 'n' to start new calulation or 'x' to exit:" )
        if ask=='y':
             num1=result
        elif ask=="n": 
            say=False
            os.system('cls')                    # to remove the pervious output
            calculator()                        # recurssive -to start new calculation

        else:
             say=False                         # to end the program
             print("bye")
calculator()       


    
