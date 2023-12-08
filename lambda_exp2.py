#lambda with sorting 2 

ls=["abhiraj","zoya","manmohan","saksham"]
print("before sorting",ls)
ls.sort(key=lambda st:sum([ord(i) for i in st]))
print("after sorting",ls)