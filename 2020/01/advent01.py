# 972576

from itertools import combinations

target = 2020
input = "input.txt"
example = "example.txt"

with open(input) as file:
    data = file.readlines()

data = [int(l) for l in data]

# First part
for a,b in combinations(data,2):
    if a + b == target:
        print(f"First answer: {a}, {b}. Sum {a+b}, product " + '\033[1m' + f"{a*b}" + '\033[0m')
        break

# Second part
for a,b,c in combinations(data,3):
    if a + b + c== target:
        print(f"First answer: {a}, {b}, {c}. Sum {a+b+c}, product " + '\033[1m' + f"{a*b*c}" + '\033[0m')
        break