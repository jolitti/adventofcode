from aocd.models import Puzzle
from more_itertools import windowed

puzzle = Puzzle(year=2023,day=5)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS

#--- FUNCTIONS
def get_mapper(lines) -> dict:
    ans = {}
    for l in lines:
        dest,source,count = map(int,l.split())
        ans[range(source,source+count)] = dest
    return ans

def map_value(val,mapper) -> int:
    for value_range,dest in mapper.items():
        if val in value_range:
            return dest + (val - value_range.start)
    return val

def get_location(seed,mappers) -> int:
    ans = seed
    #print(ans)
    for m in mappers:
        ans = map_value(ans,m)
        #print(ans)
    #print("===")
    return ans

def range_intersect(r1,r2) -> range | None:
    a1,b1 = r1.start,r1.stop
    a2,b2 = r2.start,r2.stop
    if b1 <= a2 or b2 <= a1: return None
    return range(max(a1,a2),min(b1,b2))

assert range_intersect(range(1,10),range(5,9)) == range(5,9)
assert range_intersect(range(-10,-1),range(5,9)) == None

def rangediff(r1,r2) -> set[range]:
    overlap = range_intersect(r1,r2)
    if overlap == None: return {r1}
    if overlap == r1: return set()
    left = range(r1.start,r2.start)
    right = range(r2.stop,r1.stop)
    return {ll for ll in (left,right) if len(ll)>0}

assert rangediff(range(1,10),range(20,30)) == {range(1,10)}
assert rangediff(range(1,30),range(10,20)) == {range(1,10),range(20,30)}

def intersects(r,mapper) -> bool:
    for rr,dest in mapper.items():
        if range_intersect(r,rr) is not None: return (range_intersect(r,rr),(rr,dest))
    return False

def maptotal(ranges,mapper) -> set[range]:
    min_map = min(k.start for k,v in mapper.items())
    max_map = max(k.stop for k,v in mapper.items())

    ans = set()

    while len(ranges)>0:
        r = ranges.pop()
        if not intersects(r,mapper):
            ans.add(r)
            continue
        intersection,(rr,dest) = intersects(r,mapper)
        shift = intersection.start - rr.start
        remainders = rangediff(r,intersection)
        ranges |= remainders
        ans.add(range(dest+shift,dest+shift+len(intersection)))

    return ans
        
#--- PARTS

def part1(data) -> int:
    seeds = data[0]
    seeds = [int(s) for s in seeds.removeprefix("seeds: ").split()]
    chunks = []
    acc = []
    for line in data[2:]+[""]:
        if line=="":
            chunks.append(acc[1:])
            acc = []
        else:
            acc.append(line)
    mappers = [get_mapper(chunk) for chunk in chunks]

    dests = [get_location(seed,mappers) for seed in seeds]
    #print(dests)
    return min(dests)

def part2(data) -> int:
    seeds = data[0]
    seeds = [int(s) for s in seeds.removeprefix("seeds: ").split()]
    chunks = []
    acc = []
    for line in data[2:]+[""]:
        if line=="":
            chunks.append(acc[1:])
            acc = []
        else:
            acc.append(line)
    mappers = [get_mapper(chunk) for chunk in chunks]
    seed_ranges = {range(a,a+b) for (a,b) in windowed(seeds,2,step=2)}

    for mapper in mappers:
        seed_ranges = maptotal(seed_ranges,mapper)
    
    return min(r.start for r in seed_ranges)


#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 35

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

ans_sample2 = part2(sample_data)
assert ans_sample2 == 46

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
