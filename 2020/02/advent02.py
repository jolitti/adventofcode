import re

with open("example.txt") as file:
    sample_data = file.readlines()

with open("input.txt") as file:
    data = file.readlines()

def is_valid_psswd(s) -> bool:
    a,b = [int(x) for x in re.findall(r"\d+",s)]
    char = re.findall(r"(.)(:)",s)[0][0]
    password = re.findall(r"(: )(.+)",s)[0][1]
    return a <= password.count(char) <= b

def is_valid_psswd_2(s) -> bool:
    a,b = [int(x) for x in re.findall(r"\d+",s)]
    char = re.findall(r"(.)(:)",s)[0][0]
    password = re.findall(r"(: )(.+)",s)[0][1]
    if password[a-1] != char and password[b-1] != char: return False
    return password[a-1] != password[b-1]

def valid_passwords(l:list[str], type:int = 0) -> int:
    ans = 0
    for s in l:
        if type==0:
            if is_valid_psswd(s): ans += 1
        else:
            if is_valid_psswd_2(s): ans += 1
    return ans

if valid_passwords(sample_data) != 2:
    raise ValueError("Wrong answer to the sample!")

if list(map(is_valid_psswd_2,sample_data)) != [True,False,False]:
    raise ValueError("Second pass validation is wrong!")

ans1 = valid_passwords(data)
ans2 = valid_passwords(data,2)

print(f"First answer: {ans1}")
print(f"Second answer: {ans2}")