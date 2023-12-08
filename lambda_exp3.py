#lambda with mapping

ls=["abhiraj","zoya","manmohan","saksham"]
print("before mapping",ls)
out=list(map(lambda st :st.capitalize(),ls))
print("after mapping ",out)