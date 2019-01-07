from MyProfile import *


def f(num):
    m = 1
    for i in FactorInteger(num):
        m *= int((1-i[0]**(i[1]+1)) / (1-i[0]))
    m -= num
    return m

d = []
for i in range(2,10000+1):
    if((i==f(f(i))) & (i != f(i))):
        d.append(i)
print(sum(d))

