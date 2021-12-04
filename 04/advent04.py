from os import SEEK_DATA


class Board:
    nums:list[list[int]] = []
    selected = [[False]*5]*5
    def __init__(self,seed) -> None:
        for l in seed:
            self.nums.append(list(map(int,l.split())))
    
    def insert(self,n:int)-> bool:
        for j,l in enumerate(self.nums):
            if n in l:
                i = l.index(n)
                self.selected[j][i]=True

with open("input04.txt") as file:
    data = file.readlines()

data = [x.strip() for x in data]

nums = list(map(int,data[0].split(",")))

boards = [] # list of lists of lists of int