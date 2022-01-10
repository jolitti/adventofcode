from functools import cache
import sys
sys.setrecursionlimit(100000)

dirs = [(-1,0),(0,-1),(1,0),(0,1)]

@cache
def checkBounds(t:tuple[int],l:int) -> bool:
    for x in t:
        if not 0<=x<l: return False
    return True
@cache
def tupleSum(a,b) -> tuple[int]:
    from operator import add
    return tuple(map(add,a,b))
@cache
def wrap(x:int) -> int:
    if x<=9: return x
    while x>9:
        x -= 9
    return x

def buildActualMap(points:list[list[int]]) -> list[list[int]]:
    side = len(points)
    newPoints = [[0 for _ in range(side*5)] for _ in range(side*5)]
    for j in range(5):
        for i in range(5):
            dist = j+i
            #print(f"{i} {j} {dist}")
            for y in range(side):
                for x in range(side):
                    newPoints[y+side*j][x+side*i] = wrap(points[y][x]+dist)
    return newPoints

@cache
def findMinCostTo(p:tuple[int,int]) -> int:
    if p == (0,0): return 0
    costs = []
    for x in dirs:
        np = tupleSum(x,p)
        if checkBounds(np,side): 
            x,y = np
            costs.append(findMinCostTo((x,y)))
    if costs == []: costs = [0]
    x,y = p
    #print(f"{p}: {min(costs)}")
    return min(costs)+points[y][x]
    
with open("input15.txt") as file:
    lines = file.readlines()
lines = [x.strip() for x in lines]
data = [[int(x) for x in l] for l in lines]
points = data
points = buildActualMap(data)

[print("".join(map(str,l))) for l in points]

side = len(points)

#print(findMinCostTo((side-1,side-1)))