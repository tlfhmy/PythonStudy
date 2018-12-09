a = [2,3,5,7,11,13,17,19]

b = [-1]*len(a)

j = 0
for i in a:
    m = 20
    while(m != 0):
        m = int(m / i)
        b[j] += 1
    j += 1

m = 1
for i in range(0,len(a)):
    m *= (a[i]**b[i])

print(m)