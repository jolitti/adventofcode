from math import sqrt
from functools import cache

@cache
def cumDist(a,b):
    dist = abs(a-b)
    return dist*(dist+1)/2

with open("07/input07.txt") as file:
    line = file.readline()
    line.split()
data = list(map(int,line.split(",")))
data = [x-1 for x in data]

n = len(data)
maxNum = max(data)
minNum = min(data)
sqrSum = sum([x*x for x in data])
linSum = sum(data)

""" sqrCosts = [sqrSum - 2*linSum*x +n*x*x for x in range(n)]
indexMin = sqrCosts.index(min(sqrCosts))

minCost = sum([abs(x-indexMin) for x in data])
print(indexMin)
print(minCost) """

costs = [sum([cumDist(x,d) for x in data]) for d in range(n)]
print(int(min(costs)))