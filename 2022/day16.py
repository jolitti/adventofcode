from aocd import lines
from aocd.models import Puzzle
from queue import PriorityQueue

puzzle = Puzzle(year=2022,day=16)

def split_line(s:str) -> tuple[str,int,set[str]]:
    s = s.replace(",","")
    s = s.replace(";","")
    s = s.replace("rate=","")
    words = s.split(" ")
    return words[1], int(words[4]), set(words[9:])
assert split_line(lines[0]) == ("SY",0,{"GW","LW"})

def get_graph(rooms:list[str]) -> tuple[dict,dict]:
    flow = {}
    connections = {}
    for line in rooms:
        name,flow_value,conns = split_line(line)
        flow[name] = flow_value
        connections[name] = set()
        for c in conns: connections[name].add((c,1))
    
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
    
    flow = {name:value for name,value in flow.items() if value>0}

    return flow,connections

def get_traversal_costs(conns:dict[str,set[str,int]]) -> dict[tuple[str,str],int]:
    found = {}
    rooms = {room for room,_ in conns.items()}
    for start_room in rooms:
        queue = PriorityQueue()
        for adjacent,dist in conns[start_room]:
            queue.put((dist,adjacent))
        while queue.qsize() != 0:
            cost,destination = queue.get()
            if (start_room,destination) not in found:
                found[(start_room,destination)] = cost
                for new_room_name,cost2 in conns[destination]:
                    if new_room_name == start_room: continue
                    queue.put((cost+cost2,new_room_name))

    return found

def solve(data:list[str]) -> int:
    flow, conns = get_graph(data)
    assert len(flow)+1 == len(conns)
    costs = get_traversal_costs(conns)
    print(costs)

    return 0

print(solve(puzzle.example_data.split("\n")))
