indexes = "abcdefg"

lengths = {
    2:[1],
    3:[7],
    4:[4],
    5:[2,3,5],
    6:[0,6,9],
    7:[8]
}
segments_alfa = {
    0:"abcefg",
    1:"cf",
    2:"acdeg",
    3:"acdfg",
    4:"bcdf",
    5:"abdfg",
    6:"abdefg",
    7:"acf",
    8:"abcdefg",
    9:"abcdfg"
}
segments_num = {
    0: {0,1,2,4,5,6},
    1: {2,5},
    2: {0,2,3,4,6},
    3: {0,2,3,5,6},
    4: {1,2,3,5},
    5: {0,1,3,5,6},
    6: {0,1,3,4,5,6},
    7: {0,2,5},
    8: {0,1,2,3,4,5,6},
    9: {0,1,2,3,5,6}
}

def isPrunable(l)->bool:
    solvedChars = [x for x in l if len(x)==1]
    unsolved = [x for x in l if len(x)>1]

    for c in solvedChars:
        for u in unsolved:
            if u.find(c) != -1: return True
    return False

def prune(l:list[str]) -> list[str]:
    lens = {len(x) for x in l}
    if 1 not in lens: return l
    while isPrunable(l):
        for i,s in enumerate(l):
            if len(s)==1:
                for j,ss in enumerate(l):
                    if j==i: continue
                    l[j] = ss.replace(s,"")
    return l

def charInters(l:list[str]) -> tuple[str,str]: #returns common, non-common chars
    sets = [set(x) for x in l]
    common = sets[0]
    non_common = set()
    for s in sets[1:]:
        union = common.union(s)
        common = common.intersection(s)
        non_common = non_common.union(union.difference(common))
    return "".join(common),"".join(non_common)
    



def translate(s:str,key:str) -> int:
    ans = set()
    for c in s:
        ans.add(key.index(c))
    
    for k in segments_num:
        if segments_num[k] == ans: return k

def solveSevSeg(data:list[str]) -> str: # char index is actual seg, char is encoded seg
    # data is the list of numbers the
    # submarine is attempting to display
    data = [x for x in data if len(x)<7] #filter out "8", it has no information
    data = sorted(data,key=len)

    candidates = ["abcdefg"]*7 # index= reak segment, content= possible position

    data_len = {len(x) for x in data}
    #print(*data_len)
    list5 = [x for x in data if len(x)==5]
    common5, uncommon5 = charInters(list5)
    posCommon5, posUncommon5 = [3,6],[2,4,5]
    list6 = [x for x in data if len(x)==6]
    common6, uncommon6 = charInters(list6)
    posCommon6, posUncommon6 = [5,6],[2,3,4]

    #case 1 (len 2)
    segs1 = data[0]
    for i in segments_num[1]:
        candidates[i] = segs1
    
    #case 7 (len 3)
    _,seg0 = charInters([data[0],data[1]])
    candidates[0] = seg0
    #for i,c in enumerate(candidates[1:]):
    #    candidates[i+1] = c.replace(seg0,"") #This one is solved
    candidates = prune(candidates)

    #case 4 (len 4)
    _,segs4 = charInters([data[0],data[2]])
    candidates[1]=segs4
    candidates[3]=segs4

    candidates = prune(candidates)

    #print(*candidates)

    #case 2,3,5 (len 5)
        #subcase: common segments
    for i in [3,6]:
        segs,_ = charInters([candidates[i],common5])
        candidates[i] = segs
        candidates = prune(candidates)
    #print(*candidates)
    
    # seg 4 is the uncommon value with seg 2
    _, seg4 = charInters([candidates[4],candidates[2]])
    candidates[4] = seg4
    candidates = prune(candidates)
    
    #print(*candidates)

    # seg 2 is the common value from seg 2 and uncommon 6
    seg2, _ = charInters([candidates[2],uncommon6])
    candidates[2] = seg2
    # seg 5 is the remaining one
    _, seg5 = charInters([candidates[5],seg2])
    candidates[5] = seg5

    #print(*candidates)
    return "".join(candidates)
    


#print(*prune(["a","abc","bcd"]))

#key = solveSevSeg(["acedgfb","cdfbe","gcdfa","fbcad","dab","cefabd","cdfgeb","eafb","cagedb","ab"])
#print(translate("cdfbe",key))
#print(translate("dab",key))
#solveSevSeg(["fdgbe", "aefbdcg", "cfebd", "gceb", "cbgadf", "fbc", "gfdbae", "ecfda", "cb", "bcgefd"])
#print(charInters(["abc","abd","b"]))