number= int(input("enter a number"))
num_digits=len(str(number))
sum_of_cubes=0
temp=number

while temp>0:
    digit=temp%10
    sum_of_cubes+=digit**num_digits
    temp//=10
if number==sum_of_cubes:
    print(f"{number}is an armstrong number")
else:
    print("not an armstrong number")
