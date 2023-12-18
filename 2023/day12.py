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

sample_data2 = \
"""??..??...?## 1,1,3
?..??...?## 1,1,3
??...?## 1,1,3
?...?## 1,1,3
?## 1,1,3
## 1,1,3
?## 1,3
## 1,3
?## 1,3
??...?## 1,3
?...?## 1,3
?## 1,3
?## 3
## 3
?## 3
??...?## 1,3""".splitlines()



#--- CONSTANTS
broken_finder = re.compile(r"#+")

#--- FUNCTIONS
def string_tuple(line) -> tuple[str,tuple[int]]:
    string, tup = line.split()
    return string, tuple(int(n) for n in tup.split(","))

@cache
def combinations(s,groups) -> int:
    s = s.strip(".")
    #print(s,groups)
    if not groups:
        return 1 if "#" not in s else 0
    if not s:
        return 0

    ans = 0

    if s[0] == "?":
        ans += combinations(s[1:],groups)

    head = s[:groups[0]]
    if len(head) < groups[0]: return 0
    sep = s.removeprefix(head)[:1]
    tail = s.removeprefix(head+sep)
    #print(first_slice,sep,remainder)
    if sep != "#" and "." not in head:
        ans += combinations(tail,groups[1:])
    return ans

#print(combinations(".??..??...?##.",(1,1,3)))

#--- PARTS

def part1(data) -> int:
    data = [string_tuple(line) for line in data]
    #for a,b in data:
    #    print(a,b)
    #    print(combinations(a,b))
    return sum(combinations(a,b) for a,b in data)


def part2(data) -> int:
    data = [string_tuple(line) for line in data]
    data = [
            ("?".join([line]*5),tup*5)    
            for line,tup in data
        ]
    return sum(combinations(a,b) for a,b in data)

#--- ANSWERS


ans_sample1 = part1(sample_data)
assert ans_sample1 == 21

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

ans_sample2 = part2(sample_data)
assert ans_sample2 == 525152

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
