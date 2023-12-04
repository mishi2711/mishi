mylist=[]
print("====Enhanced Simple Calculation====")
print( "1.Addition")
print( "2.Subtraction")
print( "3.Multiplication")
print( "4.Division")
print( "5.Display operation")
print( "6.Quit")
operation=input("enter the operation to be performed")

for num in range(int(operation)):
    print("====Enhanced Simple Calculation====")
    print( "1.Addition")
    print( "2.Subtraction")
    print( "3.Multiplication")
    print( "4.Division")
    print( "5.Display operation")
    print( "6.Quit")
    
    if num==0:
        num1=float(input("enter the first number"))
        num2=float(input("enter the second number"))
        result=num1+num2
        print(f"{num1} + {num2}= {result}")
        mylist.append(num1+num2)
        print(mylist)
    elif num==1:
        num1=float(input("enter the first number"))
        num2=float(input("enter the second number"))
        result=num1-num2
        print(f"{num1}-{num2}={result}")
        mylist.append(num1-num2)
        print(mylist)
    elif num==2:
        num1=float(input("enter the first number"))
        num2=float(input("enter the second number"))
        result=num1*num2
        print(f"{num1}*{num2}= {result}")
        mylist.append(num1*num2)
        print(mylist)
    elif num==3:
        num1=float(input("enter the first number"))
        num2=float(input("enter the second number"))
        result=num1/num2
        print(f"{num1}/{num2}={result}")
        mylist.append(num1/num2)
        print(mylist)
    elif num==4:
        print("+/*/-/%")
        mylist.append("+/*/-/%")
    elif num==5:
        break
    else:
        print("invalid operation")


