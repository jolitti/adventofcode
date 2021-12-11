dirs = [(x,y) for x in [-1,0,1] for y in [-1,0,1] if (x,y)!=(0,0)]

def findFlashes(nums:list[list[int]],filter:list[list[bool]]) -> list[tuple[int,int]]:
    sizex,sizey = len(nums[0]),len(nums)
    ans = [(x,y) for x in range(sizex) for y in range(sizey) if nums[y][x]>9 and filter[y][x]==False]
    return ans

class OctoBoard:
    nums:list[list[int]]
    flashes:int
    sizex:int
    sizey:int

    def isInBoard(self,x,y) -> bool:
        return 0<=x<self.sizex and 0<=y<self.sizey

    def __init__(self,seed:list[str]) -> None:
        self.nums = []
        self.flashes = 0
        self.sizex, self.sizey = len(seed[0]),len(seed)
        for s in seed:
            self.nums.append([int(x) for x in s])

    def iterate(self) -> int:
        flashed = [[False for _ in l] for l in self.nums]
        flashesInThisIter = 0
        for l in self.nums:
            for i,x in enumerate(l):
                l[i] = x+1
        toFlash = findFlashes(self.nums,flashed)
        while len(toFlash)>0:
            for f in toFlash:

                x,y = f
                flashed[y][x] = True
                self.flashes += 1
                flashesInThisIter += 1
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if self.isInBoard(nx,ny): self.nums[ny][nx] += 1

            toFlash = findFlashes(self.nums,flashed)
        flashed = [[False for _ in l] for l in self.nums]
        hasFlashed = findFlashes(self.nums,flashed)
        for x,y in hasFlashed:
            self.nums[y][x] = 0
        return flashesInThisIter

    def iterateTilAllFlash(self) -> int:
        i = 0
        while self.iterate() < self.sizex * self.sizey: i+= 1
        return i

    def printNums(self):
        for l in self.nums:
            [print(x,end="") for x in l]
            print()
