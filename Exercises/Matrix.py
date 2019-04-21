class Matrix(object):

    def __init__(self, a, m = 1, n = 1):
        assert (type(a) == tuple) or (type(a) == list)
        assert (len(a) == m*n)
        self.m = int(m) #row
        self.n = int(n) #column
        self.a = list(a)
    
    def __str__(self):
        MatrStr = ""
        for i in range(0, self.m):
            for j in range(0, self.n):
                MatrStr += str((self.a)[j+i*(self.n)]) + "\t"
            MatrStr += "\n"
        return MatrStr

    def __repr__(self):
        return str(self)
    
    def __add__(self, mtp):                 # M + MTP
        assert type(mtp) == Matrix
        assert(mtp.m == self.m) and (mtp.n == self.n)
        atp = [0] * len(self.a)
        c = Matrix(atp, self.m, self.n)
        for i in range(0,len(self.a)):
            (c.a)[i] = (self.a)[i] + (mtp.a)[i]
        return c 

    def __iadd__(self, mtp):            # M += MTP or M = M + MTP
        assert type(mtp) == Matrix
        assert(mtp.m == self.m) and (mtp.n == self.n)
        c = self + mtp
        self = c
        return self

    def __mul__(self, mtp):             # M * P
        assert type(mtp) == Matrix
        assert(mtp.m == self.n)

        atp = [0]*(self.m * mtp.n)
        c = Matrix(atp, self.m, mtp.n)

        for i in range(0, c.m):
            for j in range(0, c.n):
                #calculate c_ij
                for k in range(0, self.n):
                    (c.a)[j+i*c.n] += (self.a)[k+i*self.n] * (mtp.a)[j+k*mtp.n]
        return c

    def Det(self):
        return 0

    def Reserve(self):
        return self
    
    def Trans(self):
        return self