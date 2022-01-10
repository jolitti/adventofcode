""" def iterate(s:str,r:dict[str,str]) -> str:
    pairs = zip(s,s[1:])
    pairs = ["".join(x) for x in pairs]
    for i,p in enumerate(pairs):
        if p in r: pairs[i] = r[p]
    out = pairs[0]
    for p in pairs[1:]:
        out += p[1:]
    return out """

def iterate2(pairs:dict[str,int],rules:dict[str,tuple[str,str]]) -> dict[str,int]:
    newPairs = dict()
    for p in pairs:
        a,b = rules[p]
        n = pairs[p]
        na, nb = newPairs.get(a,0),newPairs.get(b,0)
        newPairs[a],newPairs[b] = na+n,nb+n
    return newPairs


with open("14/input14.txt") as file:
    data = file.readlines()
data = [x.strip() for x in data]


from collections import Counter
poly = data[0]
poly = ["".join(x) for x in zip(poly,poly[1:])]
poly = Counter(poly)

rls = data[2:]
rls = [x.split(" -> ") for x in rls]
for i,r in enumerate(rls):
    a,b = r
    rls[i] = (a,a[0]+b,b+a[1])
rules = {a:(b,c) for a,b,c in rls}


for i in range(40):
    poly = iterate2(poly,rules)

letters = {}

for p in poly:
    l = p[1]
    n = letters.get(l,0)
    letters[l] = n + poly[p]

letters[data[0][0]] += 1

print(poly)
print(letters)

maxL, minL = max(letters,key=letters.get), min(letters,key=letters.get)
print(letters[maxL]- letters[minL])