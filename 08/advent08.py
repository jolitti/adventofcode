from segm_utils import solveSevSeg, translate

with open("08/input08.txt") as file:
    lines = file.readlines()

lines = [l.strip() for l in lines]
lines = [l.split() for l in lines]

sum = 0

for l in lines:
    splitIndex = l.index("|")
    data = l[:splitIndex]
    output = l[splitIndex+1:]

    k = solveSevSeg(data)
    output = [translate(x,k) for x in output]
    #print(*output)
    num = output[0]*1000 + output[1]*100 + output[2]*10 + output[3]
    #print(num)   
    sum+=num

print(sum)

