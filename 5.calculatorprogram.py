def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print("select operation")
print("1.Add ")
print("2.Subtract ")
print("3.Multiply ")
print("4.Divide ")

while True:
    operation=input("enter the operation(1/2/3/4):")
    if operation in ('1','2','3','4'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("enter the second number: "))
        if operation == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        if operation == '2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        if operation == '3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        if operation == '4':
            print(num1,"/",num2,"=",divide(num1,num2))
        

         