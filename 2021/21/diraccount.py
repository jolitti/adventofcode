from collections import Counter

results = []

for a in [1,2,3]:
    for b in [1,2,3]:
        for c in [1,2,3]:
            results.append(a+b+c)

r = Counter(results)

for x in r.keys():
    print(f"{x}: {r[x]},")