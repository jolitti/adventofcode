from aocd.models import Puzzle
from aocd import lines
from math import prod

puzzle = Puzzle(year=2022,day=8)
side = len(lines)

def add_pair(x:tuple[int,int],y:tuple[int,int]) -> tuple[int,int]:
    a,b = x
    c,d = y
    return (a+c,b+d)

def in_bounds(pos:tuple[int,int]) -> bool:
    x,y = pos
    return 0<=x<side and 0<=y<side

def explore_direction(start:tuple[int,int],direction:tuple[int,int]):
    pos = start
    x,y = pos
    visible[y][x] = True
    max_height = data[y][x]
    pos = add_pair(pos,direction)
    for _ in range(side-1):
        x,y = pos
        height = data[y][x]
        if height>max_height:
            max_height = height
            visible[y][x] = True
        pos = add_pair(pos,direction)
        if max_height >= 9: break

def process_rows(start:tuple[int,int], direction:tuple[int,int], direction2:tuple[int,int]):
    pos = start
    for _ in range(side):
        explore_direction(pos,direction2)
        pos = add_pair(pos,direction)

def sight_range(start:tuple[int,int],direction:tuple[int,int]) -> int:
    x,y = start
    height = data[y][x]
    pos = start
    ans = 0
    while True:
        pos = add_pair(pos,direction)
        x,y = pos
        if not in_bounds(pos): return ans
        ans += 1
        if data[y][x] >= height: return ans 

directions = [(1,0),(0,1),(-1,0),(0,-1)]

def treehouse_score(start:tuple[int,int]) -> int:
    dirpoints = [sight_range(start,d) for d in directions]
    return prod(dirpoints)


angles_of_attack = [
        ((0,0),(1,0),(0,1)),
        ((side-1,0),(0,1),(-1,0)),
        ((side-1,side-1),(-1,0),(0,-1)),
        ((0,side-1),(0,-1),(1,0)),
        ]

data = [[int(c) for c in l] for l in lines]
assert(side == len(data[0]))
visible = [[False for _ in l] for l in data]

for st,d1,d2 in angles_of_attack:
    process_rows(st,d1,d2)

ans1 = sum(l.count(True) for l in visible)
print(f"First answer: {ans1}")
puzzle.answer_a = ans1

ans2 = max(treehouse_score((x,y)) for x in range(1,side-1) for y in range(1,side-1))
print(f"Second answer: {ans2}")
puzzle.answer_b = ans2
