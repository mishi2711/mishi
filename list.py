myData=["akrati" , 1,"krishna", "python"]
print(myData)
print(len(myData))
print(type(myData))
print(myData[:2])
print(myData[::2])
myData.append("sneha")
print(myData)
if "akrati" in myData:
    print("yes!")
thislist = list(("qwerty","asdfg",456))
print(thislist)
myData[1]="Black tea"
print(myData)
'''myData[1:3]=["Black tea","cold coffee"]
print(myData)
myData[1:2]=["sugar","tea"]
print(myData)
print(len(myData))
myData.insert(3,"soft drink")
print(myData)
myData[1:5]=["expresso","mojito"]
print(myData)
myData2=["a","b","c"]
myData.extend(myData2)
print(myData)
print(len(myData))
list1=["a","b","c"]
list2=[1,2,3]
#list3=list1+list2
#print(list3)

#for x in list2:
  #  list1.append(x)
#print(list1)

i=0
for x in list2:
    list1.insert(i,x)
    i+=1
print(list1)

newList=["apple","banana","cherry"]
finallist=newList.copy()
print(finallist)

newList=["apple","banana","cherry"]
finalList=list(newList)
print(finalList)
myList=["a","b","c"]
myList.remove("b")
print(myList)
myList=["a","b","c"]
myList.pop("b")
print(myList)
myList=["a","b","c"]
myList.pop()
print(myList)
myList=["a","b","c"]
del myList[0]
print(myList)
myList=["a","b","c"]
myList.clear()
print(myList)'''
r2 = "Python is powerful"

result = ""

for word in str2.split():

if len(word) % 2 == 0:

result += word.upper() + " "

else:

result += word.lower() + " "

print(result.strip())

What will be the output of this code?

