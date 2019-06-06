from copy import deepcopy


#           Error Code Table            #
#---------------------------------------#
#|Error Code 0  | 矩阵初始化数据类型错误
#|Error Code 1  | 矩阵初始化数据形式错误
#|Error Code 2  | 非方阵不能求逆矩阵
#|Error Code 3  | 
#---------------------------------------



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
            print("[",end="")
            for j in range(0,len(i)):
                if j != len(i) - 1:
                    print("%10.3f"%i[j],end="")
                else:
                    print("%10.3f     "%i[j],end="")
            print("]")
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

                            temprm = deepcopy(RM.body[i])
                            RM.body[i] = deepcopy(RM.body[ss])
                            RM.body[ss] = deepcopy(temprm)

                            NotZeroFound = True
                            break
                    if(not(NotZeroFound)):
                        print("ReverseMatrix does not exist.")
                        return Matrix([[]])
                valfir = OM.body[ss][ss]
                for i in range(ss+1, len(OM.body)):
                    valfi = OM.body[i][ss]
                    for j in range(0,len(OM.body)):
                        OM.body[i][j] -= valfi/valfir*OM.body[ss][j]

                        RM.body[i][j] -= valfi/valfir*RM.body[ss][j]
            
            for k in range(len(OM.body)-1, 0-1, -1):
                for j in range(k-1,0-1,-1):
                    lstelm = OM.body[k][k]
                    opeelm = OM.body[j][k]
                    for i in range(0, len(OM.body[0])):
                        OM.body[j][i] -= opeelm/lstelm*OM.body[k][i]

                        RM.body[j][i] -= opeelm/lstelm*RM.body[k][i]

            for i in range(0, len(OM.body)):
                tp = OM.body[i][i]
                for j in range(0, len(OM.body[0])):
                    OM.body[i][j] /= tp
                    RM.body[i][j] /= tp              
            return RM
        else:
            print("Error Code 2!")  #非方阵不能求逆矩阵。
    
a = Matrix([[1,3,7,12],[3,1,3,5],[5,7,6,9],[5,0,3,3]])
b = a.ReverseMatrix()
b.show()