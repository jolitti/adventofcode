from aocd.models import Puzzle
from itertools import groupby

puzzle = Puzzle(year=2023,day=13)
data = puzzle.input_data.splitlines()
sample_data = \
"""#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".splitlines()

sample_data2 = \
"""#.....
......
..##..
..##..
......
......""".splitlines()

#--- CONSTANTS

#--- FUNCTIONS
def chunks(data) -> list[list[str]]:
    return [
            list(v)
            for k,v in groupby(data,lambda s:s!="")
            if k
            ]

def eq_pairs(chunk) -> set[int] | None:
    ans = set()
    for i,(s1,s2) in enumerate(zip(chunk,chunk[1:])):
        if s1 == s2: ans.add(i)
    return ans

def translate(chunk) -> list[str]:
    return ["".join(l) for l in zip(*chunk)]

def mirror_pos(chunk) -> set[int]:
    candidates = eq_pairs(chunk)
    if not candidates: return set()
    ans = set()
    for p in candidates:
        if all(a==b for a,b in zip(chunk[p::-1],chunk[p+1:])):
            ans.add(p)
    return ans

def differences(chunk,pos) -> list[int]:
    ans = []
    for a,b in zip(chunk[pos::-1],chunk[pos+1:]):
        ans.append(sum(aa!=bb for aa,bb in zip(a,b)))
    return ans

def mirror_smudge_pos(chunk) -> set[int]:
    ans = set()
    for i in range(len(chunk)-1):
        diff = differences(chunk,i)
        diff = set(diff)
        if diff == {1} or diff == {0,1}:
            ans.add(i)
    return ans

#--- PARTS
def part1(data) -> int:
    data = chunks(data)
    ans = 0
    for ch in data:
        a = mirror_pos(ch)
        a = 0 if not a else a.pop()+1
        b = mirror_pos(translate(ch))
        b = 0 if not b else b.pop()+1
        ans += 100*a + b
    return ans

def part2(data) -> int:
    data = chunks(data)
    ans = 0
    for ch in data:
        a = mirror_smudge_pos(ch)
        assert len(a) <= 1
        a = a.pop()+1 if a else 0
        b = mirror_smudge_pos(translate(ch))
        assert len(b) <= 1
        b = b.pop()+1 if b else 0

        ans += 100*a+b
    return ans

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 405

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

ans_sample2 = part2(sample_data)
assert ans_sample2 == 400

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
