num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("choose the operation:+,-,*,/")
op=input("Enter the operation you want to perform: ")
if op=='+':
    print("Result:",num1+num2)
elif op=='-':
    print("Result:",num1-num2)
elif op=='*':
    print("Result:",num1*num2)
elif op=='/':
    if num2!=0:
        print("Result:",num1/num2)
    else:
        print("cannot divide by zero")
