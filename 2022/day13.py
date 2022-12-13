from aocd.models import Puzzle
from more_itertools import windowed
from enum import Enum
from functools import cmp_to_key
puzzle = Puzzle(year=2022,day=13)

class Comp(Enum):
    less = "<"
    equals = "="
    more = ">"

def cmp(a,b) -> Comp:
    if isinstance(a,int) and isinstance(b,int):
        if a<b: return Comp.less
        elif a==b: return Comp.equals
        return Comp.more

    if isinstance(a,int): return cmp([a],b)
    if isinstance(b,int): return cmp(a,[b])

    for aa,bb in zip(a,b):
        res = cmp(aa,bb)
        if res!=Comp.equals: return res
    return cmp(len(a),len(b))

with open("inputs/input13") as file:
    lines = file.readlines()
with open("samples/sample13") as file:
    samplelines = file.readlines()

def read_data(d:list[str]) -> list[tuple]:
    data = []
    for win in windowed(d,3,step=3):
        a,b = win[0].strip(),win[1].strip()
        data.append((eval(a),eval(b)))
    return data

ans1 = 0
for i,(a,b) in enumerate(read_data(lines)):
    if cmp(a,b)==Comp.less: ans1+=i+1

print(f"First answer: {ans1}") # 5938
puzzle.answer_a = ans1

data = [eval(l.strip()) for l in lines if l.strip()!=""]
data.append([[2]])
data.append([[6]])

data.sort(key=cmp_to_key(lambda a,b: -1 if cmp(a,b)==Comp.less else 1))

ans2 = 1
for i,d in enumerate(data):
    if d==[[2]] or d==[[6]]: ans2 *= (i+1)
print(f"Second answer: {ans2}") # 29025
puzzle.answer_b = ans2
