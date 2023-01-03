from aocd import lines
from aocd.models import Puzzle

puzzle = Puzzle(year=2022,day=16)

class Node:
    flow:int
    def __init__(self,s:str,others:set[str,"Node"]):
        s = s.replace(";","")
        s = s.replace(",","")

