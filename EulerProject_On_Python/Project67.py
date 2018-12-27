a = open("p067_triangle.txt")
b = a.read()
a.close()

chnum = ""
for i in b:
    if(str(i).isdigit()):
        chnum += str(i)

c = []
for i in range(0,len(chnum),2):
    c.append(int(chnum[i:i+2]))

d = []
j = 0
k = 1
while(j < len(c)):
    temp = []
    for i in range(j,j+k):
        temp.append(c[i])
    d.append(temp)
    j += k
    k += 1

submax = []
for i in d:
    if(len(i) == 1):
        submax.append(i[0])
    else:
        temp = []
        for j in range(0,len(i)):
            if(j == 0):
                temp.append(submax[0] + i[0])
            elif(j == len(i) - 1):
                temp.append(submax[-1] + i[-1])
            else:
                temp.append(max(submax[j-1]+i[j],submax[j]+i[j]))
        submax = temp

print(max(submax))