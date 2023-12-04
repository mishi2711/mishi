#sum of all the given number


n=int(input("enter the number"))
s=0
current_number= 1

while (current_number<=n):
    s +=current_number
    current_number +=1
print("the sum of all numbers from 1 to ",n ,"is" , s)
    
