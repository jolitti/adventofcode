from octoboard import OctoBoard

with open("11/input11.txt") as file:
    data = file.readlines()
data = [d.strip() for d in data]

b = OctoBoard(data)
print(b.iterateTilAllFlash() + 1)