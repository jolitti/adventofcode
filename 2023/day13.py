from aocd.models import Puzzle
from functools import cache

puzzle = Puzzle(year=2023,day=13)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS

#--- FUNCTIONS
@cache
def palindrome(s) -> bool:
    if len(s)%2==1: return False
    for i in range(len(s)//2):
        if s[i] != s[-i-1]: return False
    return True

assert (palindrome("aabbaa"))
assert not palindrome("abcccccc")

@cache
def mirrorpos(s) -> int | None:
    # left reduction
    temps = s
    while len(temps)>2:
        if palindrome(temps): return len(temps)//2
        temps = temps[:-1]
    
    # right reduction
    temps = s
    iters = 0
    while len(temps)>2:
        if palindrome(temps): return len(temps)//2 + iters - 1
        temps = temps[1:]
        iters += 1

    return None

def mirrorver(chunk) -> int | None:
    positions = [mirrorpos(s) for s in chunk]
    if len(set(positions)) == 1: return positions[0]
    return None

def mirrorhor(chunk) -> int | None:
    s = ["" for _ in chunk[0]]
    for line in chunk:
        for i,c in enumerate(line):
            s[i] += c
    return mirrorver(s)


#--- PARTS

def part1(data) -> int:
    chunks = []
    acc = []
    for line in data + [""]:
        if line == "":
            chunks.append(acc)
            acc = []
        else:
            acc.append(line)
    
    print(mirrorhor(chunks[0]))
def part2(data) -> int:
    pass

#--- ANSWERS

ans_sample1 = part1(sample_data)
#assert ans_sample1 == 

#ans1 = part1(data)
#print(f"Answer to part 1: {ans1}")

#ans_sample2 = part2(sample_data)
#assert ans_sample2 == 

#ans2 = part2(data)
#print(f"Answer to part 2: {ans2}")
