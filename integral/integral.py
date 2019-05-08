def f(x,sigma,miu):
    exp = 2.7182818284590452353
    pi = 3.1415926535897932384
    part1 = 1./((2.*pi)**(0.5)*sigma)
    part2 = -(x - miu)**2./(2.*sigma**2)
    return part1*(exp**part2)


def integerf(xa,xb,n,sigma,miu):
    ans = 0.
    step = (xb - xa)/n
    for i in range(0,n):
        ans += (f(xa+i*step,sigma,miu) + f(xa + (i+1)*step,sigma,miu))*step/2.
    return ans

def interifinit(sigma,miu):
    xa = -5.
    xb = 5.
    n = 1000
    esp = 1e-8
    s = max(abs(xa),abs(xb))
    I1 = integerf(-s,s,n,sigma,miu)
    I2 = integerf(-2*s,2*s,4*n,sigma,miu)
    s = 2*s
    n = 4*n
    NeedNextInte = True
    if(abs(I1-I2) < esp):
        NeedNextInte = False
        return I2
    while(NeedNextInte):
        I1 = I2
        I2 = integerf(-2*s,2*s,4*n,sigma,miu)
        s = 2*s
        n = 4*n
        if(abs(I2 - I1) < esp):
            NeedNextInte = False
            return I2


