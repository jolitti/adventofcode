from myutils import getAdventData
from detdice import DetDie

def addWrap(a,b) -> int:
    ans = a+b
    return (ans-1)%10 + 1

data = getAdventData("2021/21","input21.txt")

pos1 = int(data[0].split()[-1])
pos2 = int(data[1].split()[-1])
print(f"{pos1} {pos2}")
point1, point2 = 0,0

die = DetDie()

while point1<1000 and point2<1000:
    for _ in range(3): pos1 = addWrap(pos1,die.getNum())
    point1 += pos1
    if point1>=1000: break

    for _ in range(3): pos2 = addWrap(pos2,die.getNum())
    point2 += pos2

    #print(f"{pos1} {pos2}")



print(f"{point1} {point2}")
print(min(point1,point2)*die.iters)