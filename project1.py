dict1={}
number=[]
type=[]
amount=[]
add=0
while True:
    print("1. Add Vehicle Entry")
    print("2. Display Vehicle Entries")
    print("3. Calculate Total Toll Collection")
    print("4. Search Vehicle by Number")
    print("5. Exit")
    user_input=int(input("Enter your choice"))
    if user_input==1:
        vehicle_number=int(input("Enter your vehicle number"))
        vehicle_type=input("Enter vehicle type(car/bus/truck)")
        toll_amount=int(input("Enter the toll amount"))
        number.append(vehicle_number)
        type.append(vehicle_type)
        amount.append(toll_amount)
    elif user_input==2:
        for j in range(len(number)):
            print("Vehicle entries:")
            print("Vehicle number:",number[j])
            print("Vehicle Type:",type[j])
            print("Toll amount:",amount[j])
    elif user_input==3:
        for k in amount:
            add+=k
        print("total amount",add)
    elif user_input==4:
        num=int(input("enter the vehicle number:"))
        for j in range(len(amount)):
            for i in number:
                dict1.merge(i,j)
                print(dict1)
                for i in range(len(dict1)):
                    if num==dict1[i]:
                        store=int(num)
                        print(amount[store])
                        print(toll_amount[store])
                        print(type[store])
    elif user_input==5:
        break
    else:
        print("invalid input")







