import sys
import os

day = sys.argv[1]

if os.path.exists("day"+day+".py"):
    print("Denied: file already exists")
    sys.exit()

with open("template.py") as file:
    file_content = file.read()

file_content = file_content.replace("$DAY",day)

with open("day"+day+".py","a") as file:
    file.write(file_content)
