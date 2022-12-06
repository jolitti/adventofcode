from aocd.models import Puzzle
from aocd import lines
from more_itertools import windowed

def diffchars(s:str) -> bool:
    charset = set()
    length = len(s)
    for c in s:
        charset.add(c)
    return length == len(charset)
assert(diffchars("abcdef"))
assert(not diffchars("aabcdef"))

def first_n_diff(s:str, diff_n:int = 4) -> int:
    for n,window in enumerate(windowed(s,diff_n)):
        n = n+diff_n
        if diffchars(window): return n

puzzle = Puzzle(year=2022,day=6)
data = lines[0]
ans1 = first_n_diff(data)
print(f"First answer: {ans1}")
puzzle.answer_a = ans1

ans2 = first_n_diff(data,14)
print(f"Second answer: {ans2}")
puzzle.answer_b = ans2
