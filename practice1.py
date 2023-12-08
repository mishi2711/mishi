thislist=list(("akrati","ummati","isha"))
print(thislist)
akrati=("john","simran","apple")
mylist=list(akrati)
print(mylist)
for i in range(len(mylist)):
    print(mylist[i])
mylist=[12,34,7,16,23]
sum_elements=0
for num in mylist:
    sum_elements+=num
    print(sum_elements)
max_element=mylist[0]
sec_max=mylist[1]
for num in mylist:
    if num>max_element:
        max_element=num
        if sec_max>num:
            print(sec_max)
        #print(max_element)