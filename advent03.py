import string


with open("input03.txt") as file:
    data = file.readlines()

data = [l.strip() for l in data]

""" gamma = ""

for j in range(len(data[0])):
    sum = 0
    for i,x in enumerate(data):
        #print(f"{j},{i}")
        if x[j] == "1": sum+=1
    if sum>len(data)/2: gamma += "1"
    else: gamma += "0"

x = int(gamma,2)

epsilon = ["1" if d=="0" else "0" for d in gamma]
epsilon = "".join(epsilon)

y = int(epsilon,2)

print(x)
print(y)
print(x*y) """

