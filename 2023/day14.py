from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2023,day=14)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#---CONSTANTS
groups_finder = re.compile(r"[O.]+|#+")
M = 1000000000

#--- FUNCTIONS
def translate(data) -> list[str]:
    return list("".join(row) for row in zip(*data))
def rotate(data) -> list[str]:
    return list("".join(reversed(row)) for row in zip(*data))

def line_load(line) -> int:
    line = line.lstrip("#")
    if "O" not in line: return 0
    head = line.split("#",1)[0]
    tail = line.removeprefix(head)
    rocks = head.count("O")
    head_load = sum(len(line)-i for i in range(rocks))
    return head_load + line_load(tail)

def line_load_no_tilt(line) -> int:
    ans = 0
    for i in range(len(line)):
        if line[i]=="O":
            ans += len(line) - i
    return ans

def line_tilt(line) -> str:
    groups = groups_finder.findall(line)
    ans = []
    for s in groups:
        if "#" in s:
            ans.append(s)
        else:
            ans.append("O"*s.count("O")+"."*s.count("."))
    return "".join(ans)
assert line_tilt("..OO..#.OO.OO.O") == "OO....#OOOOO..."

def tilt(data) -> list[str]:
    return [line_tilt(line) for line in data]

def cycle_until_loop(data) -> tuple[int,int,dict]:
    states = {}
    data = rotate(rotate(rotate(data))) # facing north for tilt
    i = 0
    while tuple(data) not in states:
        states[tuple(data)] = i
        for _ in range(4):
            data = tilt(data)
            data = rotate(data)
        i+=1
    return states[tuple(data)],i,{v:k for k,v in states.items()}


#--- PARTS

def part1(data) -> int:
    data = translate(data)
    return sum(line_load(line) for line in data)

def part2(data) -> int:
    a,b,states = cycle_until_loop(data)
    n = (M-a)//(b-a) #number of cycles
    c = M -a -n*(b-a)
    assert c < (b-a)
    state = rotate(states[a+c])
    return sum(line_load_no_tilt(line) for line in translate(state))

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 136

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

ans_sample2 = part2(sample_data)
assert ans_sample2 == 64

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
