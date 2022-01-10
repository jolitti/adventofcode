import re
from math import copysign

def checkOrto(t:tuple) -> bool:
    x,y = t
    a,b,c,d = x[0],x[1],y[0],y[1]
    return a==c or b==d

def getLine(t:tuple) -> list[tuple[int,int]]:
    v,w = t
    a,b,c,d = v[0],v[1],w[0],w[1]
    dx = int(copysign(1,c-a)) if c-a != 0 else 0
    dy = int(copysign(1,d-b)) if d-b != 0 else 0
    x,y = a,b
    ans = [(x,y)]
    while x!=c or y!=d:
        x+=dx
        y+=dy
        ans.append((x,y))
    return ans

def addLine(vents:dict,t:tuple):
    points = getLine(t)
    for p in points:
        val = vents.get(p,0)
        vents[p] = val+1

# print(getLine(((0,0),(5,0))))

with open("05/input05.txt") as file:
    data = file.readlines()

points = []
for d in data:
    a,b,c,d = map(int,re.split(",| -> ",d))
    points.append(((a,b),(c,d)))
#points = [x for x in points if checkOrto(x)] # Restrict to only ortogonal ones
# print(len(points))

vents = {}
for p in points:
    addLine(vents,p)

s = sum(1 for x in vents.keys() if vents[x]>=2)

print(s)
