#lambda with sorting

ls=["abhiraj","zoya","manmohan","saksham"]
print("before sorting:",ls)
ls.sort(key=lambda st:st[-1])
print("after sorting",ls)