import enum
from myutils import getAdventData

def charToBool(c:str) -> bool:
    if c=="#": return True
    else: return False

def getNewDefault(oldDefault:bool, s:str) -> bool:
    if oldDefault == False: return charToBool(s[0])
    else: return charToBool(s[-1])

def expandImg(oldImg:list[list[bool]], borderVal:bool) -> list[list[bool]]:
    x,y = len(oldImg[0]),len(oldImg)
    ans = [[borderVal]*(x+2)]
    for l in oldImg:
        newRow = [borderVal]
        newRow += l
        newRow += [borderVal]
        ans.append(newRow)
    ans.append([borderVal]*(x+2))
    return ans

def getValAt(img:list[list[bool]],x:int,y:int,default:bool) -> bool:
    xmax,ymax = len(img[0]),len(img)
    if 0<=x<xmax and 0<=y<ymax : return img[y][x]
    else: return default

def getNewVal(img:list[list[bool]],x:int,y:int,default:bool, seed:str) -> bool:
    num = ""
    for j in [y-1,y,y+1]:
        for i in [x-1,x,x+1]:
            num += "1" if getValAt(img,i,j,default) else "0"
    return charToBool(seed[int(num,2)])

def copy2d(list2d: list[list]):
    ans = []
    for r in list2d: ans.append(r[:])
    return ans

data = getAdventData("2021/20","input20.txt")

seed = data[0]
data = data[2:]

img = [[charToBool(x) for x in d] for d in data]
default = False

for _ in range(50):
    img = expandImg(img,default)
    newImg = copy2d(img)

    for j,r in enumerate(img):
        for i,x in enumerate(r):
            newImg[j][i] = getNewVal(img,i,j,default,seed)
    
    img = newImg
    default = getNewDefault(default,seed)

with open("2021/20/output.txt","w") as file:
 for r in img:
        for x in r:
            file.write("#" if x else ".")
        file.write("\n")

tot = 0
for d in img:
    for x in d:
        if x==True:
            tot += 1

print(tot)