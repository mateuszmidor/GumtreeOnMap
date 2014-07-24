import codecs
import re

names = []
for line in codecs.open('names.txt', encoding="utf-8"):
    name = line.strip("\n\r\t ")
    if (name != ""):
        names.append(name)

names.sort(lambda s1, s2: cmp(len(s2), len(s1)))       

streets = codecs.open('streets.txt', encoding="utf-8").readlines()
for s in streets:
    for n in names:
        if (n in s):
            found = re.search(n + r"\w*\s*(.*)", s)
            
            if (found):
                print n, ' --- ', found.group(1)
          
