a=[]
for i in range(1,60):
    for j in range(1,60):
        if(i*(i+j)==500):
            a.append((i**4-j**4)*(2*i*j))
print(max(a))