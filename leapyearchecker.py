#leap year
for i in range(2000,3001):
    if (i%4==0 and i%100!=0) or (i%400==0):
        print(i)
    else:
        print(i," is not a leap year")
        
    
