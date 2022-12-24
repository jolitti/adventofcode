from aocd import numbers
from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2022,day=15)

def reduce(intervals: list[tuple[int,int]]) -> list[tuple[int,int]]:
    ans = []
    
    edges = []
    for a,b in intervals: edges += [(a,1),(b,-1)]
    ends = {}
    for point,value in edges:
        ends[point] = ends.get(point,0) + value
    ends = {p:v for p,v in ends.items() if v!=0}
    
    ends = [(p,v) for p,v in ends.items()]
    ends.sort(key=lambda x: x[0])
    state = 0
    for point, value in ends:
        if state == 0: beginning = point
        state += value
        if state == 0: ans.append((beginning,point))
    
    return ans

class Area:
    def __init__(self,pts:list[int]):
        a,b,c,d = pts
        self.center = (a,b)
        self.range = abs(a-c) + abs(b-d)
        r = self.range
        self.points = [(a-r,b),(a,b+r),(a+r,b),(a,b-r)]
    def get_range(self,ylevel:int) -> tuple[int,int]:
        x,y = self.center
        if ylevel not in range(y-self.range,y+self.range+1): return None
        diff = abs(y-ylevel)
        return (x-(self.range-diff),x+(self.range-diff))

samplenumbers = puzzle.example_data.split("\n")
samplenumbers = [list(map(int,re.findall("-?\\d+",line))) for line in samplenumbers]
sampleareas = [Area(n) for n in samplenumbers]
sampleranges = [a.get_range(10) for a in sampleareas if a.get_range(10) is not None]
sampleranges = reduce(sampleranges)
print(sampleranges)
sa,sb = sampleranges[0]
print(sb-sa+1-1)

areas = [Area(n) for n in numbers]
beacons = [(c,d) for _,_,c,d in numbers]
ranges = [a.get_range(2_000_000) for a in areas if a.get_range(2_000_000) is not None]
starts = [a for a,b in ranges]
ends = [b for a,b in ranges]
print(ranges)
smallranges = [(a//100000,b//100000) for a,b in ranges]
smallranges.sort(key=lambda x: x[0])
print(smallranges)
ranges = reduce(ranges)
a,b = ranges[0]
assert(min(starts)==a)
assert(max(ends)==b)
total = b-a+1
total-=3
print(total)
