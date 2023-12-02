from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2023,day=2)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

splitter = re.compile(r", |; ")
maxcubes = {"red":12,"green":13,"blue":14}

#---

def mincubes(line) -> dict:
    line = line.split(": ")[1]
    ans = {"red":0,"green":0,"blue":0}
    for item in splitter.split(line):
        number,color = item.split(" ")
        number = int(number)
        ans[color] = max(ans[color],number)
    return ans

def ispossible(cubes,maxcubes) -> bool:
    for color,number in cubes.items():
        if number > maxcubes[color]:
            return False
    return True

def part1(data) -> int:
    ans = 0
    for i,line in enumerate(data):
        if ispossible(mincubes(line),maxcubes):
            ans += i+1
    return ans

def part2(data) -> int:
    ans = 0
    for line in data:
        power = 1
        for _,number in mincubes(line).items(): power *= number
        ans += power
    return ans

#---

ans_sample1 = part1(sample_data)
assert ans_sample1 == 8

ans1 = part1(data)
print(ans1)

ans_sample2 = part2(sample_data)
assert ans_sample2 == 2286

ans2 = part2(data)
print(ans2)
