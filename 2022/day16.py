from aocd import lines
from aocd.models import Puzzle
from dataclasses import dataclass
from queue import PriorityQueue

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
    flow: dict[str,int]
    connections: dict[str,set[tuple[str,int]]]
    opened: set[str]
    minutes_left: int
    current_room: str
    score: int = 0
    
    def is_over(self) -> bool:
        return len(self.opened) == len(self.flow) or self.minutes_left<=0

    def new_states(self) -> list["CaveTraversal"]:
        destinations = {}
        queue = PriorityQueue()
        queue.put((0,self.current_room))
        while queue.qsize()>0:
            cost, room = queue.get()
            # print(cost,room)
            if room not in destinations: destinations[room] = cost
            for room2,cost2 in self.connections[room]:
                if room2 not in destinations: 
                    queue.put((cost+cost2,room2))
                    # print(f"  {cost+cost2} {room2}")
        destinations.pop(self.current_room)
        # TODO add new instance per destination
        ans = []
        for room,cost in destinations.items():
            if room in self.opened: continue
            if room not in self.flow: continue
            if cost+1 > self.minutes_left: continue
            next_state = CaveTraversal(
                    self.flow,
                    self.connections,
                    self.opened.union({room}),
                    self.minutes_left - cost - 1,
                    room,
                    self.score + self.flow[room] * (self.minutes_left - cost - 1)
                    )
            ans.append(next_state)
        return ans

def solve(data:list[str]) -> int:
    flow = {}
    connections = {}
    for line in data:
        name,flow_value,conns = split_line(line)
        flow[name] = flow_value
        connections[name] = set()
        for c in conns: connections[name].add((c,1))
    
    print(connections)
    # Graph compression
    for name,value in flow.items():
        if value > 0: continue
        if len(connections[name]) != 2: continue
        (namea,lena),(nameb,lenb) = connections[name]
        connections[namea].remove((name,lena))
        connections[nameb].remove((name,lenb))
        connections.pop(name)
        connections[namea].add((nameb,lena+lenb))
        connections[nameb].add((namea,lena+lenb))
    flow = {name:value for name,value in flow.items() if value!=0}

    finished_explorations = []
    exploqueue = []
    exploqueue.append(CaveTraversal(flow,connections,set(),30,"AA"))

    # TODO exploration
    
    initial_state = CaveTraversal(flow,connections,set(),30,"AA")
    while not initial_state.is_over():
        print(initial_state.current_room,initial_state.score,initial_state.opened)
        initial_state = initial_state.new_states()[0]

# solve(["Valve AA has flow rate=100; tunnels lead to valves BB",
#    "Valve BB has flow rate=1; tunnels lead to valves AA"])

solve(puzzle.example_data.split("\n"))
