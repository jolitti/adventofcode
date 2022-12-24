import matplotlib.pyplot as plt
from aocd import lines, numbers
from aocd.models import Puzzle
import re
import sys

puzzle = Puzzle(year=2022,day=15)

def mandist(a:tuple[int,int],b:tuple[int,int]) -> int:
    x,y = a
    xx,yy = b
    return abs(x-xx) + abs(y-yy)

def getsensors(nums:list[list[int]]) -> list[tuple[tuple[int,int],int]]:
    return [((a,b),mandist((a,b),(c,d))) for a,b,c,d in nums]

def can_be_beacon(p:tuple[int,int],sensors:list[tuple[int,int]],beacons:set[tuple[int,int]]=None) -> bool:
    if p in beacons: return False
    for s in sensors:
        sp, d = s
        if mandist(p,sp)<=d: return True
    return False

sampledata = puzzle.example_data.split("\n")
sampledata = [list(map(int,re.findall("[+-]?[0-9]+",line))) for line in sampledata]
samplebeacons = set((c,d) for _,_,c,d in sampledata)
samplesensors = getsensors(sampledata)

sans = ""
counter = 0
for x in range(-5,28):
    sans += "#" if can_be_beacon((x,10),samplesensors,samplebeacons) else " "
    if can_be_beacon((x,10),samplesensors,samplebeacons): counter+=1
assert(counter==26)

beacons = set((c,d) for _,_,c,d in numbers)
sensors = getsensors(numbers)
plt.plot(list(beacons))
plt.show()
sys.exit()

maxrange = max(r for _,r in sensors)
minx = min(x for (x,_),_ in sensors) - maxrange
minx -= 10000000
maxx = max(x for (x,_),_ in sensors) + maxrange
maxx += 10000000
ans1 = 0
foundmin = False
mintrue = maxx
maxtrue = minx
for x in range(minx,maxx+1):
    if not can_be_beacon((x,2_000_000),sensors,beacons):
        if not foundmin:
            print("Found a new minimum!")
            mintrue = x
            foundmin = True
        maxtrue = x
        ans1+=1
print(f"Min x found: {mintrue}, max x found: {maxtrue}")
print(f"Original minx: {minx}, maxx: {maxx}")
print(ans1)
