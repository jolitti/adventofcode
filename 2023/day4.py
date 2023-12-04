from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2023,day=4)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS

#--- FUNCTIONS
def parse_nums(line) -> tuple[set,set]:
    line = line.split(": ")[1]
    winning,numbers = line.split(" | ")
    winning = set(winning.split())
    numbers = set(numbers.split())
    return winning,numbers

def overlapping(line) -> int:
    a,b = parse_nums(line)
    return len(a & b)

def point(winning:set,numbers:set) -> int:
    common = len(winning & numbers)
    return 2**(common-1) if common > 0 else 0

#--- PARTS

def part1(data) -> int:
    total = 0
    for line in data:
        total += point(*parse_nums(line))
    return total

def part2(data) -> int:
    ans = np.ones((len(data)),dtype="int32")
    for i in range(len(data)):
        for j in range(overlapping(data[i])):
            ans[i+j+1] += ans[i]
    return np.sum(ans)

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 13

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

ans_sample2 = part2(sample_data)
print(ans_sample2)
assert ans_sample2 == 30

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
