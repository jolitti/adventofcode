from aocd import lines
from aocd.models import Puzzle
from more_itertools import windowed

puzzle = Puzzle(year=2022,day=11)

assert(1501//3==500)
class Monkey:
    def __init__(self,initdata:list[str],worrydiv3=True):
        self.throws = 0
        self.worrydiv3 = worrydiv3
        initdata = initdata[1:-1]
        initdata = [l.strip() for l in initdata]
        items = initdata[0].removeprefix("Starting items: ")
        self.items = list(map(int,items.split(", ")))
        self.op = initdata[1].removeprefix("Operation: new =")
        self.divi = int(initdata[2].removeprefix("Test: divisible by "))
        self.dest_true = int(initdata[3].removeprefix("If true: throw to monkey "))
        self.dest_false = int(initdata[4].removeprefix("If false: throw to monkey "))
    
    def reference_monkey(self,monkeys:list["Monkey"]):
        self.dest_true = monkeys[self.dest_true]
        self.dest_false = monkeys[self.dest_false]

    def iterate(self, div=3):
        while len(self.items)>0:
            item = self.items.pop(0)
            old = item
            item = eval(self.op)
            if self.worrydiv3: item = item//3
            else: item = item%div
            if item % self.divi == 0:
                self.dest_true.items.append(item)
            else:
                self.dest_false.items.append(item)
            self.throws += 1
 

with open("samples/sample11") as file:
    sampledata = file.readlines()

monkeys = list(Monkey(l) for l in windowed(lines,7,step=7))
for m in monkeys: m.reference_monkey(monkeys)
for _ in range(20):
    for m in monkeys:
        m.iterate()

throws = [m.throws for m in monkeys]
throws.sort(reverse=True)

ans1 = throws[0]*throws[1]
print(f"First answer: {ans1}") # 54036
puzzle.answer_a = ans1

monkeys2 = list(Monkey(l,False) for l in windowed(lines,7,step=7))
for m in monkeys2: m.reference_monkey(monkeys2)
# Insight in the input data revealed all the division criteria are prime numbers
# So we can reduce the worry levels by their product, since this won't
# change their divisibility by those numbers
div = 1
for m in monkeys2: div *= m.divi
for i in range(10000):
    # print(i)
    for m in monkeys2: m.iterate(div)

throws2 = [m.throws for m in monkeys2]
throws2.sort(reverse=True)
ans2 = throws2[0] * throws2[1]
print(f"Second answer: {ans2}") # 13237873355
puzzle.answer_b = ans2
