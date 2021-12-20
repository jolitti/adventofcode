
def needsExploding(p:str) -> bool:
    nest = 0
    for x in p:
        match x:
            case "[": nest += 1
            case "]": nest -= 1
        if nest>=4: return True
    return False
def needsSplit(p:str) -> bool:
    import re
    nums = re.findall(r"\d+",p)
    for n in nums:
        if int(n)>9: return True
    return False

def pairAdd(p1:str,p2:str) -> str:
    ans = f"[{p1},{p2}]"
