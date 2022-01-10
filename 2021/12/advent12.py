def canVisitTwice(c:str,path:list[str]) -> bool:
    if c=="start" or c=="end": return False
    for s in path:
        if s.islower() and path.count(s)>1: return False
    return True

def link(pair:str,links:dict,small:set,big:set):
    a,b = pair.split("-")
    small.add(a) if a.islower() else big.add(a)
    small.add(b) if b.islower() else big.add(b)
    alinks = links.get(a,[])
    alinks.append(b)
    links[a] = alinks
    blinks = links.get(b,[])
    blinks.append(a)
    links[b] = blinks

def getPaths(p:str,prev:list[str]) -> list[list[str]]:
    if p=="end": return [prev+[p]]
    ans = []
    for l in links[p]:
        if l in small and l in prev and not canVisitTwice(l,prev+[p]): continue
        ans += getPaths(l,prev+[p])
    return ans

with open("12/input12.txt") as file:
    data = file.readlines()
data = [d.strip() for d in data]

links,small,big = {},set(),set()

[link(l,links,small,big) for l in data]

paths = getPaths("start",[])
print(len(paths))

for p in paths:
    d = {x:p.count(x) for x in p}
    #print(d)