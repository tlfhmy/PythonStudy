from random import randint
n = int(input("请输入随机数个数:"))
a = []
for i in range(0,n):
    a.append(randint(0,2*n))

print(a)

for i in range(1,n):
    key = a[i]
    j = i - 1
    while j > -1 and a[j] > key:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key

print(a)