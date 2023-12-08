from aocd.models import Puzzle
import re
from itertools import cycle
from math import lcm

puzzle = Puzzle(year=2023,day=8)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS

#--- FUNCTIONS
def steps_to_end(state,node_map,directions,validator) -> int:
    ans = 0
    for d in cycle(directions):
        state = node_map[state][d]
        ans += 1
        if validator(state):
            return ans

def loop_insight(state,node_map,directions):
    first_dest = None
    counter = 0
    for i,d in cycle(enumerate(directions)):
        if counter>100000: return
        state = node_map[state][d]
        counter += 1
        if state[-1] == "Z":
            if first_dest is None:
                first_dest = counter
            print(state,counter)
            print(counter/first_dest)


#--- PARTS

def part1(data) -> int:
    directions = [0 if c=="L" else 1 for c in data[0]]

    node_map = {}
    for line in data[2:]:
        line = re.sub(r"[=,\(\)]","",line)
        source,left,right = line.split()
        node_map[source] = (left,right)

    return steps_to_end("AAA",node_map,directions,lambda s:s=="ZZZ")

def part2(data) -> int:
    directions = [0 if c=="L" else 1 for c in data[0]]

    node_map = {}
    first_nodes = set()
    for line in data[2:]:
        line = re.sub(r"[=,\(\)]","",line)
        source,left,right = line.split()
        node_map[source] = (left,right)
        if source[-1] == "A":
            first_nodes.add(source)

    steps = [
            steps_to_end(node,node_map,directions,lambda s:s[-1]=="Z")
            for node in first_nodes
            ]
    return lcm(*steps)

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 2

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

#ans_sample2 = part2(sample_data)
#assert ans_sample2 == 

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
