from aocd.models import Puzzle
import regex as re

puzzle = Puzzle(2023,1)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

sample_data2 = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
        ]

number_finder = re.compile(r"[0-9]|one|two|three|four|five|six|seven|eight|nine")
association = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
        }

def first_digit(s:str) -> int:
    for c in s:
        if c.isdigit():
            return int(c)
    print("No numbers!")
    print(s)

def first_digit2(s:str) -> int:
    c = number_finder.findall(s)[0]
    if c.isdecimal(): return int(c)
    else: return association[c]

def last_digit(s:str) -> int:
    c = number_finder.findall(s,overlapped=True)[-1]
    if c.isdecimal(): return int(c)
    else: return association[c]

def part1(data) -> int:
    nums = ((first_digit(s),first_digit(s[::-1])) for s in data)
    nums = (10*a + b for (a,b) in nums)
    return sum(nums)

def part2(data) -> int:
    nums = ((first_digit2(s),last_digit(s)) for s in data)
    nums = (10*a + b for (a,b) in nums)
    return sum(nums)

ans_ex_1 = part1(sample_data)
assert ans_ex_1 == 142
ans1 = part1(data)
assert ans1 == 55108

ans_ex_2 = part2(sample_data2)
assert ans_ex_2 == 281
#print(ans_ex_2)

ans2 = part2(data)
print(ans2)
