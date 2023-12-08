'''n=int(input("enter the number "))
i=0
for num in range(n+1):
    if num%2==0 and num%3==0:
        i+=num
        print(i)
string=input("enter the string")
vowels="aeiouAEIOU"
count=0
for char in string:
    if char in vowels:
        count+=1
        print,(,count)'''
mylist=[12,20,3,2,5,8,36]
squared_list=[x**2 for x in mylist]
even_list=[x for x in squared_list if x%2==0]
print(even_list)