from aocd.models import Puzzle

puzzle = Puzzle(year=2023,day=5)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS

#--- FUNCTIONS
def get_mapper(lines) -> dict:
    ans = {}
    for l in lines:
        dest,source,count = map(int,l.split())
        ans[range(source,source+count)] = dest
    return ans

def map_value(val,mapper) -> int:
    for value_range,dest in mapper.items():
        if val in value_range:
            return dest + (val - value_range.start)
    return val

def get_location(seed,mappers) -> int:
    ans = seed
    #print(ans)
    for m in mappers:
        ans = map_value(ans,m)
        #print(ans)
    #print("===")
    return ans

#--- PARTS

def part1(data) -> int:
    seeds = data[0]
    seeds = [int(s) for s in seeds.removeprefix("seeds: ").split()]
    chunks = []
    acc = []
    for line in data[2:]+[""]:
        if line=="":
            chunks.append(acc[1:])
            acc = []
        else:
            acc.append(line)
    mappers = [get_mapper(chunk) for chunk in chunks]

    dests = [get_location(seed,mappers) for seed in seeds]
    #print(dests)
    return min(dests)

def part2(data) -> int:
    pass

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 35

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

#ans_sample2 = part2(sample_data)
#assert ans_sample2 == 

#ans2 = part2(data)
#print(f"Answer to part 2: {ans2}")
