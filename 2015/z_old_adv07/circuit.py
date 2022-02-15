from dataclasses import dataclass

class Gate:
    """
    Abstract gate, to be derived
    """
    def result(self) -> int:
        pass

@dataclass
class Literal (Gate):
    value: int
    def result(self) -> int:
        print("literal",self.value)
        return self.value

@dataclass
class Assign (Gate):
    reference: str
    def result(self) -> int:
        print("assign",self.reference)
        return wires[self.reference].result()

@dataclass
class And (Gate):
    a:str
    b:str
    def result(self) -> int:
        print("and",a,b)
        if a.isnumeric() and b.isnumeric(): return int(a) & int(b)
        if a.isnumeric(): return int(a) & wires[self.b].result()
        if b.isnumeric(): return int(b) & wires[self.a].result()
        return wires[self.a].result() & wires[self.b].result()

@dataclass
class Or (Gate):
    a:str
    b:str
    def result(self) -> int:
        print("or",a,b)
        return wires[self.a].result() | wires[self.b].result()

@dataclass
class Not (Gate):
    source: str
    def result(self) -> int:
        print("not",self.source)
        return ~wires[self.source].result()
    
@dataclass
class Lshift (Gate):
    source: Gate
    amount: int
    def result(self) -> int:
        print("lshift",self.source,self.amount)
        return wires[self.source].result()<<self.amount

@dataclass
class Rshift (Lshift):
    def result(self) -> int:
        print("rshift",self.source,self.amount)
        return wires[self.source].result()>>self.amount

with open("input.txt") as file:
    data = file.readlines()
data = [d.strip() for d in data]

wires = dict() #string -> Gate

for d in data:
    match d.split():
        case [a,_,c]:
            if (a.isnumeric()): wires[c] = Literal(int(a))
            else: wires[c] = Assign(a[:])
        case [a,op,b,_,c]:
            match op:
                case "AND": wires[c] = And(a[:],b[:])
                case "OR": wires[c] = Or(a[:],b[:])
                case "LSHIFT": wires[c] = Lshift(a[:],int(b))
                case "RSHIFT": wires[c] = Rshift(a[:],int(b))
                case _: raise Exception("Invalid operation")

print(wires["a"].result())