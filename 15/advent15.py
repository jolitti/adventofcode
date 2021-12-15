from queue import PriorityQueue
dirs = [(1,0),(0,1),(-1,0),(0,-1)]
dirs = [(1,0),(0,1)]

def wrap(x:int) -> int:
    if x<=9: return x
    while x>9:
        x -= 9
    return x

def distance(t:tuple[int,int],l:int) -> int:
    d1 = abs(t[0]-l+1)
    d2 = abs(t[1]-l+1)
    return d1 + d2  #prev: d1 * d2

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


def checkBounds(t:tuple[int],l:int) -> bool:
    for x in t:
        if not 0<=x<l: return False
    return True

def tupleSum(a,b) -> tuple[int]:
    from operator import add
    return tuple(map(add,a,b))

def getMinCost(points:list[list[int]],costs:list[list[int]]) -> int:
    side = len(points)
    q = PriorityQueue()
    q.put((distance((0,0),side),0,(0,0)))

    while costs[side-1][side-1]<0:
        _, cost, pos = q.get()
        print(f"{pos}: {cost}")
        x,y = pos
        costs[y][x] = cost
        for d in dirs:
            npos = tupleSum(pos,d)
            ndist = distance(npos,side)
            if not checkBounds(npos,side): continue
            nx,ny = npos
            if costs[ny][nx] >-1: continue
            ncost = cost + points[ny][nx]
            q.put((ncost+ndist,ncost,(nx,ny)))
    
    return costs[side-1][side-1]


with open("15/input00.txt") as file:
    lines = file.readlines()
lines = [x.strip() for x in lines]
data = [[int(x) for x in l] for l in lines]
data = buildActualMap(data)

#[print(*l) for l in data]

costs = [[-1 for _ in l] for l in data]
costs[0][0]=0

print(getMinCost(data,costs))
