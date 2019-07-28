import pymysql

db = pymysql.connect("localhost","root","981722694","testchem")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s" % data)

db.close()