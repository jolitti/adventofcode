from aocd.models import Puzzle

puzzle = Puzzle(year=2024,day=2)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS

#--- FUNCTIONS
def parse(line) -> list:
    return list(map(int,line.split(" ")))

def is_safe(seq,direction=None) -> bool:
    if len(seq) <= 1:
        return True
    a,b = seq[:2]
    if a == b:
        return False
    if abs(a-b) > 3:
        return False
    if direction==None:
        if a<b:
            return is_safe(seq[1:],"up")
        if a>b:
            return is_safe(seq[1:],"down")
    if direction=="up" and a>b:
        return False
    if direction=="down" and a<b:
        return False
    return is_safe(seq[1:],direction)

def is_safe_with_tolerance(seq) -> bool:
    if is_safe(seq):
        return True
    else:
        for i in range(len(seq)):
            if is_safe(seq[:i]+seq[i+1:]):
                return True
        return False


#--- PARTS

def part1(data) -> int:
    data = [parse(l) for l in data]
    ans = sum(is_safe(d) for d in data)
    return ans

def part2(data) -> int:
    data = [parse(l) for l in data]
    ans = sum(is_safe_with_tolerance(d) for d in data)
    return ans

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 2

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

ans_sample2 = part2(sample_data)
assert ans_sample2 == 4
assert is_safe_with_tolerance([48,46,47,49,51,54,56])

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
