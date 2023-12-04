st1="hello welcome to gla university"
print("string",st1)
#slice first 10 characters
print(st1[slice(10)])
#slice from last 4th position to 10th position
print(st1[slice(-10,-3)])
#slice the first character to 5th character
print(st1[slice(0,5)])
#slice from first character to 5th character by skipping 3 characters
print(st1[slice(0,8,3)])
#return the entire string using array slicing
print(st1[:])
#slice from 7th character to 20th character
print(st1[6:20])

input_str="hello"
reversed_str=input_str[::-1]
#[::-1]: This is the slice notation.it specifies how you want to extract a portion of the string
#the first colon:indicates the start of the slice
#the secondd colon:is the end of the slice.Since we dont specify a value offer
#the second colon,it means we want to include all characters up to the end.
#the -1 is the step size.It indicates that we want to iterate over the string in reverse order







input_str="hello"
char="1"
#count=input_str,
x=count(char)
print(x)
#output=2