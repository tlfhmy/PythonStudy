normyear = [31,28,31,30,31,30,31,31,30,31,30,31]
leapyear = [31,29,31,30,31,30,31,31,30,31,30,31]

years = range(1901,2001)

firwe = 1

wedyear = []

for i in years:
    if( (((i-1)%100 != 0)&((i-1)%4 == 0)) | ((i-1)&400 == 0)):
        firwe += 2
        firwe = firwe % 7
        wedyear.append(firwe)
    else:
        firwe += 1
        firwe = firwe % 7
        wedyear.append(firwe)

days = 0

for i in range(0,len(years)):
    if(years[i] % 4 == 0):
        fd = wedyear[i]
        for j in leapyear:
            fd += j
            fd = fd % 7
            if(fd == 0):
                days += 1
    else:
        fd = wedyear[i]
        for j in normyear:
            fd += j
            fd = fd % 7
            if(fd == 0):
                days += 1

print(days)