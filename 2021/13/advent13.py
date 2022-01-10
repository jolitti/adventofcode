def getPointSet(lines:list[str]) -> set[tuple[int,int]]:
    ans = set()
    for l in lines:
        x,y = map(int,l.split(","))
        ans.add((x,y))
    return ans

def getSizes(l:set[tuple[int,int]]) -> tuple[int,int]:
    maxx = max([p[0] for p in l])
    maxy = max([p[1] for p in l])
    return (maxx+1,maxy+1)

def fold(pts:set[tuple[int,int]],f:tuple[str,int]) -> set[tuple[int,int]]:
    #TODO
    i = 0 if f[0]=="x" else 1
    other = 1-i
    pos = f[1]
    ans = set()
    for p in pts:
        if p[i] > pos:
            newPos = pos -(p[i] - pos)
            newTuple = (newPos,p[1]) if f[0]=="x" else (p[0],newPos)
            ans.add(newTuple)
        else:
            ans.add(p)
    return ans

with open("13/input13.txt") as file:
    data = file.readlines()
data = [x.strip() for x in data]

split = data.index("")
pts = data[:split]
folds = data[split+1:]

points = getPointSet(pts)
sizex,sizey = getSizes(points)

for i,desc in enumerate(folds):
    s = desc.split()[-1]
    dir, pos = s.split("=")
    pos = int(pos)
    folds[i] = (dir,pos)

for f in folds:
    points = fold(points,f)
    sizex,sizey = getSizes(points)

#points = fold(points,folds[1])

for j in range(sizey):
    for i in range(sizex):
        if (i,j) in points:
            print("#",end="")
        else: print(".",end="")
    print()

print(len(points))
    