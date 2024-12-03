from aocd.models import Puzzle

import re

puzzle = Puzzle(year=2024,day=3)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")
sample_data_2 = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))don't()mul(5,5)"]

#--- CONSTANTS
mulfinder = r"mul\(\d+,\d+\)"
muldodontfinder = mulfinder + r"|do\(\)|don't\(\)"

#--- FUNCTIONS
def row_ans_1(data) -> int:
    muls = re.findall(mulfinder,data)
    tot = 0
    for m in muls:
        m = m.removeprefix("mul(").removesuffix(")")
        a,b = map(int,m.split(","))
        tot += a*b
    return tot
    
def row_ans_2(data) -> int:
    tot = 0
    count = True
    for match in re.findall(muldodontfinder,data):
        if match == "do()":
            count = True
        elif match == "don't()":
            count = False
        elif count:
            m = match.removeprefix("mul(").removesuffix(")")
            a,b = map(int,m.split(","))
            tot += a*b
    return tot

#--- PARTS

def part1(data) -> int:
    return sum(row_ans_1(l) for l in data)

def part2(data) -> int:
    data = "".join(data)
    return row_ans_2(data)

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 161

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

ans_sample2 = part2(sample_data_2)
assert ans_sample2 == 48

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
