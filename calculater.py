def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
n1=int(input("Enter 1st no.:"))
n2=int(input("Enter 2nd no.:"))
print("select operation:\n 1.Addition\n 2.Substraction\n 3.Multiplication\n 4,Division")

while True:
    choice=int(input("Enter choice 1/2/3/4:"))
    if choice==1:
        print(addition(n1,n2))
    elif choice==2:
        print(subtraction(n1,n2))
    elif choice==3:
        print(multiplication(n1,n2))
    elif choice==4:
        print(division(n1,n2))
    else:
        print("Invalid input")
    break
