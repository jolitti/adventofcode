import hashlib
import sys

i = 0
while True:
    bst = "iwrupvqb" + str(i)
    s = hashlib.md5(bytes(bst,encoding="utf8")).hexdigest()
    if str(s)[:6]=="000000":
        print(i)
        sys.exit()
    i+=1

""" s = "abcdef609043"
print(hashlib.md5(bytes(s,encoding="utf8")).hexdigest()) """