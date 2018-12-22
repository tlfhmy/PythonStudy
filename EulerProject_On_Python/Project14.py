from functools import reduce

def Collatz(num):
    chain = []
    while(num != 1):
        chain.append(num)
        if(num % 2 == 0):
            num = int(num / 2)
        else:
            num = 3*num + 1
    chain.append(1)
    return chain


tmp = list(map(lambda p: Collatz(p),range(1,1000000)))

mx = max(map(lambda p:len(p),tmp))

for i in tmp:
    if(len(i) == mx):
        print(i[0])
        break