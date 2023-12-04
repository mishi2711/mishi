num1=int(input("enter a initiating number"))
num2=int(input("enter the ending number"))
for i in range(num1,num2+1):
    if i>1:
        for num in range(2,i):
            if (i%num)==0:
                break
            else:
                print(i)