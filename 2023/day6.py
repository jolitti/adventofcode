from aocd.models import Puzzle
from math import sqrt,floor,ceil,prod

puzzle = Puzzle(year=2023,day=6)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS

#--- FUNCTIONS
def win_boundaries(budget,record) -> tuple[int,int]:
    delta = sqrt(budget**2 - 4*record)
    ans1 = (budget -delta)/2
    ans2 = (budget +delta)/2
    return floor(ans1)+1,ceil(ans2)-1

def win_interval(budget,record) -> int:
    a,b = win_boundaries(budget,record)
    return b-a+1

def part1(data) -> int:
    times = [int(t) for t in data[0].split()[1:]]
    distances = [int(d) for d in data[1].split()[1:]]
    
    intervals = [win_interval(t,d) for t,d in zip(times,distances)]
    return prod(intervals)

def part2(data) -> int:
    time = int(data[0].removeprefix("Time:").replace(" ",""))
    distance = int(data[1].removeprefix("Distance:").replace(" ",""))

    return win_interval(time,distance)

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 288

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

ans_sample2 = part2(sample_data)
assert ans_sample2 == 71503

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
