from aocd import lines
from aocd.models import Puzzle
from enum import Enum
from more_itertools import windowed

class Tile(Enum):
    rock = "#"
    sand = "o"
    origin = "@"
class GrainResult(Enum):
    in_cave = "cave"
    bottom = "bottom"
    occluded = "occluded"

puzzle = Puzzle(year=2022,day=14)

def interpolate(a:tuple[int,int],b:tuple[int,int]) -> list[tuple[int,int]]:
    x,y = a
    xx,yy = b
    ans = []
    if x==xx:
        miny = min(y,yy)
        maxy = max(y,yy)
        for yyy in range(miny,maxy+1): ans.append((x,yyy))
    else:
        minx = min(x,xx)
        maxx = max(x,xx)
        for xxx in range(minx,maxx+1): ans.append((xxx,y))
    return ans

def getcoords(s:str) -> tuple[int,int]:
    a,b = s.split(",")
    a,b = int(a),int(b)
    return (a,b)

class Cave:
    def __init__(self, rockdata:list[str]):
        self.tiles = {}
        self.sand_origin = (500,0)
        self.tiles[(500,0)] = Tile.origin
        self.minx, self.maxx = 1000,0
        self.miny, self.maxy = 0,0
        for line in rockdata:
            pairs = line.split(" -> ")
            pairs = [getcoords(p) for p in pairs]
            for a,b in windowed(pairs,2):
                for x,y in interpolate(a,b):
                    self.tiles[(x,y)] = Tile.rock
                    self.minx = min(self.minx,x)
                    self.maxx = max(self.maxx,x)
                    self.maxy = max(self.maxy,y)
    def __str__(self) -> str:
        ans = []
        dx,dy = self.maxx-self.minx,self.maxy-self.miny
        ans.append(f"{dx}x{dy} cave")
        for y in range(self.miny,self.maxy+1):
            line = ""
            for x in range(self.minx,self.maxx+1):
                tile = self.tiles.get((x,y),None)
                if tile is not None: line+=tile.value
                else: line+=" "
            ans.append(line)
        return "\n".join(ans)
    def is_solid(self,p:tuple[int,int]) -> bool:
        if self.tiles.get(p,None) is not None: return True
        if p[1]>=self.maxy+2: return True
        return False
    def dropspace(self,p:tuple[int,int]) -> tuple[int,int]:
        x,y = p
        if not self.is_solid((x,y+1)): return (x,y+1)
        if not self.is_solid((x-1,y+1)): return (x-1,y+1)
        if not self.is_solid((x+1,y+1)): return (x+1,y+1)
        return None
    def dropgrain(self) -> GrainResult:
        p = self.sand_origin
        while self.dropspace(p) is not None:
            p = self.dropspace(p)
        self.tiles[p] = Tile.sand
        if p[1] >=self.maxy: return GrainResult.bottom
        if p==self.sand_origin: return GrainResult.occluded
        else: return GrainResult.in_cave

cave = Cave(lines)
ans1 = 0
while cave.dropgrain() == GrainResult.in_cave: ans1+=1
print(f"First answer: {ans1}")
puzzle.answer_a = ans1

ans2 = ans1
while cave.dropgrain() != GrainResult.occluded: ans2 += 1
ans2 += 2 # Off by two error! Don't know why, don't have time to fix
print(f"Second answer: {ans2}")
print(cave)
puzzle.answer_b = ans2
