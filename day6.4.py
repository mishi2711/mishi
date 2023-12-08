num1=float(input("enter the first value"))
num2=float(input("enter the second value"))
if num1>=1 and num2>=1:
    if num1>num2:
        print(f"{num1} is grater then {num2}")
    elif num2>num1:
        print(f"{num2} is greater then {num1}")
    elif num2==num1:
        print(f"{num1} is equal to{num2}")
else:
    print("invalid")