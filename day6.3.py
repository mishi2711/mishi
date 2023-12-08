num1=float(input("enter the first number"))
num2=float(input("enter the second number"))
if  num2==0 and num1==0:
    print("invalid")
elif num2>0 and num1==0:
    print("invalid")
elif num1>0 and num2==0:
    print("invalid")
elif num1>num2:
    print(f"{num1}is greater then {num2}")
elif num2>num1:
    print(F"{num2}is greater then{num1}")
elif num1<0 and num2<0:
    print("invalid")
elif num1<1 and num2<1:
    print("invalid")
else:
    print("the both are equal")
krishna="    mangal    "
print(krishna.strip())