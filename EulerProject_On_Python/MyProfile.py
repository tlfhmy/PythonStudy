from functools import reduce

#------------------------数学组合数----------------------------
def Conbinnum(num1,num2):
    if(num1 == num2):
        return 1
    elif((num1 > 0) & (num2 == 0)):
        return 1
    elif((num2 > num1) | (num1 < 0) | (num2 < 0)):
        return "Math Error!"
    else:
        fct1 = reduce(lambda x,y: x*y,range(1,num1+1))
        fct2 = reduce(lambda x,y: x*y,range(1,num2+1))
        fct3 = reduce(lambda x,y: x*y,range(1,num1-num2+1))
        return int(fct1 /(fct2 * fct3))

#-------------------------生成不大于num的素数表----------------------
def PrimeNumber(num):
    a = [True]*(num+1)
    a[0] = False
    a[1] = False
    for i in range(2,num):
        if(a[i] == False):
            continue
        j = i*i
        while(j <= num):
            if(j % i == 0):
                a[j] = False
            j += 2

    b = []

    for i in range(0,num+1):
        if(a[i]):
            b.append(i)
    return b

#----------------------给出指定整数的素分解--------------------
def FactorInteger(num):
    fac = []
    isFirst = True
    while(num % 2 == 0):
        if(isFirst):
            fac.append([2,1])
            num = int(num / 2)
            isFirst = False
        else:
            fac[0][1] += 1
            num = int(num / 2)

    j = 3
    while(True):
        isFirst = True
        if(num < j):
            if(num != 1):
                fac.append([num,1])
            return fac
        else:
            while(num % j == 0):
                if(isFirst):
                    fac.append([j,1])
                    num = int(num / j)
                    isFirst = False
                else:
                    num = int(num / j)
                    fac[-1][1] += 1
        j += 2

#---------------------制成某种整数列表--------------------
def Table(func,start,end):
    return(list(map(func,range(start,end + 1))))

#--------------------