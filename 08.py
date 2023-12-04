li=list(map(int, input().split()))
t=int(input("enter"))

for i in range (0,len(li)):
    for j in range(i+1,len(li)):
        if (li[i]+li[j]==t):
            print(li[i],li[j])
        