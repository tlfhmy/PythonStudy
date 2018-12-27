a = "75 \
95 64 \
17 47 82 \
18 35 87 10 \
20 04 82 47 65 \
19 01 23 75 03 34 \
88 02 77 73 07 63 67 \
99 65 04 28 06 16 70 92 \
41 41 26 56 83 40 80 70 33 \
41 48 72 33 47 32 37 16 94 29 \
53 71 44 65 25 43 91 52 97 51 14 \
70 11 33 28 77 73 17 78 39 68 17 57 \
91 71 52 38 17 14 91 43 58 50 27 29 48 \
63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

b = a.replace(" ","")
c = []
for i in range(0,len(b),2):
    c.append(int(b[i:i+2]))

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