from mimetypes import common_types
from sys import argv
import os

common_code = """
with open("example.txt") as file:
    sample_data = file.readlines()
    sample_data = [x.strip() for x in sample_data]
with open("input.txt") as file:
    data = file.readlines()
    data = [x.strip() for x in data]
"""

day = argv[1]

wd = os.getcwd()
newPath = wd +"/" + day
scriptPath = newPath + "/advent" + day + ".py"
sampleInputPath = newPath + "/example.txt" 
os.mkdir(wd+"/"+day)
f = open(scriptPath,"w")
f.write(common_code)
f.close()
f = open(sampleInputPath,"w")
f.close()