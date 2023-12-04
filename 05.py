pos = int(input("enter the position"))
count = 0
for i in range (1,1001):
    if i%3!=0 and i%10!=3:
        count=count+1
        if count == pos :
            print(i)
            break