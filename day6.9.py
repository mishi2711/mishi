#while loop ke andr likho tb chalega bahar mt likh dena
passcode=(input("enter the passcode"))
while True:
    if len(passcode)<=6:
        print("passcode must be 6 character long ,please enter again")
        pass
    else:
        print("passcode set successfully") 
    break
    