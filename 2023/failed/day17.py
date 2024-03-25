from aocd.models import Puzzle
import heapq

puzzle = Puzzle(year=2023,day=17)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")
small_sample = \
"""199
111
991""".splitlines()

#--- CONSTANTS
north,south,east,west = (0,-1),(0,1),(1,0),(-1,0)
directions = {north,south,east,west}

#--- FUNCTIONS
def add(v1,v2) -> tuple[int]:
    return tuple(a+b for a,b in zip(v1,v2))

def mandist(v1,v2) -> int:
    return sum(abs(a-b) for a,b in zip(v1,v2))

def inverse(direction) -> tuple[int]:
    if not direction: return None
    return tuple(-x for x in direction)

def allowed_dirs(history) -> set[tuple]:
    if not history: return directions
    last = history[-1]
    ans = directions - {inverse(last)}
    if tuple(history[-3:]) == (last,last,last):
        ans -= {last}
    return ans

#assert allowed_dirs((east,north,north,north)) == {east,west}
#assert allowed_dirs((south,east,north,north)) == {east,west,north}

def in_bounds(pos,data) -> bool:
    x,y = pos
    lx = len(data[0])
    ly = len(data)
    return 0 <= x < lx and 0 <= y < ly

#--- PARTS

def part1(data) -> int:
    data = [[int(c) for c in line] for line in data]
    target = (len(data[0])-1,len(data)-1)

    queue = [(mandist((0,0),target),0,(),(0,0))] # loss_bound, loss, history, position
    explored = {(0,0)}
    heapq.heapify(queue)
    count = 0
    while queue:
        #print(len(explored) / (len(data)*len(data[0])))
        print(len(queue),len(data)*len(data[0]))
        _,loss,history,position = heapq.heappop(queue)
        if position in explored:
            count += 1
        print(count)
        explored.add(position)
        if position == target:
            return loss
        for d in allowed_dirs(history):
            newpos = add(position,d)
            if newpos in explored or not in_bounds(newpos,data):
                continue
            x,y = newpos
            newloss = loss + data[y][x]
            heapq.heappush(queue,(newloss+mandist(newpos,target),newloss,history[-3:]+(d,),newpos))
    raise ValueError("End of queue")


def part2(data) -> int:
    pass

part1(small_sample)

ans_sample1 = part1(sample_data)
assert ans_sample1 == 102

#ans1 = part1(data)
#print(f"Answer to part 1: {ans1}")

#ans_sample2 = part2(sample_data)
#assert ans_sample2 == 

#ans2 = part2(data)
#print(f"Answer to part 2: {ans2}")
