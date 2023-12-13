from aocd.models import Puzzle
import re
from functools import cache

puzzle = Puzzle(year=2023,day=12)
data = puzzle.input_data.splitlines()
sample_data = \
"""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".splitlines()

#--- CONSTANTS
broken_finder = re.compile(r"#+")

#--- FUNCTIONS
def string_tuple(line) -> tuple[str,tuple[int]]:
    string, tup = line.split()
    return string, tuple(int(n) for n in tup.split(","))

def get_sequences(springs_completed) -> tuple[int]:
    assert "?" not in springs_completed
    return tuple(len(s) for s in broken_finder.findall(springs_completed))

assert get_sequences("#..#..###") == (1,1,3)

def combinations(springs, sequences) -> int:
    if springs[0]==".":
        return combinations(springs[1:],sequences)
    if springs[-1]==".":
        return combinations(springs[:-1],sequences)
    if springs.count("?") + springs.count("#") < sum(sequences):
        return 0
    if "?" not in springs:
        return 1 if get_sequences(springs)==sequences else 0
    working = combinations(springs.replace("?",".",1),sequences)
    broken = combinations(springs.replace("?","#",1),sequences)
    return working + broken

@cache
def comb(spr,seq) -> int:
    spr = spr.strip(".")
    if len(spr) < sum(seq):
        return 0
    if len(seq) == 0:
        return int("#" not in spr)
    if "#" not in spr and "." not in spr:
        if len(seq)==1 and seq[0] == len(spr):
            return 1

    first_spr_slice = spr[:seq[0]]
    if "." in first_spr_slice:
        return 0 # first element can't fit
    
    ans = 0
    if len(spr)>seq[0] and spr[seq[0]] != "#":
        ans += comb(spr[seq[0]+1:],seq[1:]) 
    if spr[0]=="?":
        ans += comb(spr[1:],seq)

    return ans

assert comb("??",(1,)) == 2
assert comb("????",(1,2)) == 1
assert comb("????",(1,1)) == 3
assert comb("???#???",(2,2)) == 2
assert comb("?###????????", (3,2,1)) == 10

#--- PARTS

def part1(data) -> int:
    data = [string_tuple(line) for line in data]
    for spr,seq in data:
        print(comb(spr,seq))
    return sum(comb(spr,seq) for spr,seq in data)

def part2(data) -> int:
    pass

#--- ANSWERS


ans_sample1 = part1(sample_data)
print(ans_sample1)
assert ans_sample1 == 21

#ans1 = part1(data)
#print(f"Answer to part 1: {ans1}")

#ans_sample2 = part2(sample_data)
#assert ans_sample2 == 

#ans2 = part2(data)
#print(f"Answer to part 2: {ans2}")
