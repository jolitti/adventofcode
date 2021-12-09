dirs:list[tuple[int,int]] = [(1,0),(0,1),(-1,0),(0,-1)]

def isLowPoint(x:int,y:int,map:list[str]) -> bool:
    refVal = int(map[y][x])
    max_y = len(map)
    max_x = len(map[0])
    for d in dirs:
        dx,dy = d
        nx,ny = x+dx,y+dy
        if not 0<=nx<max_x: continue
        elif not 0<=ny<max_y: continue
        if int(map[ny][nx])<= refVal: return False
    return True

def getBasin(x:int,y:int,map:list[str],buff:set[tuple[int,int]]=None) -> set[tuple[int,int]]:
    if buff is None: buff = set()
    if not 0<=x<len(map[0]) or not 0<=y<len(map): return buff
    pointedVal = int(map[y][x])
    if pointedVal>=9: return buff
    elif (x,y) in buff: return buff
    buff.add((x,y))
    for d in dirs:
        dx,dy = d
        buff = buff.union(getBasin(x+dx,y+dy,map,buff))
    return buff
    


with open("09/input09.txt") as file:
    map = file.readlines()
map = [x.strip() for x in map]

minPos = []
for j in range(len(map)):
    for i,c in enumerate(map[j]):
        if isLowPoint(i,j,map):
            #print(f"{i},{j}:  {c}")
            minPos.append((i,j))

#print((getBasin(1,0,map)))
#print((getBasin(9,0,map)))

basins = []
for m in minPos:
    x,y = m
    basins.append(getBasin(x,y,map))

#print(len(getBasin(2,1,map)))

basins = sorted(basins,key=len,reverse=True)
basins = basins[:3]
basins = [len(x) for x in basins]
print(*basins)
from math import prod
print(prod(basins))