import re

with open("05/input00.txt") as file:
    data = file.readlines()

points = []
for d in data:
    a,b,c,d = map(int,re.split(",| -> ",d))
    points.append(((a,b),(c,d)))
print(len(points))

vents = {}