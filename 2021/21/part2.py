from myutils import getAdventData
from universe import results,getWins

data = getAdventData("2021/21","input21.txt")

pos1 = int(data[0].split()[-1]) - 1
pos2 = int(data[1].split()[-1]) - 1

print(f"{pos1} {pos2}")

#print((getWins(pos1,pos2,0,0,1)))

print(max(getWins(pos1,0,pos2,0,1)))