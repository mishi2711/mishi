l=[5,10,20,30,40,50,60,70]
t=int(input("enter" ))
i=0
j=len(l)-1
while(i<j):
    if (l[i]+l[j]==t):
        print(l[i],l[j])
        i+=1
        j+=1
    elif(l[i]+l[j]>t):
        j=j-1
    else :
        i+=i