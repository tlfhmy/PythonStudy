import pymysql


class ChemLib(object):
    def __init__(self, htname, acname, pswd, dbname, tbname):
        self.hostname = htname
        self.accountname = acname
        self.databasename = dbname
        self.db = pymysql.connect(htname, acname, pswd, dbname)
        self.cursor = self.db.cursor()
        self.tablename = tbname
        #self.tablestruct = None

    def ShowAll(self):
        sql = "DESC "+self.tablename
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            tableHead = []
            for row in res:
                tableHead.append(row[0])
        except:
            print("Error1!")

        sql = "SELECT * FROM "+self.tablename
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            for row in res:
                cnt = len(row)
                for i in range(0, cnt):
                    print(tableHead[i], ":", row[i], end="  ")
                print("\n")
        except:
            print("Error2!")

    def Insert(self, sn_C, sn_E, ssmi, fwie):
        sql = "DESC "+self.tablename
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            tableHead = []
            for row in res:
                tableHead.append(row[0])
        except:
            print("Error1!")
        try:
            sql = "INSERT INTO "+self.tablename+"("
            for i in range(1, len(tableHead)):
                sql += tableHead[i]
                sql += ","
            sql = sql[:-1]
            tmp = ") VALUES("+"\""+sn_C+"\", \""+sn_E+"\", \""\
                +ssmi+"\", "+fwie+")"
            sql += tmp
            print(sql)
            self.cursor.execute(sql)
            self.cursor.connection.commit()
        except:
            print("Error3!")
