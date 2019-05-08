from copy import deepcopy
class Matrix(object):
    def __init__(self,b):
        if type(b) == list:
            self.body = deepcopy(b)
        elif type(b) == int:
            self._unitmatrix(b)
        else:
            self = [[]]
            print("Error Code 0!")
        self._check()

    def _unitmatrix(self,n):
        s = [[0]*n for _ in range(0, n)]
        for i in range(0, n):
            s[i][i] = 1
        self.body = deepcopy(s)

    def _check(self):
        length = len(self.body[0])
        for i in self.body:
            if(len(i) != length):
                print("Error Code 1!")
                self.body = [[]]
                return

    def show(self):
        print("Matrix(")
        for i in self.body:
            print(i)
        print(")")
    
    def GetRoCo(self):
        return (len(self.body), len((self.body)[0]))

    def ReverseMatrix(self):
        if(self.GetRoCo()[0] == self.GetRoCo()[1]):
            RM = Matrix(self.GetRoCo()[0])
            OM = deepcopy(self)
            for ss in range(0, len(OM.body)):
                if OM.body[ss][ss] == 0:
                    NotZeroFound = False
                    for i in range(ss+1, len(OM.body)):
                        if(OM.body[i][ss] != 0):
                            temp = deepcopy(OM.body[i])
                            OM.body[i] = deepcopy(OM.body[ss])
                            OM.body[ss] = deepcopy(temp)
                            NotZeroFound = True
                            break
                    if(not(NotZeroFound)):
                        print("ReverseMatrix does not exist.")
                        return Matrix([[]])
                else:
                    valfir = OM.body[ss][ss]
                    for i in range(ss+1, len(OM.body)):
                        valfi = OM.body[i][ss]
                        for j in range(0,len(OM.body)):
                            OM.body[i][j] -= valfi/valfir*OM.body[ss][j]
                    
            return OM


        else:
            print("Error Code 3!")  #非方阵不能求逆矩阵。
    
a = Matrix([[1,2,7,1,1],[2,1,3,3,4],[5,1,3,2,7],[8,6,3,1,3],[2,5,3,1,3]])
b = a.ReverseMatrix()
b.show()