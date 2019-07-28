from ofile import *
import re

s = readFile("target_uniprot.txt")
print(len(s))
t = readFile("pdbbind.txt")
print(len(t))

r = []

pat = ""
for j in t:
        if j != "":
            pat += "......."+j+"$"+"|"
pat= pat[:-1]



outfile = open("out.txt","w+")
for i in s:
        matchObj = re.match(pat,i,re.IGNORECASE)
        if matchObj is not None:
            #print(matchObj.group())
            outfile.write(matchObj.group()+"\n")

outfile.close()