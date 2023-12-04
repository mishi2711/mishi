n=int(input("enter the number"))
count=0
for i in range(2,n):
    if (n%i)==0:
        for j in range(1,i):
            if i%j==0:
                count+=1
                print(i)
        if count>=2:
            if i>n**(1/2):
                print(i,"strange")
                break
    else:
        print("not strange")
                
        
