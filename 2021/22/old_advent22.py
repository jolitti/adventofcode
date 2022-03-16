from myutils import getAdventData
from old_cuboid import *
import re

LIMIT = 100000

data = getAdventData("2021/22","input22.txt")

data = [re.split(" |,",d) for d in data]
for d in data:
    d[0] = True if d[0]=="on" else False
    for i in [1,2,3]:
        d[i] = d[i][2:]

reactor = dict()
for x in range(-LIMIT,LIMIT+1):
    print(x)
    for y in range(-LIMIT,LIMIT+1):
        for z in range(-LIMIT,LIMIT+1):
            reactor[(x,y,z)] = False

i = 0
for d in data:
    i+=1
    print(i)
    newState = d[0]
    cub = getCuboid(d[1:])
    cub = trimCuboid(cub,LIMIT)
    if cub is not None:
        for p in cuboidToPoints(cub):
            reactor[p] = newState

tot = 0
for p in reactor.keys():
    if reactor[p]: tot += 1

print(tot)