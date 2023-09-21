from random import *
c_num=randrange(1,101)
score=10
attempt=10
while 1:
    u_num=int(input("guess the number"))
    if u_num==c_num:
        print("you win with score",score)
        break
    elif u_num > c_num:
        print("too big")
        score=score-1
        if score<=0:
            print(0)
        attempt-=1
        print("attempt left",attempt)
        if attempt<=0:
           print("no attempts left")   
    else :
        print("too small")
        score=score-1
        if score<=0:
            print(0)
        attempt-=1
        print("attemp left",attempt)
        if attempt<=0:
           print("no attempts left")
           break

       
    
