from myutils import getAdventData
from bitparser import Packet, hexToBin

data = getAdventData("16","input16.txt")

p = Packet()
p.populate(hexToBin(data[0]))
#print(p)

#print(p.getVersionSum())
print(p.getValue())