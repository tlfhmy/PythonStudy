import pymysql


class ChemLib(object):
    def __init__(self, htname, acname, pswd, dbname, tbname):
        self.hostname = htname
        self.accountname = acname
        self.databasename = dbname
        self.db = pymysql.connect(htname, acname, pswd, dbname)
        self.cursor = self.db.cursor()
        self.tablename = tbname
        self.tableHead = []
        self.__GettableHead__()
        self.tables = []
        self.__Gettables__()
        self.Help()
        #self.tablestruct = None
    
    def Help(self):
        print("该程序已实现的功能有\n")
        print("1. 读取表头信息")
        print("2. 打印整张表")
        print("3. 自由命令（显示不完美）")
        print("4. 显示数据库拥有哪些表")

    def __GettableHead__(self):
        sql = "DESC "+self.tablename
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for row in res:
                self.tableHead.append(row[0])
        except:
            print("Error1!")
    
    def __Gettables__(self):
        sql = "SHOW TABLES"
        self.cursor.execute(sql)
        res=self.cursor.fetchall()
        #print(res)
        for row in res:
            self.tables.append(row[0])

    def ShowTables(self):
        for ele in self.tables:
            print(ele)

    def Show(self, Limit = -1):
        assert(type(Limit)==int)
        if Limit < -1:
            sql = "SELECT * FROM "+self.tablename
            try:
                self.cursor.execute(sql)
                res = self.cursor.fetchall()
                for row in res:
                    cnt = len(row)
                    for i in range(0, cnt):
                        print(self.tableHead[i], ":", row[i], end="  ")
                    print("\n")
            except:
                print("Error2!")
        else:
            sql = "SELECT * FROM " + self.tablename + " LIMIT " + str(Limit)
            try:
                self.cursor.execute(sql)
                res = self.cursor.fetchall()
                for row in res:
                    cnt = len(row)
                    for i in range(0, cnt):
                        print(self.tableHead[i], ":", row[i], end="  ")
                    print("\n")
            except:
                print("Error2!")
    
    def ShowRows(self):
        sql = "SELECT COUNT(*) FROM " + self.tablename
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            #print(res)
            for row in res:
                cnt = len(row)
                for i in range(cnt):
                    print(self.tableHead[i], ":", row[i], end=" ")
        except:
            print("Error3!")

    def Command(self):
        cont = True
        while(cont):
            sql = str(input())
            try:
                self.cursor.execute(sql)
                res = self.cursor.fetchall()
                for row in res:
                    for i in range(len(row)):
                        print(row[i])
                    print("\n")
            except:
                m = str(input("Error!\nContinue? y/n"))
                if m == 'y':
                    continue
                else:
                    break