import os

pa = os.path.split(os.path.realpath(__file__))
path = pa[0]

infile = open(path+"/input","w+")
inname = str(input("请输入化学式名称：  "))
infile.write(inname)
infile.close()

com = "java -jar " + path + "/opsin.jar -osmi " + path + "/input  " + path + "/output" 
os.system(com)

outfile = open(path+"/output","r+")
outname = str(outfile.read())
outfile.close()
print(outname)