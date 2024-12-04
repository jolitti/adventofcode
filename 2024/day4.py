from aocd.models import Puzzle

puzzle = Puzzle(year=2024,day=4)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")
sample_data2 = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX"
        ]

#--- CONSTANTS
TARGET = "XMAS"
TARGET2 = "MAS"

directions = [
        (dx,dy) for dx in (-1,0,1) for dy in (-1,0,1) 
        if not (dx==dy==0)
        ]

dirs2 = [
        ((a,b),(-b,a))
        for a in (-1,1)
        for b in (-1,1)
        ]

#--- FUNCTIONS
def in_bounds(pos,array) -> bool:
    x,y = pos
    if x<0 or y<0: return False
    if y>=len(array) or x>=len(array[0]): return False
    return True

def tupadd(t1,t2) -> tuple:
    return tuple(a+b for a,b in zip(t1,t2))

def tupflip(t) -> tuple:
    return tuple(-a for a in t)

def wordappears(word,pos,direction,array) -> bool:
    if not word:
        return True
    if not in_bounds(pos,array):
        return False
    head,tail = word[0],word[1:]
    if array[pos[1]][pos[0]] != head:
        return False
    pos2 = tupadd(pos,direction)
    return wordappears(tail,pos2,direction,array)

#--- PARTS

def part1(data) -> int:
    tot = 0
    for x in range(len(data[0])):
        for y in range(len(data)):
            for d in directions:
                if wordappears(TARGET,(x,y),d,data):
                    tot += 1
    return tot

def part2(data) -> int:
    tot = 0
    for x in range(len(data[0])):
        for y in range(len(data)):
            for dd in dirs2:
                p1,p2 = (tupadd((x,y),tupflip(d)) for d in dd)
                d1,d2 = dd
                if wordappears(TARGET2,p1,d1,data) \
                and wordappears(TARGET2,p2,d2,data):
                    tot += 1
    return tot

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 4

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

ans_sample2 = part2(sample_data2)
assert ans_sample2 == 9

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
