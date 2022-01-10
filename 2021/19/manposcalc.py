from myutils import getAdventData
from vector3 import Vector3, manDistance

data = getAdventData("19","scannerpos.txt")
pos = []
for d in data:
    a,b,c = map(int,map(float,d.split()))
    pos.append(Vector3(a,b,c))

dists = [manDistance(x,y) for x in pos for y in pos if x is not y]
print(*dists)
print(max(dists))