mul = []
for i in range(100,999):
    for j in range(i,999):
        mul.append(i*j)
a = []
for i in mul:
    if(list(str(i)) == list(reversed(list(str(i))))):
        a.append(i)
print(max(a))
