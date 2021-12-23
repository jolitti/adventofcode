from myutils import getAdventData
from vector3 import Vector3
from v3utils import extractDistCompatible, fusePointLists,extractCompatibleRotation, extractSufficientAdjustment
from v3utils import getDistances, getAdjustments, getVecDistances, getTranslations
from random import shuffle

data = getAdventData("19","input00.txt")
scanners:list[list[Vector3]] = []

newSc = []
for d in data:
    if d == "": continue
    elif d[1] == "-":
        if len(newSc)>0: scanners.append(newSc) 
        newSc = []
    else:
        a,b,c = map(float,d.split(","))
        newSc.append(Vector3(a,b,c))
scanners.append(newSc)

refScan = scanners[0]
scanners = scanners[1:]
scanpos = [Vector3()] #list of scanner positions
for s in scanners: s.append(Vector3()) # add scanner position

thr = 12
while len(scanners)>0:
    shuffle(scanners)
    s = extractDistCompatible(scanners,refScan,thr)
    if s is None: raise ValueError("No compatible values")
    r = extractCompatibleRotation(s,refScan,thr)
    if r is None: continue
    t = extractSufficientAdjustment(r,refScan,thr)
    if t is None: continue
    scanners.remove(s)
    scanpos.append(t[-1]) #posion of scanner
    t.remove(t[-1])
    refScan = fusePointLists(refScan,t)
    print(len(scanners))

print(len(refScan))
with open("19/output00.txt","w") as file:
    for p in refScan:
        file.write(f"{p.x} {p.y} {p.z}\n")

    file.write("---\n")
    for p in scanpos:
        file.write(f"{p.x} {p.y} {p.z}\n")