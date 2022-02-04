def getCuboid(pts:list[str]) -> list[tuple[int,int]]:
    ans = []
    for p in pts:
        start, end = map(int,p.split(".."))
        ans.append((start,end))
    return ans

def trimCuboid(pts:list[tuple[int,int]], limit:int) -> list[tuple[int,int]] | None:
    for start,end in pts:
        if start>limit or end<-limit: return None
    
    ans = []
    for start,end in pts:
        ans.append((max(-limit,start),min(end,limit)))
    return ans

def cuboidToPoints(cuboid:list[tuple[int,int]]) -> list[tuple[int,int]]:
    ans = []
    xx,yy,zz = cuboid
    for x in range(xx[0],xx[1]+1):
        for y in range(yy[0],yy[1]+1):
            for z in range(zz[0],zz[1]+1):
                ans.append((x,y,z))
    return ans