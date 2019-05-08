import random
from copy import deepcopy
a = []
for i in range(0,1000):
    x = random.randint(-105,105)
    a.append(x)
print(a)
print(len(a))
xp = (sum(a))/1000
print(xp)
m = 0
for i in a:
    m += (i-xp)**2
s = (1/(1000-1)*m)**0.5
print(s)

b=[[] for _ in range(21)]
#print(b)
a1=-105
b1=106
a2=0
b2=21
for i in a:
    n=(i-a1)/(b1-a1)*(b2-a2)
    b[int(n)].append(i)



print(b[0])