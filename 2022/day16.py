from aocd import lines
from aocd.models import Puzzle
from queue import PriorityQueue
from itertools import permutations
from more_itertools import windowed

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
        # print(found)
        # print(start_room)
        visited = set()
        queue = PriorityQueue()
        queue.put((0,start_room))
        while queue.qsize() != 0:
            cost,destination = queue.get()
            if destination not in visited:
                found[(start_room,destination)] = cost
                visited.add(destination)
                for new_room_name,cost2 in conns[destination]:
                    if new_room_name == start_room: continue
                    if new_room_name in visited: continue
                    queue.put((cost+cost2,new_room_name))
                    # print(f"  Putting {new_room_name}")

    return found

def find_best_moves(
        past_moves: list[str],
        available_rooms: set[str],
        current_score: int,
        time_remaining: int,
        room_flows: dict[str,int],
        traversal_costs: dict[tuple[str,str],int]
        ) -> tuple[list[str],int]: # following moves, score

    current_room = past_moves[-1]
    if time_remaining <= 0: return [],current_score
    if len(available_rooms) == 1:
        (only_move,) = available_rooms
        travcost = traversal_costs[(current_room,only_move)]
        if travcost + 1 > time_remaining:
            raise ValueError("Not enough time to travel to only room!")
        return [only_move], current_score + room_flows[only_move] * (time_remaining - travcost - 1)

    maxmoves,maxscore = [], current_score
    for destination in available_rooms:
        traveltime = traversal_costs[(current_room,destination)]
        if traveltime+1 >= time_remaining: continue
        added_score = room_flows[destination] * (time_remaining - traveltime - 1)
        newmoves,newscore = find_best_moves(
                past_moves + [destination],
                available_rooms.difference({destination}),
                current_score + added_score,
                time_remaining - traveltime - 1,
                room_flows,
                traversal_costs
                )
        if newscore > maxscore:
            maxmoves,maxscore = [destination]+newmoves,newscore

    return maxmoves,maxscore


def solve(data:list[str]) -> int:
    flow, conns = get_graph(data)
    assert len(flow)+1 == len(conns)
    costs = get_traversal_costs(conns)
    rooms = {room for room,_ in flow.items()}

    moves,score = find_best_moves(["AA"],rooms,0,30,flow,costs)
    #print(moves)
    #costlist = []
    #for a,b in windowed(["AA"]+moves,2):
    #    costlist.append(costs[(a,b)] + 1)
    #print(costlist,sum(costlist))

    return score

assert solve(puzzle.example_data.split("\n")) == 1651
ans1 = solve(lines) # 2166 too low 2200 too high !! 2181 good candidate -> CORRECT
print(f"First answer: {ans1}")
# puzzle.answer_a = ans1  For some reason this breaks aocd
