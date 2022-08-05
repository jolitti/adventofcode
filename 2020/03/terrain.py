

class Terrain:
    map: list[str]

    def __init__(self,map:list[str]) -> None:
        self.map = map
        self.width = len(self.map[0])
        self.height = len(self.map)

    def is_tree(self,x:int,y:int) -> bool:
        if x<0 or y<0: raise ValueError("Invalid coordinates!")
        new_x = x % self.width
        if self.map[y][new_x] == "#": return True
        else: return False

    def get_trees(self,x_incr,y_incr) -> int:
        x,y = 0,0
        ans = 0
        while y<self.height:
            if self.is_tree(x,y): 
                ans += 1
            x += x_incr
            y += y_incr
        return ans
