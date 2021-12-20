from math import floor, ceil

class Pair:
    value = None
    parent = None
    left, right = None, None

    def __init__(self) -> None:
        self.left, self.right = None,None
        self.value, self.parent = None,None

    def copy(self,parent=None):
        newPair = Pair()
        newPair.parent = parent
        if self.value is not None:
            newPair.value = self.value
        else:
            newPair.left = self.left.copy(self)
            newPair.right = self.right.copy(self)
        return newPair

    def populate(self,seed:str) -> str:
        seed = seed.replace(",","")
        match seed[0]:
            case x if x.isdigit():
                self.value = int(x)
                return seed[1:]
            case "[":
                self.left,self.right = Pair(),Pair()
                self.left.parent,self.right.parent = self,self
                seed = self.left.populate(seed[1:])
                seed = self.right.populate(seed)
                return seed[1:]
                
    def magnitude(self) -> int:
        if self.value is not None: return self.value
        else: return 3*self.left.magnitude() + 2*self.right.magnitude()

    def __str__(self) -> str:
        if self.value is not None: return str(self.value)
        return f"[{str(self.left)},{str(self.right)}]"

    def getLeftMost(self):
        if self.value is not None: return self
        return self.left.getLeftMost()
    def getRightMost(self):
        if self.value is not None: return self
        return self.right.getRightMost()
    def isRoot(self) -> bool: return self.parent is None
    def isLeft(self) -> bool:
        if self.isRoot(): return False
        return self.parent.left is self
    def isRight(self) -> bool:
        if self.isRoot(): return False
        return self.parent.right is self

    def getImmLeft(self):
        if self.isRoot(): return None
        if self.parent.isRoot() and self.isLeft(): return None
        if self.isRight(): return self.parent.left.getRightMost()
        else: return self.parent.getImmLeft()
    def getImmRight(self):
        if self.isRoot(): return None
        if self.parent.isRoot() and self.isRight(): return None
        if self.isLeft(): return self.parent.right.getLeftMost()
        else: return self.parent.getImmRight()

    def willExplode(self,depth:int=0):
        if depth> 4: return self.parent
        if self.value is not None: return None
        e1 = self.left.willExplode(depth+1) 
        e2 = self.right.willExplode(depth+1)
        return e1 if e1 is not None else e2
    def willSplit(self):
        if self.value is not None:
            if self.value > 9: return self
            else: return None
        s1 = self.left.willSplit()
        s2 = self.right.willSplit()
        return s1 if s1 is not None else s2

    def iterate(self):
        exp, spl = self.willExplode(), self.willSplit()
        while exp is not None or spl is not None:
            print(self)
            if exp is not None:
                l,r = exp.left.value,exp.right.value
                if exp.getImmLeft() is not None: exp.getImmLeft().value += l
                if exp.getImmRight() is not None:
                    #print(exp.getImmRight())
                    exp.getImmRight().value += r
                exp.value,exp.left,exp.rigt = 0,None,None
                exp, spl = self.willExplode(), self.willSplit()
                continue
            elif spl is not None:
                val = spl.value/2
                spl.value = None
                spl.left, spl.right = Pair(),Pair()
                spl.left.parent,spl.right.parent = self,self
                spl.left.value, spl.right.value = floor(val),ceil(val)
            exp, spl = self.willExplode(), self.willSplit()
                
def pairAdd(p1:Pair,p2:Pair) -> Pair:
    print(f"{p1} + {p2}")
    p = Pair()
    p.left, p.right = p1.copy(p),p2.copy(p)
    p.iterate()
    return p

if __name__=="__main__":

    pp = Pair()
    pp.populate("[[[[[[1,1]1]1]1]1]1]")
    pp.iterate()
    print(pp)