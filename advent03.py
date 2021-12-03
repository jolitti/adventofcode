def nukeList(l:list[str],filterValue:str,index) -> list[str]:
    newL = [x for x in l if x[index]==filterValue]
    return newL

def getOx(_data:list[str]) -> int:
    v = _data[:]
    numLen = len(v[0])
    for j in range(numLen):
        if len(v)==1: break
        ones, zeros = 0,0
        
        for n in v:
            if n[j]=="1":ones+=1
            else: zeros += 1
    
        if ones>=zeros: v = nukeList(v,"1",j)
        else: v = nukeList(v,"0",j)
    
    return int(v[0],2)

def getCO2(_data:list[str]) -> int:
    v = _data[:]
    numLen = len(v[0])
    for j in range(numLen):
        if len(v)==1: break
        ones, zeros = 0,0
        
        for n in v:
            if n[j]=="1":ones+=1
            else: zeros += 1
    
        if ones>=zeros: v = nukeList(v,"0",j)
        else: v = nukeList(v,"1",j)
    
    return int(v[0],2)



with open("input03.txt") as file:
    data = file.readlines()

data = [l.strip() for l in data]

x= getOx(data)
y= getCO2(data)
print(x)
print(y)
print(x*y)

""" gamma = ""

for j in range(len(data[0])):
    sum = 0
    for i,x in enumerate(data):
        #print(f"{j},{i}")
        if x[j] == "1": sum+=1
    if sum>len(data)/2: gamma += "1"
    else: gamma += "0"

x = int(gamma,2)

epsilon = ["1" if d=="0" else "0" for d in gamma]
epsilon = "".join(epsilon)

y = int(epsilon,2)

print(x)
print(y)
print(x*y) """

