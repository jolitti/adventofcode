from pos import Pos

target1 = (20,30,-10,-5)
target2 = (288,330,-96,-50)

count = 0
for i in range(331):
    for j in range(-110,110):
        p = Pos((i,j))
        if p.willHit(target2): count += 1

print(count)