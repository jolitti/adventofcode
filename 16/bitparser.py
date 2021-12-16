from math import prod

def hexToBin(h:str) -> str:
    return bin(int("1"+h,16))[3:]


def get3bit(s:str) -> tuple[int,str]:
    ans = int(s[:3],2)
    return ans,s[3:]
def getNbit(s:str,n:int) -> tuple[int,str]:
    ans = int(s[:n],2)
    return ans,s[n:]

def hasNextNybble(s:str) -> bool:
    return s[0]=="1"
def getNybble(s:str) -> tuple[str,str]:
    ans = s[1:5]
    return ans,s[5:]

def getLitValue(s:str) -> tuple[int,str]:
    nybs = ""
    while hasNextNybble(s):
        n, s = getNybble(s)
        nybs += n
    n,s = getNybble(s)
    nybs += n
    return int(nybs,2),s

class Packet:
    value: int|list
    type: int
    version: int

    def __init__(self) -> None:
        #print("Initializing new packet")
        pass

    def populate(self,seed:str) -> str:
        bin = seed
        #bin = hexToBin(seed)
        self.version, bin = get3bit(bin)
        self.type, bin = get3bit(bin)
        
        match self.type:
            case 4:
                self.value,bin = getLitValue(bin)

            case _:
                self.value,bin = getMultiPacket(bin)

        return bin

    def getValue(self) -> int:
        if self.type == 4: return self.value
        valueList = [x.getValue() for x in self.value]
        match self.type:
            case 0:
                return sum(valueList)
            case 1:
                return prod(valueList)
            case 2:
                return min(valueList)
            case 3:
                return max(valueList)
            case 5:
                return 1 if valueList[0] > valueList[1] else 0
            case 6:
                return 1 if valueList[0] < valueList[1] else 0
            case 7:
                return 1 if valueList[0] == valueList[1] else 0
            case _:
                raise ValueError(f"Error! Unexpected opType {self.type}")
                

    def getVersionSum(self) -> int:
        ans = self.version
        if isinstance(self.value,int): return ans
        else: return ans + sum([v.getVersionSum() for v in self.value])

    def strStructure(self) -> list[str]:
        ans = []
        ans.append(f"version: {self.version}, type: {self.type}, value: ")
        if isinstance(self.value,int):
            ans[0]+=f"{self.value}"
            return ans
        else:
            recurs = []
            for v in self.value:
                recurs += v.strStructure()
            recurs = ["| "+x for x in recurs]
            ans += recurs
            return ans

    def __str__(self):
        return "\n".join(self.strStructure())

def getPacketsByBits(s:str,n:int) -> tuple[list[Packet],str]:
    targetLen = len(s)-n
    ans = []
    while len(s)>targetLen:
        newPack = Packet()
        s = newPack.populate(s)
        ans.append(newPack)
    return ans,s

def getPacketByNumber(s:str,n:int) -> tuple[list[Packet],str]:
    ans = []
    for i in range(n):
        newPack = Packet()
        s = newPack.populate(s)
        ans.append(newPack)
    return ans,s

def getMultiPacket(s:str) -> tuple[list[Packet],str]:
    mode = int(s[0])
    s = s[1:]
    #print(s)
    match mode:
        case 1:
            packNum,s = getNbit(s,11)
            ans,s = getPacketByNumber(s,packNum)
            return ans,s
        case 0:
            bitsNum,s = getNbit(s,15)
            ans,s = getPacketsByBits(s,bitsNum)
            return ans, s
        case _:
            raise ValueError("Error! Not a bit")

#print(hexToBin("38006F45291200"))