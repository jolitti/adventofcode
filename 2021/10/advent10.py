from chunkstack import ChunkStack

with open("10/input10.txt") as file:
    data = file.readlines()
data = [x.strip() for x in data]

lines = [ChunkStack(x) for x in data]
#points = [x.val for x in lines if x.val>=0]
#print(*points)
#print(sum(points))

incompleteLines = [x for x in lines if x.val == 0]
completePoints = [x.complete() for x in incompleteLines]
completePoints.sort()
#print(*completePoints)

mid = len(completePoints)//2
print(completePoints[mid])