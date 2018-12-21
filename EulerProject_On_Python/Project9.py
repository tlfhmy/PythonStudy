
#此程序需要了解一些数论知识，便于简化运算，小可爱一定要问我哦   (^_^)
a=[]
for i in range(1,60):
    for j in range(1,60):
        if(i*(i+j)==500):
            a.append((i**4-j**4)*(2*i*j))
print(max(a))