with open("input01.txt") as file:
    data = file.readlines()

data = list(map(int,data))
throuples = list(zip(data,data[1:],data[2:]))
tuplesum = list(map(sum,throuples))

sum = 0
for i,t in enumerate(tuplesum[:-1]):
    if t<tuplesum[i+1]: sum+=1

print(sum)