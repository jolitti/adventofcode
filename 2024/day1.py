from aocd.models import Puzzle
from collections import Counter

puzzle = Puzzle(year=2024,day=1)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS

#--- FUNCTIONS
def turn_to_lists(data) -> tuple[list]:
    list1,list2 = [],[]
    for d in data:
        a,b = map(int,d.split("  "))
        list1.append(a)
        list2.append(b)
    return list1,list2

#--- PARTS

def part1(data) -> int:
    l1,l2 = turn_to_lists(data)
    l1,l2 = sorted(l1),sorted(l2)
    tot_dist = 0
    for a,b in zip(l1,l2):
        tot_dist += abs(a-b)
    return tot_dist

def part2(data) -> int:
    l1,l2 = turn_to_lists(data)
    c2 = Counter(l2)
    tot = 0
    for n in l1:
        tot += n*c2[n]
    return tot

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 11

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

ans_sample2 = part2(sample_data)
assert ans_sample2 == 31

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
