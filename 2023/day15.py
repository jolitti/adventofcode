from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2023,day=15)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS
letter_finder = re.compile(r"[a-z]+")
number_finder = re.compile(r"\d+")

#--- FUNCTIONS
def hashcode(s) -> int:
    ans = 0
    for c in s:
        ans += ord(c)
        ans *= 17
        ans %= 256
    return ans

#--- PARTS
def part1(data) -> int:
    data = list(data[0].split(","))
    return sum(map(hashcode,data))

def part2(data) -> int:
    data = list(data[0].split(","))
    boxes = [([],set()) for _ in range(256)]
    for d in data:
        label = letter_finder.findall(d)[0]
        l,s = boxes[hashcode(label)]
        if "-" in d:
            if label in s:
                newl = [(ll,n) for (ll,n) in l if ll!=label]
                s.remove(label)
                boxes[hashcode(label)] = (newl,s)
        else:
            new_n = int(number_finder.findall(d)[0])
            if label in s:
                newl = [(ll,new_n) if ll==label else (ll,nn) for (ll,nn) in l]
                boxes[hashcode(label)] = (newl,s)
            else:
                s.add(label)
                newl = l + [(label,new_n)]
                boxes[hashcode(label)] = (newl,s)
    ans = 0
    for i in range(255):
        for j,(ll,nn) in enumerate(boxes[i][0]):
            ans += (i+1)*(j+1)*nn
    return ans

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 1320

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

ans_sample2 = part2(sample_data)
assert ans_sample2 == 145

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
