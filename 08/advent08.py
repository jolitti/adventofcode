lengths = {
    2:[1],
    3:[7],
    4:[0,4],
    5:[2,3,5],
    6:[6,9],
    7:[8]
}
segments = {
    1:"cf",
    2:"acdeg",
    3:"acdfg",
    4:"bcdf",
    5:"abdfg",
    6:"abdefg",
    7:"acf",
    8:"abcdefg",
    9:"abcdfg"
}

def filter(s:str,f:str) -> str:
    toRemove = [c for c in s if c not in f] # chars that don't appear in filter
    for c in toRemove:
        s = s.replace(c,"")
    return s

def filterCand(c:list[str],f:str) -> list:
    pass

with open("08/input08.txt") as file:
    lines = file.readlines()

lines = [l.strip() for l in lines]
lines = [l.split() for l in lines]

for l in lines:
    splitIndex = l.index("|")
    data = l[:splitIndex]
    output = l[splitIndex+1:]

    candidates = ["abcdefg"]*10
    for s in data:
        possibleFits = lengths[len(s)]
        for p in possibleFits:
            candidates[p] = filter(candidates[p],s)
    
    print(candidates)

