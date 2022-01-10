def hexToBin(h:str) -> str:
    return bin(int(h,16))[2:]
def toDec(b:str) -> int:
    return int(b,2)
def readLiteral(b:str) -> tuple[int,str]:
    hw = b[:5]
    nybs = ""
    while hw[0] == "1":
        b = b[5:]
        nybs = nybs + hw[1:]
        hw = b[:5]
    nybs = nybs + hw[1:]
    #print(nybs)
    ans = toDec(nybs)
    return ans,b

class Packet:
    pass

class Packet:
    version:int
    type:int
    bin:str
    value: int|list[Packet]

    def __init__(self,seed:str) -> None:
        self.bin = toBin(seed)
        self.version = toDec(self.bin[:3])
        self.type = toDec(self.bin[3:6])
        match self.type:
            case 4:
                self.value, _ = readLiteral(self.bin[6:])
            case _:
                pass

    def printSelf(self):
        print(self.version)
        print(self.type)
        print(self.value)