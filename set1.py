myset=set(("apple","banana","cherry"))
'''for x in myset:
    print(x)'''
thisset={"apple","banana","cherry"}
thisset.add("orange")
thisset.update("orange")
print(thisset)
thisset={"apple","banana","cherry"}
tropical={"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)
thisset.remove("banana")
print(thisset)
thisset.discard("apple")
print(thisset)
thisset={"apple","banana","cherry"}
x=thisset.pop()
print(x)
print(thisset)
thisset={"apple","banana","cherry"}
thisset.clear()
print(thisset)
'''thisset={"apple","banana","cherry"}
del thisset
print(thisset)'''