#unordered,unchanged,unindexed
#sets are used to store multiple values in a single variable
#they are unchangeble but you can remove items and add new items
#it automatically removes duplicate items
thisset={"apple","banana","cherry"}
print(thisset)
thisset1={"apple","banana","cherry","apple"}
print(thisset1)
myset=set(("apple","banana","cherry"))# note the double round bracket
print(myset)
print(len(thisset))
print(type(thisset))
print(type(thisset1))
print(len(thisset1))
