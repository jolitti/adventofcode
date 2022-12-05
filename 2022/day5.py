from aocd.models import Puzzle
from aocd import lines, numbers
from more_itertools import windowed

def third_char(s:str) -> chr:
    return s[2]

puzzle = Puzzle(year=2022,day=5)
data = lines

initial_state = lines[:8]
initial_state = [" " + s for s in initial_state]
initial_state = [list(map(third_char,windowed(l,4,step=4))) for l in initial_state]
actions = numbers[1:]

stacks = []
for i in range(len(initial_state) + 1):
    stack = []
    for row in initial_state:
        if row[i]!=" ": stack.insert(0,row[i])
    stacks.append(stack)

stacks2 = [s.copy() for s in stacks]

for n,source,dest in actions:
    source,dest = source-1,dest-1
    s = stacks[source]
    d = stacks[dest]
    for _ in range(n): d.append(s.pop())

for n,source,dest in actions:
    source,dest = source-1,dest-1
    source, dest = stacks2[source], stacks2[dest]
    tempstack = []
    for _ in range(n): tempstack.append(source.pop())
    for _ in range(n): dest.append(tempstack.pop())

ans1 = [s[-1] for s in stacks]
ans1 = "".join(ans1)
print(f"First answer: {ans1}") # VGBBJCRMN
puzzle.answer_a = ans1

ans2 = [s[-1] for s in stacks2]
ans2 = "".join(ans2)
print(f"Second answer: {ans2}") # LBBVJBRMH
puzzle.answer_b = ans2
