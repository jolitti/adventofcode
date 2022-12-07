from aocd import lines
from aocd.models import Puzzle

puzzle = Puzzle(year=2022,day=7)

data = list(lines)
data.append("end")
data_iter = iter(data)
path = [] # Current sequence of directory exploration

class Directory:
    name: str
    subdirs: list["Directory"]
    files: list[tuple[str,int]]

    def __init__(self,name:str):
        self.name = name
        self.subdirs = []
        self.files = []

    def file_weight(self) -> int:
        return sum(map(lambda pair: pair[1], self.files))

sample_dir = Directory("sus")
sample_dir.files = [("a",100),("b",200)]
assert(sample_dir.file_weight() == 300)

while True:
    line = next(data_iter)
    # check end of sequence
    if line=="end": break
    
    line = line.split(" ")
    # check command
    if line[0] == "$":
        line = line[1:]
        match line:
            case ["cd",destination]:
                print(destination)
    # data (file/directory) insertion
    else:
        pass
