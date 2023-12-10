from aocd.models import Puzzle
import numpy as np
import re

puzzle = Puzzle(year=2023,day=10)
data = puzzle.input_data.splitlines()
sample_data = \
"""..F7.
.FJ|.
SJ.L7
|F--J
LJ...
""".splitlines()

sample_data2 = \
"""..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........""".splitlines()

sample_data3 = \
""".F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...""".splitlines()

sample_data4 = \
"""FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L""".splitlines()

#--- CONSTANTS
char_to_dirs = {
        "|":"ns",
        "-":"ew",
        "L":"ne",
        "J":"nw",
        "7":"sw",
        "F":"se"
        }
dirs_to_vecs = {
        "n":np.array([0,-1]),
        "s":np.array([0,1]),
        "e":np.array([1,0]),
        "w":np.array([-1,0]),
        }
vecs_to_dirs = {tuple(v):k for k,v in dirs_to_vecs.items()}

dir_to_arrow = {
        "n":"^",
        "s":"v",
        "e":">",
        "w":"<"
        }
vecs_to_arrow = {k:dir_to_arrow[v] for k,v in vecs_to_dirs.items()}

cardinals = np.array(
        [[1,0],[0,1],[-1,0],[0,-1]]
        )

#--- FUNCTIONS
def find_start(data) -> np.ndarray:
    for y,line in enumerate(data):
        for x,c in enumerate(line):
            if c=="S": return np.array([x,y])

def start_char_and_dir(data,pos) -> tuple[chr,np.ndarray]:
    escape_dirs = []

    for dd in cardinals:
        x,y = tuple(pos + dd)
        newchar = data[y][x]
        if newchar==".":
            continue
        for d in char_to_dirs[newchar]:
            if (dirs_to_vecs[d]==-dd).all():
                escape_dirs.append(dd)

    ans_dir = escape_dirs[0]
    for char in r"|-FJL7":
        dirset = set(char_to_dirs[char])
        currentset = {vecs_to_dirs[tuple((esc))] for esc in escape_dirs}
        if dirset == currentset: return char,ans_dir
        

def new_direction(char, direction) -> np.ndarray:
    for cardinal in char_to_dirs[char]:
        candidate = dirs_to_vecs[cardinal]
        if (candidate != -direction).any():
            return candidate

def inside_path(point,data) -> bool:
    line_finder = re.compile(r"\||F-*J|L-*7")
    x,y = point
    ray = data[y][:x]
    intersections = len(line_finder.findall(ray))
    verdict = "inside" if intersections%2==1 else "outside"
    #print(f"{ray} {verdict}")
    return intersections % 2 == 1

#--- PARTS
def part1(data) -> int:
    start_pos = find_start(data)
    start_char, direction = start_char_and_dir(data,start_pos)
    new_data = [line.replace("S",start_char) for line in data]

    moves = 1
    position = start_pos + direction
    while (position!=start_pos).any():
        x,y = tuple(position)
        direction = new_direction(data[y][x],direction)
        position += direction
        moves += 1
    return (moves+1)//2

def part2(data) -> int:
    start_pos = find_start(data)
    start_char, direction = start_char_and_dir(data,start_pos)
    new_data = [line.replace("S",start_char) for line in data]

    visited = {tuple(start_pos):vecs_to_arrow[tuple(direction)]}
    
    position = start_pos + direction
    while (position!=start_pos).any():
        x,y = tuple(position)
        direction = new_direction(data[y][x],direction)
        visited[(x,y)] = vecs_to_arrow[tuple(direction)]
        position += direction

    #travel_map = [
    #        "".join(
    #                visited.get((x,y),".")
    #            for x in range(len(new_data[0]))
    #            )
    #        for y in range(len(new_data))
    #        ]

    data_visited_only = [
            "".join(
                new_data[y][x] if (x,y) in visited else "."
                for x in range(len(new_data[0]))
                )
            for y in range(len(new_data))
            ]

    ans = 0
    for y,line in enumerate(data_visited_only):
        for x,c in enumerate(line):
            if c=="." and inside_path((x,y),data_visited_only):
                    ans += 1

    return ans

ans1 = part1(data)
print(f"Answer to first part: {ans1}")
ans2 = part2(data)
print(f"Answer to the second part: {ans2}")
