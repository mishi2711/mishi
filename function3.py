def modify_int(x):
    x+=10
    print("Inside the function:",x)
num=5
modify_int(num)
print("outside the function:",num)

def modify_string(s):
    s += " world!"
    print("inside the function:",s)
greeting = "hello"
modify_string(greeting)
print("outside the function:",greeting)

def modify_tuple(t):
    t+=(4,5)
    print("inside the function:",t)

coordinates=(1,2,3)
modify_tuple(coordinates)
print("outside the function:",coordinates)

def modify_list(lst):
    lst.append(4)
    lst[0]=99
    print("inside the function:",lst)#list is mutable so it world get
    #changed so when we are printing the list outside the function it would print the updated list

numbers=[1,2,3]
modify_list(numbers) 
print("Outside the function:",numbers)
def modify_dict(d):
    d['new_key']='new_value'
    print("inside the function",d)
my_dict={'key1':'value1','key2':'value2'}
modify_dict(my_dict)
print("outside the function:",my_dict)

def modify_set(s):
    s.add(4)
    print("inside the function:",s)
my_set={1,2,3}
modify_set(my_set)
print("outside the function",my_set)