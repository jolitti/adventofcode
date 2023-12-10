from aocd.models import Puzzle
import numpy as np
from scipy.ndimage import label
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

structure = np.array([[0,1,0],[1,1,1],[0,1,0]])

#--- FUNCTIONS
def find_start(data) -> np.ndarray:
    for y,line in enumerate(data):
        for x,c in enumerate(line):
            if c=="S": return np.array([x,y])

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

def debug_line(line):
    print(line)
    inside = 0
    for i in range(len(line)):
        if line[i]=="." and inside_path((i,0),[line]): inside += 1
    print(inside)

#--- PARTS

def part1(data,first_direction) -> int:
    start_pos = find_start(data)
    pos = start_pos + first_direction
    direction = first_direction
    moves = 1

    while (pos != start_pos).any():
        char = data[pos[1]][pos[0]]
        direction = new_direction(char,direction)
        pos += direction
        moves += 1
    
    return (moves+1)//2


def part2(data,first_direction,subs_s="J",print_to_file=False) -> int:
    start_pos = find_start(data)
    for i in range(len(data)):
        data[i] = data[i].replace("S",subs_s)
    pos = start_pos + first_direction
    direction = first_direction
    
    visited_set = {tuple(start_pos)}
    visited_list = [tuple(start_pos)]

    while (pos != start_pos).any():
        visited_list.append(tuple(pos))
        visited_set.add(tuple(pos))

        char = data[pos[1]][pos[0]]
        direction = new_direction(char,direction)
        pos += direction

    unvisited_map = [
            [
                0 if (x,y) in visited_set else 1
                for x,_ in enumerate(line)
            ]
            for y,line in enumerate(data)
            ]
    #print(unvisited_map)
    labeled,ncomponents = label(unvisited_map,structure)
    _,component_counts = np.unique(labeled,return_counts=True)
    #print(labeled)

    data_path_only = [
            "".join(
                "." if (x,y) not in visited_set else c
                for x,c in enumerate(line)
            )
            for y,line in enumerate(data)
            ]

    #if print_to_file:
    #    with open("output10","a") as file:
    #        for y,line in enumerate(data_path_only):
    #            for x,char in enumerate(line):
    #                if (x,y) not in visited_set:
    #                    file.write("*")
    #                else:
    #                    file.write(data_path_only[y][x])
    #            file.write("\n")

    #ans = 0
    #for i in range(1,ncomponents+1): # we skip 0
    #    point = np.where(labeled == i)
    #    point = (point[1][0],point[0][0])

    #    #print(i, component_counts[i],point)

    #    if inside_path(point,data_path_only):
    #        ans += component_counts[i]

    #debug_line(data_path_only[len(data_path_only)//2])

    # TEMPORARY UGLIER SOLUTION
    ans = 0
    for y in range(len(data)):
        #print(data_path_only[y])
        for x in range(len(data[0])):
            if (x,y) not in visited_set:
                if inside_path((x,y),data_path_only):
                    ans += 1

    return ans
    

#--- ANSWERS

ans_sample1 = part1(sample_data,np.array([0,1]))
#print(ans_sample1)
assert ans_sample1 == 8

ans1 = part1(data,np.array([-1,0]))
print(f"Answer to part 1: {ans1}")

#ans_sample2 = part2(sample_data2,np.array([0,1]),"F")
#assert ans_sample2 == 4

ans_sample3 = part2(sample_data3,np.array([0,1]),"F")
assert ans_sample3==8

ans_sample4 = part2(sample_data4,np.array([0,1]),"7")
assert ans_sample4==10

#ans2 = part2(data,np.array([0,1]))
#print(f"Answer to part 2: {ans2}")
