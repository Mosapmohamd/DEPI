from main import Calculator

def main():
    global Calculator
    Calculator = Calculator()
    while True:
        Oper=input("Enter the Operator (add,sub,milt,div) or stop to exit: ")
        if Oper=="stop":
            break
        elif Oper=="add" or Oper=="sub" or Oper=="milt" or Oper=="div":
            try:
                num1=float(input("Enter the first number: "))
                num2=float(input("Enter the second number: "))

                if Oper=="add":
                    result=Calculator.add(num1,num2)
                elif Oper=="sub":
                    result=Calculator.sub(num1,num2)
                elif Oper=="milt":
                    result=Calculator.mult(num1,num2)
                elif Oper=="div":
                    result=Calculator.div(num1,num2)
                print("Result: ",result)

            except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            print("Invalid operator. Please enter a valid operator.")

if __name__=="__main__":
    main()
