from aocd import lines, submit
from more_itertools import windowed

def ord2(c:chr) -> int:
    return ord(c) - ord('a') + 1

def letter_priority(c:chr) -> int:
    ans = 0
    if c.isupper(): ans += ord2('z')
    c = c.lower()
    ans += ord2(c)
    return ans
assert(letter_priority('a')==1 and letter_priority('z')==26)
assert(letter_priority('A')==27 and letter_priority('Z')==52)

def line_score(s:str) -> int:
    items = set(),set()
    slen = len(s)
    for a,b in zip(s[:slen//2],s[slen//2:]):
        items[0].add(a)
        items[1].add(b)
    common = items[0] & items[1]
    # print(s)
    # print(common)
    common = common.pop()
    return letter_priority(common)

def common_over_rows(l:list[str]):
    sets = []
    for _ in l: sets.append(set())
    for string,letterset in zip(l,sets):
        for c in string: letterset.add(c)
    # print(*sets)
    common = set.intersection(*sets).pop()
    return letter_priority(common)

data = lines
ans1 = sum(line_score(l) for l in data)
print(f"First answer: {ans1}") # 8176
# submit(ans1,"a",day=3,year=2022)

ans2 = sum(common_over_rows(window) for window in windowed(data,3,step=3))
print(f"Second answer: {ans2}") # 2689
# submit(ans2,"b",day=3,year=2022)
