import sys

day = sys.argv[1]

with open("template.py") as file:
    file_content = file.read()

file_content = file_content.replace("$DAY",day)

with open("day"+day+".py","a") as file:
    file.write(file_content)
