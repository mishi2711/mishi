#counting the digits


num = int(input("enter the number"))
count = 0

while num != 0:
    num = num // 10
    count +=1
print("the total number of digits are", count)
    
