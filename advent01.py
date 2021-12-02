with open("input01.txt") as file:
    data = file.readlines()

data = list(map(int,data))

sum = 0

for i, x in enumerate(data):
    if x>data[i-1]>data[i-2]: 
        sum+=1
        print(f"{x}>{data[i-1]}")
    #print(x)

print(sum)