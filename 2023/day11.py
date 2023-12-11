from aocd.models import Puzzle
from itertools import combinations

puzzle = Puzzle(year=2023,day=11)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS

#--- FUNCTIONS
def expand_space(point,empty_rows,empty_cols,amount=1) -> tuple[int,int]:
    x,y = point
    x += sum(x > col for col in empty_cols)*amount
    y += sum(y > row for row in empty_rows)*amount
    return (x,y)

def manhattan_dist(p1,p2) -> int:
    return sum(abs(a-b) for a,b in zip(p1,p2))

#--- PARTS

def part1(data) -> int:
    empty_rows = [i for i,line in enumerate(data) if "#" not in line]
    empty_cols = [i for i,col in enumerate(zip(*data)) if "#" not in col]

    galaxies = [
            (x,y) 
            for y in range(len(data))
            for x in range(len(data[0]))
            if data[y][x]=="#"
            ]
    galaxies = [expand_space(g,empty_rows,empty_cols) for g in galaxies]

    return sum(manhattan_dist(p1,p2) for (p1,p2) in combinations(galaxies,2))

def part2(data) -> int:
    empty_rows = [i for i,line in enumerate(data) if "#" not in line]
    empty_cols = [i for i,col in enumerate(zip(*data)) if "#" not in col]

    galaxies = [
            (x,y) 
            for y in range(len(data))
            for x in range(len(data[0]))
            if data[y][x]=="#"
            ]
    galaxies = [expand_space(g,empty_rows,empty_cols,1_000_000-1) for g in galaxies]

    return sum(manhattan_dist(p1,p2) for (p1,p2) in combinations(galaxies,2))

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 374

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

#ans_sample2 = part2(sample_data)
#assert ans_sample2 == 

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
