lengths = [2,3,4,7]

with open("08/input08.txt") as file:
    lines = file.readlines()

lines = [l.strip() for l in lines]
lines = [l.split() for l in lines]
lines2 = [l[l.index("|")+1:] for l in lines]
inputs = [l[:l.index("|")] for l in lines]

""" sum = 0
for l in lines:
    for s in l:
        if len(s) in lengths: sum += 1

print(sum) """

for x,i in enumerate(inputs):
    sortd = sorted(i,key=len)
    print(*[len(x) for x in sortd])