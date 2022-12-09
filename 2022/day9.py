from aocd import lines
from aocd.models import Puzzle

direction_dict = {"U":(0,1), "D":(0,-1), "L": (-1,0), "R": (1,0)}
def add_pair(a:tuple[int,int],b:tuple[int,int]) -> tuple[int,int]:
    x,y = a
    xx,yy = b
    return (x+xx,y+yy)

def mandist(a,b) -> int:
    x,y = a
    xx,yy = b
    return abs(xx-x) + abs(yy-y)

def clamp(x:int) -> int:
    x = min(x,1)
    x = max(x,-1)
    return x

def follow_head(head:tuple[int,int],tail:tuple[int,int]) -> tuple[int,int]:
    x,y = head
    xx,yy = tail
    dx = x-xx
    dy = y-yy
    dist = mandist(head,tail)
    if dist<=1: return tail
    if dist==2 and abs(dx)==abs(dy): return tail
    dx,dy = clamp(dx),clamp(dy)
    return add_pair(tail,(dx,dy))
assert(follow_head((0,0),(0,0)) == (0,0))
assert(follow_head((1,0),(0,0)) == (0,0))
print(follow_head((1,1),(0,0)))
assert(follow_head((1,1),(0,0)) == (0,0))

puzzle = Puzzle(year=2022,day=9)
data = [l.split(" ") for l in lines]
data = [(direction_dict[direction], int(amount)) for direction,amount in data]

head_pos = (0,0)
tail_pos = (0,0)
visited_positions = set()

for v, length in data:
    for _ in range(length):
        head_pos = add_pair(head_pos,v)
        tail_pos = follow_head(head_pos,tail_pos)
        visited_positions.add(tail_pos)

ans1 = len(visited_positions)
print(f"First answer: {ans1}")
puzzle.answer_a = ans1

pos = [(0,0)]*10
visited = set()
for v, length in data:
    for _ in range(length):
        newpos = []
        newpos.append(add_pair(pos[0],v))
        for p in pos[1:]:
            newpos.append(follow_head(newpos[-1],p))
        visited.add(newpos[-1])
        pos = newpos

ans2 = len(visited)
print(f"Second answer: {ans2}")
puzzle.answer_b = ans2
