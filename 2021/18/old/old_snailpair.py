class Pair:
    value = None
    left, right = None, None

    def __init__(self) -> None:
        self.left, self.right = None,None

    def populate(self,seed:str) -> str:
        #Cut first [
        seed = seed[1:]
        #Populate left element
        match seed[0]:
            case x if x.isdigit():
                self.left = int(x)
                seed = seed[2:]
            case "[":
                self.left = Pair()
                seed = self.left.populate(seed)
            case _:
                raise ValueError("This wasn't supposed to happen")
        #Populate right element
        match seed[0]:
            case x if x.isdigit():
                self.right = int(x)
                seed = seed[2:]
            case "[":
                self.right = Pair()
                seed = self.right.populate(seed)
            case _:
                raise ValueError("Incorrect ending")
        #Cut right bracket
        seed = seed[1:]

        return seed

    def magnitude(self) -> int:
        leftMagn = 3*self.left if isinstance(self.left,int) else 3*self.left.magnitude()
        rightMagn = 2*self.right if isinstance(self.right,int) else 2*self.right.magnitude()
        return leftMagn + rightMagn

    def __str__(self) -> str:
        return f"[ {str(self.left)} , {str(self.right)} ]"

    def copy(self):
        p = Pair()
        if isinstance(self.left,int):
            p.left = self.left
        else:
            p.left = self.left.copy()
        if isinstance(self.right,int):
            p.right = self.right
        else:
            p.right = self.right.copy()
        return p

def pairSum(p1:Pair,p2:Pair) -> Pair:
    p = Pair()
    p.left = p1.copy()
    p.right = p2.copy()
    return p