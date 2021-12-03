a = [1,2,3,4,5]

pairs = list(zip(a,a[1:],a[2:]))
print(*pairs)