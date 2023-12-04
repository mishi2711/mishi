start=int(input("enter the starting number"))
stop=int(input("enter the endi
               ng number"))
num1=0
num2=1
num3=0
print(num1)
for num in range(start,stop+1):
    num1=num2
    num2=num3
    num3=num1+num2
    print(num3,"")
#limit = 1000
#fibonacci_sequence = [0,1]
#while True:
#   next_number=fibonacci_sequence[-1] + fibonacci[-2]
#if next_number>limit:
#fibonacci_sequence is [next_number] #combine lists using'+='
#print("fibonacci sequence:")
#print(fibonacci_sequence)
#[-1] is the index it is used to define that the previous term is being mentioned or reffered here.