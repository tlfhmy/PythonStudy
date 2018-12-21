n = int(input("如果数组越界，请输入更大的n:    "))

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


m = 1
while(True):
    k = int(m*(m+1)/2)
    fac = []
    j = 0
    isFirst = True
    while(True):
        fc = b[j]
        if(k % fc == 0):
            if(isFirst):
                fac.append([fc,1])
            else:
                fac[-1][1] += 1
            k = int(k / fc)
            isFirst = False
            continue
        else:
            isFirst = True
        if(k == 1):
            break
        if(k < b[j]):
            fac.append(k)
            break
        j += 1
    
    num = 1
    for i in fac:
        num *= (i[1] + 1)
    #print(fac,num)
    if(num > 500):
        print(f"第{m}个三角形数为{int(m*(m+1)/2)},它的素分解为:")
        print(fac)
        print(f"可知,它具有{num}个因子")
        break
    m += 1
