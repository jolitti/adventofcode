from sys import argv
import os

day = argv[1]

wd = os.getcwd()
newPath = wd +"/" + day
scriptPath = newPath + "/advent" + day + ".py"
sampleInputPath = newPath + "/input00.txt" 
os.mkdir(wd+"/"+day)
f = open(scriptPath,"w")
f.close()
f = open(sampleInputPath,"w")
f.close()