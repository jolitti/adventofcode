from aocd import lines
from aocd.models import Puzzle

puzzle = Puzzle(year=2022,day=7)
TOTAL_SPACE = 70000000
FREE_SPACE_NEEDED = 30000000

data = list(lines)
data.append("end")
data_iter = iter(data)

class Directory:
    name: str
    subdirs: list["Directory"]
    files: list[tuple[str,int]]
    parent_dir: "Directory"

    def __init__(self,name:str,parent:"Directory"=None):
        self.name = name
        self.parent_dir = parent
        self.subdirs = []
        self.files = []

    def file_weight(self) -> int:
        return sum(map(lambda pair: pair[1], self.files))
    def total_weight(self) -> int:
        return sum(subdir.total_weight() for subdir in self.subdirs) + self.file_weight()
    def add_file(self,name:str,weight:int):
        self.files.append((name,weight))
    def add_subdirectory(self,name:str) -> "Directory":
        newdir = Directory(name,self)
        self.subdirs.append(newdir)
        return newdir
    def has_subdirectory(self,name:str) -> bool:
        any(sd.name==name for sd in self.subdirs)
    def print_contents(self,level:int=0):
        print(" "*level*2,self.name)
        for f in self.files:
            print(" "*level*2,f[0],f[1])
        for d in self.subdirs:
            d.print_contents(level+1)
    def fetch_dirs_below(self,threshold:int) -> list["Directory"]:
        ans = []
        if self.total_weight() <= threshold: ans.append(self)
        for d in self.subdirs:
            ans += d.fetch_dirs_below(threshold)
        return ans
    def smallest_dir_above(self,threshold:int):
        ans = []
        if self.total_weight() >= threshold: ans.append(self)
        for d in self.subdirs:
            small_d = d.smallest_dir_above(threshold)
            if small_d is not None:
                ans.append(small_d)
        if len(ans)<=0: return None
        return min(ans,key=lambda d: d.total_weight())


sample_dir = Directory("sus")
sample_dir.files = [("a",100),("b",200)]
assert(sample_dir.file_weight() == 300)

starting_dir = Directory("/")
current_dir = starting_dir
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
                if destination=="/":
                    current_dir = starting_dir
                elif destination=="..":
                    current_dir = current_dir.parent_dir
                elif current_dir.has_subdirectory(destination):
                    raise ValueError()
                else:
                    newdir = current_dir.add_subdirectory(destination)
                    current_dir = newdir

    # data (file/directory) insertion
    else:
        if line[0] != "dir":
            weight, name = line
            weight = int(weight)
            current_dir.add_file(name,weight)

# starting_dir.print_contents()
ans1 = sum(d.total_weight() for d in starting_dir.fetch_dirs_below(100000))
print(f"First answer: {ans1}") # 1206825
puzzle.answer_a = ans1

free_space = TOTAL_SPACE - starting_dir.total_weight()
space_needed = FREE_SPACE_NEEDED - free_space

ans2 = starting_dir.smallest_dir_above(space_needed).total_weight()
print(f"Second answer: {ans2}") # 9608311
puzzle.answer_b = ans2
