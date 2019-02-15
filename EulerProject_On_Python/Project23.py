from MyProfile import *

def isAbunddant(num):
    a = FactorInteger(num)
    temp = 1
    for i in a:
        temp *= int( (i[0]**(i[1]+1)-1) / (i[0]-1)  )
    return ((temp - num) > num)

a = []

for i in range(2,28124):
    if(isAbunddant(i)):
        a.append(i)

c = []

for i in range(0,len(a)):
    for j in range(i,len(a)):
        c.append(a[i]+a[j])

d = list(set(range(1,28124)) - set(c))

print(sum(d))