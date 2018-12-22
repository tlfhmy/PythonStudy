from MyProfile import FactorInteger

m = 1
while(True):
    k = int(m*(m+1)/2)
    fac = FactorInteger(k)
    num = 1
    for i in fac:
        num *= (i[1] + 1)
    if(num > 500):
        print(f"第{m}个三角形数为{int(m*(m+1)/2)},它的素分解为:")
        print(fac)
        print(f"可知,它具有{num}个因子")
        break
    m += 1
