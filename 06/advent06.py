class Fish:
    timer:int
    def __init__(self,d:int=8) -> None:
        self.timer = d
    def iterate(self,l:list) -> None:
        self.timer-=1
        if self.timer < 0:
            self.timer = 6
            l.append(Fish())

class Sea:
    timers:list[int] # list of fish with (index) days remaining
    def __init__(self,seed:list[int]) -> None:
        self.timers = [0]*9
        for s in seed:
            self.timers[s]+=1
    def iterate(self):
        newTimers = [0]*9
        for i,f in enumerate(self.timers):
            if i==0:
                newTimers[8]+=f
                newTimers[6]+=f
            else:
                newTimers[i-1]+=f
        self.timers = newTimers

with open("06/input06.txt") as file:
    data = file.readline()
    data.strip()

nums = list(map(int,data.split(",")))

s = Sea(nums)

for i in range(256):
    s.iterate()

print(sum(s.timers))