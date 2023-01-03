from aocd import lines,numbers
from aocd.models import Puzzle

puzzle = Puzzle(year=2022,day=16)

class Cave:
    rooms:dict[str,"Room"]
    def __init__(self,l:list[str]):
        self.rooms = {}
        for s in l:
            name = s.split(" ")[1]
            self.rooms[name] = Room(s,self)
    def testdata(self):
        # Starting room links to more than two rooms
        # for name,r in self.rooms.items():
            # if r.flow == 0: assert len(r.links)==2,f"Room {name} links >2 rooms"
        # print("All rooms with flow 0 link between others")
        pass
    def collapse(self):
        collapsed = set()
        for name,r in self.rooms.items():
            if r.collapse():
                collapsed.add(name)
        print(collapsed)

class Room:
    flow:int
    opened: bool
    links:dict[str,int]
    cave:Cave
    def __init__(self,s:str,cave:Cave):
        self.opened = False
        self.links = {}
        self.cave = cave
        s = s[9:] # Strip "Valve <name> "
        s = s.replace(";","")
        s = s.replace(",","")
        s = s.removeprefix("has flow rate=")
        slist = s.split(" ")
        self.flow = int(slist[0])
        slist = slist[5:]
        for r in slist:
            self.links[r] = 1
        # print(self)
    def __str__(self) -> str:
        op = "Opened" if self.opened else "Closed"
        return f"{op} room with flow {self.flow} linked with {self.links}"
    def collapse(self) -> bool:
        if self.flow<=0 and len(self.links.items())==2:
            (namea,lena),(nameb,lenb) = self.links.items()
            self.cave.rooms[namea].links[nameb] = lena+1
            self.cave.rooms[nameb].links[namea] = lenb+1
            return True
        return False

cave = Cave(lines)
cave.testdata()
cave.collapse()
