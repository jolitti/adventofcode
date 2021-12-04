with open("input02.txt") as file:
    data = file.readlines()

h,d,aim = 0,0,0

for l in data:
    args = l.split()
    args[1]=int(args[1])

    match args:
        case ["forward",x]:
            h+=x
            d += aim*x
        case ["down",x]:
            aim += x
        case ["up",x]:
            aim -= x
        case _:
            print("Invalid case found")

print(f"{h},{d}")
print(h*d)