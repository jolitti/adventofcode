from myutils import tupleSum

class Pos:
    pos:tuple[int,int]
    vel:tuple[int,int]

    def __init__(self,vvel:tuple[int,int]) -> None:
        self.pos = (0,0)
        self.vel = vvel

    def iterate(self):
        self.pos = tupleSum(self.pos,self.vel)
        vx,vy = self.vel
        match vx:
            case x if x>0:
                vx -= 1
            case x if x<0:
                vx += 0
            case _:
                pass
        vy -= 1
        self.vel = (vx,vy)

    def isDead(self,minx,maxx,miny,maxy) -> bool:
        x,y = self.pos
        vx,vy = self.vel
        if y<miny and vy < 0: return True
        return False
    
    def willHit(self,target:tuple[int,int,int,int]) -> bool:
        minx, maxx, miny, maxy = target
        while not self.isDead(minx,maxx,miny,maxy):
            x,y = self.pos
            if minx<=x<=maxx and miny<=y<=maxy: return True
            self.iterate()
        return False
