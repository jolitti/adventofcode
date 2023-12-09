from aocd.models import Puzzle

puzzle = Puzzle(year=2023,day=9)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS

#--- FUNCTIONS
def all_zero(seq) -> bool:
    for n in seq:
        if n != 0: return False
    return True

def differences(seq) -> list[int]:
    ans = []
    for a,b in zip(seq,seq[1:]):
        ans.append(b-a)
    return ans

def prediction(seq) -> int:
    diff = differences(seq)
    if all_zero(diff):
        return seq[-1]
    return seq[-1] + prediction(diff)

def prediction_previous(seq) -> int:
    diff = differences(seq)
    if all_zero(diff):
        return seq[0]
    return seq[0] - prediction_previous(diff)

#--- PARTS

def part1(data) -> int:
    data = [[int(n) for n in line.split()] for line in data]
    return sum(prediction(seq) for seq in data)

def part2(data) -> int:
    data = [[int(n) for n in line.split()] for line in data]
    return sum(prediction_previous(seq) for seq in data)

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 114

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

ans_sample2 = part2(sample_data)
assert ans_sample2 == 2

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
