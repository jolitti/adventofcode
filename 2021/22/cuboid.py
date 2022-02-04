
class Cuboid:
    value:any
    coords = [(0,0),(0,0),(0,0)]

    def __init__(self,coords:list[str],val):
        self.value = val
        self.coords = []
        for p in coords:
            start, end = map(int,p.split(".."))
            self.coords.append((start,end))

    def toLimitPts(self) -> tuple[tuple[int,int,int]]:
        (x1,x2),(y1,y2),(z1,z2) = self.coords
        return ((x1,y1,z1),(x2,y2,z2))

    def intersects(c:"Cuboid") -> bool:
        pass