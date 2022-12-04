from aocd import numbers, submit

def fullycontains(l:list[int]) -> bool:
    a,b,c,d = map(abs,l)
    if a<=c and b>=d: return True
    if c<=a and d>=b: return True
    return False

assert(fullycontains([2,8,3,7]))
assert(fullycontains([2,6,6,6]))
assert(not fullycontains([3,6,4,8]))

def overlaps(l:list[int]) -> bool:
    a,b,c,d = map(abs,l)
    s1,s2 = set(range(a,b+1)), set(range(c,d+1))
    intersection = s1 & s2
    return len(intersection) > 0

ans1 = sum(1 if fullycontains(l) else 0 for l in numbers)
print(f"First answer: {ans1}") # 471
# submit(ans1,"a",day=4,year=2022)

ans2 = sum(1 if overlaps(l) else 0 for l in numbers)
print(f"Second answer: {ans2}") # 888
# submit(ans2,"b",day=4,year=2022)
