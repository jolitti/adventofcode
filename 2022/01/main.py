from aocd import get_data

data = get_data(day=1,year=2022).split("\n\n")
data = [list(map(int,l.split())) for l in data]

ans1 = max(sum(d) for d in data)
print(f"First answer: {ans1}")

sums = [sum(d) for d in data]
sums.sort(reverse=True)

ans2 = sum(sums[0:3])
print(f"Second answer: {ans2}")
