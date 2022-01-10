from heapq import *

dirs = [(1,0),(0,1),(-1,0),(0,-1)]

def v2add(x,y):
    a,b = x
    c,d = y
    return (a+c,b+d)

def getDistances(points:list[list[int]]) -> list[list[int]]:
    side = len(points)
    sol = [[-1 for _ in range(side)] for _ in range(side)]
    visited = set()

    q = []
    heappush(q,(0,(0,0)))

    while len(q)>0:
        weight, pos = heappop(q)
        x,y = pos
        sol[y][x] = weight
        visited.add(pos)
        for d in dirs:
            newPos = v2add(d,pos)
            if newPos in visited: continue
            nx,ny = newPos
            if not(0<=nx<side) or not (0<=ny<side): continue
            heappush(q,(weight+points[ny][nx],(newPos)))
            visited.add(newPos)
    return sol

with open("15/i15.txt") as file:
    lines = file.readlines()
lines = [x.strip() for x in lines]
data = [[int(x) for x in l] for l in lines]

print(getDistances(data)[len(data)-1][len(data)-1])