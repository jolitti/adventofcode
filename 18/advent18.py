from snailpair import Pair, pairAdd
from myutils import getAdventData

def reduceLine(s:str) -> str:
    s = s.replace(",","")
    s = s.replace("]","")
    return s

data = getAdventData("18","input18.txt")
data = [reduceLine(l) for l in data]
pairs = []
for d in data:
    newP = Pair()
    newP.populate(d)
    pairs.append(newP)

""" p = pairs[0]
for pp in pairs[1:]:
    p = pairAdd(p,pp)

print(p)
print(p.magnitude()) """

pairspairs = [(x,y) for x in pairs for y in pairs if x is not y]
sums = [pairAdd(a,b).magnitude() for a,b in pairspairs]
print(max(sums))