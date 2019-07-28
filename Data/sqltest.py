import pymysql

db = pymysql.connect("localhost","root","981722694","testchem")
cursor = db.cursor()

sql = "DESC tb_namechem"
try:
    cursor.execute(sql)
    res = cursor.fetchall()
    for row in res:
        print(row)
except:
    print("Error!")

db.close()