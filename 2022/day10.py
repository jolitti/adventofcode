from aocd import lines
from aocd.models import Puzzle
from more_itertools import windowed

puzzle = Puzzle(year=2022,day=10)

def get_states(starting:int, command:str) -> list[int]:
    if command=="noop":
        return [starting]
    num = int(command.split(" ")[1])
    return [starting,starting+num]

def process(cmds:list[str]) -> list[int]:
    x = 1
    states = []

    for l in cmds:
        l = l.strip()
        states += get_states(x,l)
        x = states[-1]
    return [1]+states

def sigstr(cmds:list[str]) -> int:
    values = process(cmds)
    ans = 0
    for t in [20,60,100,140,180,220]:
        ans += (t*values[t-1])
        # print(t,values[t-1],t*values[t-1])
    return ans

values = process(lines)
ans1 = sigstr(lines)

print(f"First answer: {ans1}")
puzzle.answer_a = ans1

screen = ""
for i in range(240):
    current = values[i]
    if i%40 in range(current-1,current+2): screen+="#"
    else: screen+="."

screen = windowed(screen,40,step=40)
screen = ["".join(l) for l in screen]
for l in screen: print(l)

ans2 = "ZFBFHGUP"
print(f"Second anwser: {ans2}")
puzzle.answer_b = ans2
