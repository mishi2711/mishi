#lambda with filter

ls=[4,6,7,8]
print("after mapping ",ls)
out=list(filter(lambda x :x<=5,ls))
print("after mapping", out)
