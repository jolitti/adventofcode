from typing import Union
from myBinTree import BinNode
from math import floor,ceil

def chopOff(s:str) -> tuple[str,str]:
    return s[0],s[1:]

class Pair(BinNode):
    left:"Pair"
    right:"Pair"

    def addLeft(self, val=None) -> "Pair":
        newPair = Pair(val,self)
        self.left = newPair
        return newPair
    def addRight(self, val=None) -> "Pair":
        newPair = Pair(val,self)
        self.right = newPair
        return newPair
    def addBoth(self,val1=None,val2=None) -> tuple["Pair","Pair"]:
        return self.addLeft(val1),self.addRight(val2)

    # seed = left sqr brackets and single digits
    def populate(self,seed:str) -> str:
        ch, seed = chopOff(seed)

        if ch.isdigit():
            self.value = int(ch)
        else:
            self.addBoth()
            seed = self.left.populate(seed)
            seed = self.right.populate(seed)

        self.calcDepth()
        return seed

    def magnitude(self) -> int:
        if self.value is not None: return self.value
        else: return 3*self.left.magnitude() + 2*self.right.magnitude()
    
    def explode(self) -> None:
        l,r = self.left.value, self.right.value
        
        nl,nr = self.getNextLeft(),self.getNextRight()
        if nl is not None: nl.value = nl.value + l
        if nr is not None: nr.value = nr.value + r
        self.left = None
        self.right = None
        self.value = 0

    def explodingPair(self) -> Union["Pair",None]:
        self.calcDepth()
        leaves = self.getAllLeaves()
        for l in leaves:
            if l.depth >= 5: return l.parent
        return None

    def splittingNumber(self) -> Union["Pair",None]:
        self.calcDepth()
        leaves = self.getAllLeaves()
        for l in leaves:
            if l.value > 9: return l
        return None

    def splitNumber(self):
        l,r = floor(self.value/2), ceil(self.value/2)
        self.addBoth(l,r)
        self.value = None

    def copy(self) -> "Pair":
        n = Pair(self.value)
        if self.left is not None:
            n.left = self.left.copy()
            n.left.parent = n
        if self.right is not None:
            n.right = self.right.copy()
            n.right.parent = n
        return n



def pairAdd(p1:Pair,p2:Pair) -> Pair:
    n = Pair()
    n.left, n.right = p1.copy(),p2.copy()
    n.left.parent,n.right.parent = n,n
    
    while True:
        expl = n.explodingPair()
        if expl is not None:
            expl.explode()
            continue
        spl = n.splittingNumber()
        if spl is not None:
            spl.splitNumber()
            continue
        else: break

    return n