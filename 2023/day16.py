from aocd.models import Puzzle

puzzle = Puzzle(year=2023,day=16)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS
north,south,east,west = (0,-1),(0,1),(1,0),(-1,0)
horizontal = {east,west}
vertical = {north,south}

#--- FUNCTIONS
def add(v1,v2) -> tuple[int]:
    return tuple(a+b for a,b in zip(v1,v2))

def in_bounds(pos,data) -> bool:
    x,y = pos
    return 0 <= x < len(data[0]) and 0 <= y < len(data)

def ray_result(ray,tile) -> set[tuple[int]]:
    assert ray in horizontal or ray in vertical
    match tile:
        case ".":
            return {ray}
        case "-":
            return {ray} if ray in horizontal else horizontal
        case "|":
            return {ray} if ray in vertical else vertical
        case "\\":
            if ray in horizontal:
                return {north} if ray==west else {south}
            if ray in vertical:
                return {west} if ray==north else {east}
        case "/":
            if ray in horizontal:
                return {south} if ray==west else {north}
            if ray in vertical:
                return {east} if ray==north else {west}
        case _:
            raise ValueError(f"Invalid tile {tile}")

#--- PARTS

def part1(data) -> int:
    rays = {(x,y):set() for x in range(len(data[0])) for y in range(len(data))} # pos : set[rays]
    frontier = {((0,0),east)}

    while frontier:
        pos,ray = frontier.pop()
        x,y = pos
        new_rays = ray_result(ray,data[y][x])
        for r in list(new_rays):
            rays[pos].add(r)
            new_pos = add(pos,r)
            if not in_bounds(new_pos,data):
                continue
            if r not in rays[new_pos]:
                rays[new_pos].add(r)
                frontier.add((new_pos,r))

    return sum(len(rays[(x,y)]) > 0 for x in range(len(data[0])) for y in range(len(data)))


def part2(data) -> int:
    pass

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 46

#ans1 = part1(data)
#print(f"Answer to part 1: {ans1}")

#ans_sample2 = part2(sample_data)
#assert ans_sample2 == 

#ans2 = part2(data)
#print(f"Answer to part 2: {ans2}")
