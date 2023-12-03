from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2023,day=3)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS
number_finder = re.compile(r"\d+")

#--- FUNCTIONS

#--- PARTS

def part1(data) -> int:
    # symbol scan
    symbols = {}
    for y,line in enumerate(data):
        for x,c in enumerate(line):
            if not c.isnumeric() and c!=".":
                symbols[(x,y)] = c
    symbols_set = {k for k,v in symbols.items()}
    total = 0
    
    for y,line in enumerate(data):
        for number in number_finder.finditer(line):
            x_start,x_end = number.start(),number.end()
            symbol_candidates = set()
            symbol_candidates.add((x_start-1,y))
            symbol_candidates.add((x_end,y))
            for x in range(x_start-1,x_end+1):
                symbol_candidates.add((x,y-1))
                symbol_candidates.add((x,y+1))
            if len(symbol_candidates & symbols_set) > 0:
                total += int(line[number.start():number.end()])
    return total

def part2(data) -> int:
    symbols = {}
    for y,line in enumerate(data):
        for x,c in enumerate(line):
            if not c.isnumeric() and c!=".":
                symbols[(x,y)] = c
    gear_set = {k:[] for k,v in symbols.items() if v == "*"}
    for y,line in enumerate(data):
        for number in number_finder.finditer(line):
            x_start,x_end = number.start(),number.end()
            symbol_candidates = set()
            symbol_candidates.add((x_start-1,y))
            symbol_candidates.add((x_end,y))
            for x in range(x_start-1,x_end+1):
                symbol_candidates.add((x,y-1))
                symbol_candidates.add((x,y+1))
            intersection = symbol_candidates & set(gear_set.keys())
            assert len(intersection) <= 1
            if len(intersection) == 0:
                continue
            inters = intersection.pop()
            gear_set[inters].append(int(line[number.start():number.end()]))
    total = 0
    for pos,nums in gear_set.items():
        if len(nums) == 2:
            total += nums[0] * nums[1]
    return total

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 4361

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")
assert ans1 == 553079

ans_sample2 = part2(sample_data)
assert ans_sample2 == 467835

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
