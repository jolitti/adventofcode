from rizomath.cuboid import Cuboid, str_to_cb
# on x=44376..68804,y=-48705..-15357,z=24716..43885

def cubo_from_line(s:str) -> Cuboid:
    l = s.split()
    value = True if l[0]=="on" else False
    source = l[1]
    for c in ["x=","y=","z="]:
        source = source.replace(c,"")
    source = source.replace(","," ")
    return str_to_cb(source,value)

def overlaps(l:list[Cuboid], c:Cuboid) -> Cuboid | None:
    for list_cubo in l:
        overlap = list_cubo & c
        if overlap is not None: return list_cubo
    return None


with open("input22.txt") as file:
    data = file.read().splitlines()
cubos = []

for i,d in enumerate(data):
    print(i)
    new_cubo = cubo_from_line(d)
    print(d, " ", new_cubo.value)
    #while (overlapping:=overlaps(cubos,new_cubo)) is not None:
    while overlaps(cubos,new_cubo) is not None:
        overlapping = overlaps(cubos,new_cubo)
        #print(f"{overlapping=}")
        #print(new_cubo)
        cubos.remove(overlapping)
        cubos += overlapping - new_cubo
    cubos.append(new_cubo)

print(sum(c.volume() for c in cubos if c.value==True))
print(sum(c.volume() for c in cubos if c.value==False))
print(sum(c.volume() for c in cubos))
print(f"{len(cubos)=}")
