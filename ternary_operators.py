x=5
y=10
result=x if x>y else y
print(result)
is_raining=True
activity='stay indoors' if is_raining else 'Go for a walk'
print(activity)
numbers=[1,2,3,4,5]
result=[x*2 if x%2==0 else x**2 for x in numbers]
print(result)
temperature=25
status='Warm' if temperature>20 else'Cold'
print(status)
#eval function can be used to calculate calues instead of using float or int datatypes.
numbers=[1,2,3,4,5]
squared_numbers=[]
for num in numbers:
    squared_numbers.append(num**2 if num %2==0 else num)
print(squared_numbers)
count=0
while count<5:
    message="Count is less than 5" if count<5 else"Count is 5 or more"
    print(message)
    count+=1
x=5
result="x is less than 5" if x<5 else "x is eqaul to 5" if x==5 else "x is less than" 
print(result)
user_input=input("Enter numbers separated by spaces:")
numbers=list(map(int, user_input.split()))
squared_numbers=list(map(lambda x:x**2,numbers))
print("original numbers:",numbers)
print("squared Numbers:",squared_numbers)
even_odd_checker=list(map(lambda x:"Even" if x%2==0 else "odd",numbers))
print("Results:",even_odd_checker)