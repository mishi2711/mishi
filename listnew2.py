'''num1=int(input("enter start number"))
num2=int(input("enter the ending number"))
for num in range(num1,num2+1):
    if num%5==0:
        print(num+2 )'''
'''number=int(input("enter the number"))
temp=str(number)
sum=0
if len(temp)>1:
    for num in temp:
        sum+=int(num)
    print(sum)'''
num=int(input("enter a number(except one-digit):"))
digits=[int(digit) for digit in str(num)]
sum_of_digits=0
for digit in digits:
    sum_of_digits+=digit
print(f"The sum of the digits{num} is {sum_of_digits}")