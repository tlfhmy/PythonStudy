n = int(input(">"))

a = [True]*(n+1)

a[0] = False
a[1] = False

for i in range(2,n):
    if(a[i] == False):
        continue
    j = i*i
    while(j <= n):
        if(j % i == 0):
            a[j] = False
        j += 2

b = []

for i in range(0,n+1):
    if(a[i]):
        b.append(i)

print(sum(b))