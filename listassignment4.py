my_list=[]
num_items=int(input("enter a number"))
for i in range(num_items):
    item=input(f"enter item {i+1}:")
    my_list.append(item)
print("final list:",my_list)
'''element_to_occur=int(input("enter the number to count occurance"))
count=0
for num in my_list:
    if num == element_to_occur:
        count+=1
print(count)'''
reversed_list=[]
for i in range(len(my_list)-1,-1,-1):
    reversed_list.append(my_list[i])
print(reversed_list)
'''list2=my_list[::-1]
print(list2)'''

'''largest_element=my_list[0]
second_largest=my_list[0]
for num in (my_list):
    if largest_element>num :
        largest_element=num
    elif second_largest<largest_element and second_largest>num:
print(second_largest)'''
lowest_ele=my_list[0]
for num in my_list:
    if lowest_ele<num:
        lowest_ele=num
    print(lowest_ele)

