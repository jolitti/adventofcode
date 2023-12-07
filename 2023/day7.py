from aocd.models import Puzzle
from collections import Counter
from functools import cmp_to_key

puzzle = Puzzle(year=2023,day=7)
data = puzzle.input_data.splitlines()
sample_data = puzzle.examples[0].input_data.split("\n")

#--- CONSTANTS
card_power = {c:i for i,c in enumerate("23456789TJQKA")}
card_power2 = {c:i for i,c in enumerate("J23456789TQKA")}
card_types = len(card_power)
hand_type_power = [
        (1,1,1,1,1), # high card
        (2,1,1,1), # pair
        (2,2,1), # two pair
        (3,1,1), # three of a kind
        (3,2), # full house
        (4,1), # four of a kind
        (5,) # five of a kind
    ]
hand_type_power = {h:i for i,h in enumerate(hand_type_power)}

#--- FUNCTIONS
def hand_type(hand) -> tuple[int]:
    char_count = Counter(hand)
    counts = [n for c,n in char_count.items()]
    return tuple(sorted(counts,reverse=True))

assert hand_type("AAAAA") == (5,)
assert hand_type("23332") == (3,2)

def hand_type2(hand) -> tuple[int]:
    # print(hand)
    char_count = Counter(hand)
    jokers = char_count.get("J",0)
    del char_count["J"]
    counts = sorted([n for c,n in char_count.items()],reverse=True)
    if len(counts)==0: counts=[0] # in case of JJJJJ
    counts[0] += jokers # jokers become the most popular card
    return tuple(counts)

assert hand_type2("T55J5") == (4,1)
assert hand_type2("KTJJT") == (4,1)
assert hand_type2("QQQJA") == (4,1)

def lex_greater(hand1,hand2,part=1) -> bool:
    if len(hand1) != len(hand2):
        raise ValueError()
    if hand1 == hand2 == "":
        raise ValueError("Hands shouldn't be equal")
    if hand1[0] == hand2[0]:
        return lex_greater(hand1[1:],hand2[1:],part)

    if part == 1:
        return card_power[hand1[0]] > card_power[hand2[0]]
    else:
        return card_power2[hand1[0]] > card_power2[hand2[0]]

assert lex_greater("AAAAA","K2345")
assert lex_greater("99887","98877")

def beats(hand1,hand2,part=1) -> bool:
    type_function = hand_type if part==1 else hand_type2
    type1,type2 = type_function(hand1),type_function(hand2)
    if type1 == type2:
        return lex_greater(hand1,hand2,part)
    return hand_type_power[type1] > hand_type_power[type2]

assert beats("KK677","KTJJT")
assert beats("QQQJA","32T3K")

# used for custom sorting
def beats_int(hand_bid1,hand_bid2) -> int:
    hand1,_ = hand_bid1
    hand2,_ = hand_bid2
    return -1 if beats(hand1,hand2) else 1

def beats_int2(hand_bid1,hand_bid2) -> int:
    hand1,_ = hand_bid1
    hand2,_ = hand_bid2
    return -1 if beats(hand1,hand2,part=2) else 1
#--- PARTS

def part1(data) -> int:
    data = [line.split() for line in data]
    data = [(hand,int(bid)) for hand,bid in data]

    data = sorted(data,key=cmp_to_key(beats_int),reverse=True)
    total = 0
    for i,(_,bid) in enumerate(data):
        total += bid * (i+1)
    
    return total


def part2(data) -> int:
    data = [line.split() for line in data]
    data = [(hand,int(bid)) for hand,bid in data]

    data = sorted(data,key=cmp_to_key(beats_int2),reverse=True)
    total = 0
    for i,(_,bid) in enumerate(data):
        total += bid * (i+1)
    
    return total

#--- ANSWERS

ans_sample1 = part1(sample_data)
assert ans_sample1 == 6440

ans1 = part1(data)
print(f"Answer to part 1: {ans1}")

ans_sample2 = part2(sample_data)
assert ans_sample2 == 5905

ans2 = part2(data)
print(f"Answer to part 2: {ans2}")
