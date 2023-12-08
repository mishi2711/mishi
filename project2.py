list1=[]
list2=[]
list3=[]
list4=[]
add=0
new=[]

while True:
    print("1. Add Product")
    print("2. Display Product Catalog")
    print("3. Update Product Quantity")
    print("4. Search Product by ID")
    print("5. Calculate Total Cost")
    print("6. Remove Product by ID")
    print("7. Exit")
    user_input=int(input("Enter your choice"))
    if user_input==1:
        product_id=input("Enter Product ID")
        product_name=input("Enter Product Name")
        quantity=input("Enter Product Quantity")
        price=input("enter the price")
        list1.append(product_id)
        list2.append(product_name)
        list3.append(quantity)
        list4.append(price)
    elif user_input==2:
        for i in range(len(list1)):
            print("Product catalog:")
            print("product id: ",product_id[i])
            print("product name: ",product_name[i])
            print("Quantity:",quantity[i])
            print("price:", price[i])
    elif user_input==3:
        new_quantity=quantity
        new.append(new_quantity)
        print(new_quantity)
    elif user_input==5:
        for k in list4:
            x=k*list3[k]
            add+=x
            print(add)
    elif user_input==6:
        removed=int(input("enter product id to be removed"))
        for i in range(len(list2)):
            if removed==list1[i]:
                del list2[i]
                print(list2)
    elif user_input==7:
        break
    else:
        print("invalid input")