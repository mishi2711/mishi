li=list(map(int,input().split()))
for i in range(0,len(li)):
    for j in range(i+1,len(li)):
        print(li[i],li[j])