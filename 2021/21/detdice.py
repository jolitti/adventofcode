class DetDie:
    num = 1
    iters = 0

    def __init__(self) -> None:
        self.num = 1
        self.iters = 0
    
    def getNum(self) -> int:
        self.iters += 1
        oldNum = self.num
        self.num += 1
        if self.num > 100: self.num = 1

        #print(oldNum)

        return oldNum