from aocd import lines
from aocd.models import Puzzle
from queue import PriorityQueue

puzzle = Puzzle(year=2022,day=12)

class Point:
    def __init__(self,pos:tuple[int,int], parent:"Point"=None, step:int = 0):
        self.pos = pos
        self.parent = parent
        self.step = step
    def __lt__(self,other):
        return self.step<other.step
    def __le__(self,other):
        return self.step<=other.step
    def surrounding(self,matrix:list[list[int]],explored:set[tuple[int,int]]) -> list["Point"]:
        ans = []
        grid_size = len(matrix[0]),len(matrix)
        x,y = self.pos
        for a,b in [(x+dx,y) for dx in [-1,1]] + [(x,y+dy) for dy in [-1,1]]:
            if a<0 or b<0: continue
            if a>=grid_size[0] or b>=grid_size[1]: continue
            #print(f"Evaluating point ({a},{b}) of height {matrix[b][a]} from point ({x},{y}) of height {matrix[y][x]}")
            if (a,b) in explored: continue
            if matrix[b][a]>matrix[y][x]+1: continue
            ans.append(Point((a,b),self,self.step+1))
            explored.add((a,b))
        return ans

def findpos(target:chr, matr:list[list[chr]]) -> list[tuple[int,int]]:
    ans = []
    for y,l in enumerate(matr):
        for x,c in enumerate(l):
            if c==target: ans.append((x,y))
    return ans

def solve(elevations:list[str],starting:tuple[int,int]=None) -> Point:
    elev = [s.strip() for s in elevations]
    startpos = starting
    if starting is None: startpos = findpos("S",elev)[0]
    targetpos = findpos("E",elev)[0]
    elev = [d.replace("S","a") for d in elev]
    elev = [d.replace("E","z") for d in elev]
    data = [[c for c in l] for l in elev]
    data = [[ord(c.lower()) - ord("a") for c in l] for l in data]
    visited = set()
    queue = PriorityQueue()
    
    startpoint = Point(startpos)
    queue.put(startpoint)
    while True:
        #print(len(queue.queue))
        #for p in queue.queue: print(p.pos,end=" ")
        #print()
        point = queue.get()
        if point.pos == targetpos: return point
        for newpoint in point.surrounding(data,visited):
            queue.put(newpoint)
        if len(queue.queue)<=0: return None

with open("samples/sample12") as file:
    samplemap = file.readlines()

assert(solve(samplemap).step == 31)

ans1 = solve(lines).step
print(f"First answer: {ans1}")
puzzle.answer_a = ans1

positions = findpos("a",lines) + findpos("S",lines)
# print(len(positions))
paths = [solve(lines,p) for p in positions]
paths = [p.step for p in paths if p is not None]

ans2 = min(paths)
print(f"Second answer: {ans2}")
puzzle.answer_b = ans2
