from random import random
esp = 1e-8

fProp = []

n = int(input("请输入样本总数:"))

for i in range(0,n):
    fProp.append(float(input(f"请输入第{i+1}个样本的概率：")))

fSumProp = 0.0                                          #代表分布概率
bCoreProp = True
for i in fProp:
    if i < 0.0:
        bCoreProp = False
        break
    elif i > 1.0:
        bCoreProp = False
        break
    else:
        fSumProp += i

if abs(fSumProp-1.0) > esp:
    bCoreProp = False

if bCoreProp:
    iSamples = list(range(0,n))
    fPropStep = []
    for i in range(0,len(fProp)+1):
        if len(fPropStep) == 0:
            fPropStep.append(0.0)
        else:
            fPropStep.append(fProp[i-1]+fPropStep[-1])
    
    print(fPropStep)

    iTaking = []
    m = int(input("请输入抽样试验次数："))
    for i in range(0,m):
        frdnum = random()
        iPlace = 0
        for j in range(0,len(fPropStep)-1):
            if frdnum >= fPropStep[j] and frdnum < fPropStep[j+1]:
                iPlace = j
                break
        iTaking.append(iPlace)
    
    
    #print(iTaking)

    iTestSamples = [0 for i in range(0,len(iSamples))]
    for i in iTaking:
        iTestSamples[i] += 1
    iTestProp = [0.0 for i in range(0,n)]

    for i in range(0,n):
        iTestProp[i] = iTestSamples[i] / m
    
    print(iTestProp)

else:
    print("概率分布设置错误！")