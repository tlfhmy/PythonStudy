from math import log
from copy import deepcopy

class ConverNum(object):
    def __init__(self, n, m=10):
        # 此处的 base 是指该数字的基（进制）
        #  num 是一个数组，它表示在基base下每个位的数码表示
        #  value 代表这个数字的与基无关的数学值（当然在计算机格式化输出时默认十进制）
        assert type(n) == list or type(n) == int or type(n) == tuple
        if type(n) == int:
            self.num = list(map(lambda x: int(x), list(str(n))))
            self.base = int(m)
        else:
            self.num = list(n)
            self.base = int(m)
        tmp = 0
        for i in range(0, len(self.num)):
            tmp += (self.num)[i] * (self.base)**(len(self.num) - i -1)
        self.value = tmp

    def __str__(self):
        return str(self.num) + " in base " + str(self.base)
    
    def __repr__(self):
        return str(self)
    
    def baseSet(self, s):
        assert type(s) == int
        assert s > 0
        self.base = s

        #基改变之后，它的数码表示也会改变；所以需要计算出新表示。
        tmp = []
        p = self.value
        r = int(log(self.value, self.base))
        for i in range(0, r+1):
            tmp.append(p // self.base**(r-i))
            p -= tmp[i]*(self.base**(r-i))
        if tmp[0] == self.base:
            tmp.append(0)
            tmp[0] = 1
        self.num = list(tmp)
    

    ####定义加减的乘法，求余数，求商数的运算：结果以第一个数字的基为自己的基。



    #    __add__, __mul__等等不带i的运算之中，涉及中间变量的赋值，必须加入
    #   deepcopy，这样才能仅仅赋值而不是传递对象；否则对中间变量的改变，就会传递到
    #   self本身上去了。
    #   但是对带__iadd__, __imul__等带i的运算中，我们期望会改变self自身，所以
    #   就不考虑这一层了。
    #
    #
    #   因为，在Python中，赋值默认传递的是对象本身，类似于C或C++中的引用
    #   在Python中的  a = b， 等价于C或C++中的 a = &d


    def __add__(self, tp):                                      #加法              a+b
        assert type(tp) == ConverNum
        sum = deepcopy(self)
        sum.value += tp.value
        sum.baseSet(self.base)
        return sum

    def __iadd__(self, tp):                                     #自变增强加法       a += b <==> a = a+b
        assert type(tp) == ConverNum
        self.value += tp.value
        self.baseSet(self.base)
        return self
    
    def __mul__(self, tp):                                      #乘法       a*b
        assert type(tp) == ConverNum
        multi = deepcopy(self)
        multi.value *= tp.value
        multi.baseSet(self.base)
        return multi

    def __imul__(self, tp):                                     #自变增强乘法    a *= b <==> a = a*b
        assert type(tp) == ConverNum
        self.value *= tp.value
        self.baseSet(self.base)
        return self

    def __sub__(self, tp):                                      #减法          a-b
        assert type(tp) == ConverNum
        dif = deepcopy(self)
        dif.value -= tp.value
        dif.baseSet(self.base)
        return dif

    def __isub__(self, tp):                                     ##自变增强减法  a -= b  <==> a = a-b
        assert type(tp) == ConverNum
        self.value -= tp.value
        self.baseSet(self.base)
        return self
    
    def __mod__(self, tp):                                      ##求模运算，求余数      a%b
        assert type(tp) == ConverNum
        rem = deepcopy(self)
        rem.value %= tp.value
        rem.baseSet(self.base)
        return rem
    
    def __imod__(self, tp):                                     ##自变增强求模运算，求余数      a %= b <==> a = a%b
        assert type(tp) == ConverNum
        self.value %= tp.value
        self.baseSet(self.base)
        return self
    
    def __floordiv__(self, tp):                                 ##求整除商  a // b
        assert type(tp) == ConverNum
        quot = deepcopy(self)
        quot.value //= tp.value
        quot.baseSet(self.base)
        return quot
    
    def __ifloordiv__(self, tp):                                ##自变增强求整除商  a //= b <==> a = a//b
        assert type(tp) == ConverNum
        self.value //= tp.value
        self.baseSet(self.base)
        return self
    