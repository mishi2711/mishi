#butterfly pattern
rows=10
for i in range(1,rows+1):
    print("*"*(i)+" "*(rows-i)+" "*(rows-i)+"*"*(i))
for i in range(1,rows+1):
    print("*"*(rows-i)+" "*(i)+" "*(i)+"*"*(rows-i))
print()          
