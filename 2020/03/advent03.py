# 162 3064612320

from terrain import Terrain

with open("example.txt") as file:
    sample_data = file.readlines()
    sample_data = [x.strip() for x in sample_data]
with open("input.txt") as file:
    data = file.readlines()
    data = [x.strip() for x in data]

terr = Terrain(data)

print(f"First answer: {terr.get_trees(3,1)}")

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

ans = 1
for a,b in slopes:
    ans *= terr.get_trees(a,b)

print(f"Second answer: {ans}")