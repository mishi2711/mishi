print("Hello,Welcome to our canteen!")

x=input("What do you prefer?(veg/nonveg)").lower()
y=int(input("how much time do you have?(in minutes):"))
z=int(input("how muct would you like to spend?(in rupee)"))
if x=="veg" and y>=30 and z>=200:
    print("Here is what we have to offer:extra cheese pizza:200/-")
    print("maharaja burger:250/-")
    print("white sauce pasta:240/-")
elif x=="veg" and y<=10 and z>=200:
    print("you may like:")
    print("french fries:280/-")
    print("honey chillie potato:210/;")
    print("red sauce pasta:250/-")
elif x=="nonveg" and y>=20 and z>=100:
    print("Here is something you  may like:")
    print("chicken briyani:300/-")
    print("crabs:250/-")
    print("fishes:200/-")
elif x=="veg" and y<=5 and z<=50:
    print("you may have:")
    print("cheese maggi:50/-")
    print("vadapav:40/-")
    print("plain maggi:30/-")
elif x=="veg" or y>=30 and z>=300:
    print("you may have our special offer")
    print("combo pack offer(peri peri fries,colddrink,burger):500/-")
    print("combo offer of (cheese pizza,peri peri fries,burger):600/-")

