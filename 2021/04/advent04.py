from os import SEEK_DATA
from typing import Tuple

class Board:
    nums:list[list[int]] = []
    selected = [[False]*5]*5
    def __init__(self,seed:str) -> None:
        self.selected = []
        for _ in range(5):
            self.selected.append([False]*5)
        self.nums = []
        for l in seed:
            l.strip()
            if l=="": continue
            self.nums.append(list(map(int,l.split())))
            if len(self.nums)>=5:break

    def findBingo(self) -> Tuple[int,str]|None:
        for i in range(5):
            ret = True
            for b in self.selected[i]:
                if ret and not b: 
                    ret = False
                    break
            if ret: return (i,"row")
        for i in range(5):
            ret = True
            for b in self.selected:
                if ret and not b[i]: 
                    ret = False
                    break
            if ret: return (i,"col")
        return None

    def setTrue(self,n:int):
        for j in range(5):
            for i in range(5):
                if self.nums[j][i] == n:
                    self.selected[j][i] = True
                    return

    def insert(self,n:int)-> bool:
        self.setTrue(n)
        if self.findBingo() is not None: return True
        else: return False

    def printBoard(self):
        print(f"{len(self.nums)} lines")
        for l in self.nums:
            print(*l)
    
    def printSelected(self):
        for l in self.selected:
            print(*l)
    
    def sumOfUnmarked(self)->int:
        return sum([self.nums[j][i] for j in range(5) for i in range(5) if not self.selected[j][i]])

def process(boards,nums) -> tuple[Board,int]:
    for n in nums:
        for b in boards:
            if b.insert(n): return (b,n)

def processLast(boards,nums) -> tuple[Board,int]:
    for n in nums:
        toRemove = []
        for b in boards:
            if b.insert(n): 
                if len(boards) == 1:
                    return (b,n)
                toRemove.append(b)
        [boards.remove(b) for b in toRemove]



file = None
try:
    file = open("input04.txt")
except:
    file = open("04/input04.txt")

data = file.readlines()
data = [x.strip() for x in data]
nums = list(map(int,data[0].split(",")))
data = data[1:]

boards = []

for _ in range(len(data)//6):
    seed = data[:6]
    data = data[6:]
    
    boards.append(Board(seed))

b,n = processLast(boards,nums)

print(b.sumOfUnmarked()*n)