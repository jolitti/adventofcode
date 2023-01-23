from aocd import lines
from aocd.models import Puzzle
from dataclasses import dataclass
from queue import SimpleQueue

puzzle = Puzzle(year=2022,day=16)

def split_line(s:str) -> tuple[str,int,set[str]]:
    s = s.replace(",","")
    s = s.replace(";","")
    s = s.replace("rate=","")
    words = s.split(" ")
    return words[1], int(words[4]), set(words[9:])
assert split_line(lines[0]) == ("SY",0,{"GW","LW"})

@dataclass
class CaveTraversal:
    opened: set[str]
    minutes_left: int
    current_room: str
    score: int = 0
    
    def is_over(self,flow:dict[str,int]) -> bool:
        return len(self.opened) == len(flow) or self.minutes_left<=0

    def new_states(self,flow:dict[str,int],connections:dict[str,tuple[str,int]]) -> list["CaveTraversal"]:
        if self.is_over(flow): return [self]
        ans = []
        if self.current_room in flow and self.current_room not in self.opened:
            ans.append(CaveTraversal(
                self.opened.copy() or {self.current_room},
                self.minutes_left-1,
                self.current_room,
                (self.score + (self.minutes_left-1)*flow[self.current_room])
                ))
        for (destination,cost) in connections[self.current_room]:
            if cost > self.minutes_left: continue
            ans.append(CaveTraversal(self.opened.copy(),self.minutes_left-cost,destination,self.score))
        return ans

    

def solve(data:list[str]) -> int:
    flow = {}
    connections = {}
    for line in data:
        name,flow_value,conns = split_line(line)
        flow[name] = flow_value
        connections[name] = set()
        for c in conns: connections[name].add((c,1))
    flow = {name:value for name,value in flow.items() if value!=0}

    finished_explorations = []
    exploqueue = SimpleQueue()
    exploqueue.put(CaveTraversal(set(),30,"AA"))
    while not exploqueue.empty():
        explo = exploqueue.get()
        print(explo.minutes_left)
        if explo.is_over(flow): finished_explorations.append(explo)
        for ex in explo.new_states(flow,connections): exploqueue.put(ex)

    values = [ex.score for ex in finished_explorations]
    print(max(values))

solve(puzzle.example_data.split("\n"))
