import random
r=random.randint(1,20)

while(True):
    inp=int(input())
    if(inp>r):
        print("too big")
    elif(inp<r):
        print("too small")
    else:
        ("right answer")
