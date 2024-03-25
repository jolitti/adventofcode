from aocd.models import Puzzle
import heapq

puzzle = Puzzle(year=2023,day=17)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS
north,south,east,west = (0,-1),(0,1),(1,0),(-1,0)
directions = {north,south,east,west}

#--- FUNCTIONS
def add(v1,v2) -> tuple[int]:
    return tuple(a+b for a,b in zip(v1,v2))

def mandist(v1,v2) -> int:
    return sum(abs(a-b) for a,b in zip(v1,v2))

def inverse(direction) -> tuple[int]:
    if not direction: return None
    return tuple(-x for x in direction)

def in_bounds(pos,data) -> bool:
    x,y = pos
    lx = len(data[0])
    ly = len(data)
    return 0 <= x < lx and 0 <= y < ly

def allowed_dirs(history) -> set[tuple]:
    if not history: return directions
    last = history[-1]
    ans = directions - {inverse(last)}
    if tuple(history[-3:]) == (last,last,last):
        ans -= {last}
    return ans

#--- PARTS

def part1(data) -> int:
    data = [[int(c) for c in line] for line in data]
    target = (len(data[0])-1,len(data)-1)

def part2(data) -> int:
    pass

#--- ANSWERS

ans_sample1 = part1(sample_data)
#assert ans_sample1 == 

#ans1 = part1(data)
#print(f"Answer to part 1: {ans1}")

#ans_sample2 = part2(sample_data)
#assert ans_sample2 == 

#ans2 = part2(data)
#print(f"Answer to part 2: {ans2}")
