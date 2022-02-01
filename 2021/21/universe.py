from myutils import tupleSum
from functools import cache

WIN_POINTS = 21

results = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}

def addWrap(a,b) -> int:
    ans = a+b
    return ans%10

@cache
def getWins(p1,pt1,p2,pt2,turn) -> tuple[int,int]:
    if pt1>=WIN_POINTS: return (1,0)
    elif pt2>=WIN_POINTS: return (0,1)

    ans = (0,0)

    for k in results.keys():
        ansk = (0,0)
        if turn == 1:
            newp1 = addWrap(p1,k)
            newpt1 = pt1+newp1+1
            ansk = getWins(newp1,newpt1,p2,pt2,2)
        else:
            newp2 = addWrap(p2,k)
            newpt2 = pt2+newp2+1
            ansk = getWins(p1,pt1,newp2,newpt2,1)
        
        a,b = ansk
        ans = tupleSum(ans,(a*results[k],b*results[k]))
    
    return ans