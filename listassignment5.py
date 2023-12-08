list1=[23,13,14,14,65,24,65,68]
list2=[]
for i  in list1:
    if i not in list2:
        list2.append(i)
print(list2)
