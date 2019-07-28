import pymysql

db = pymysql.connect("localhost","root","981722694","testchem")
cursor = db.cursor()

sql = "SELECT * FROM tb_namechem"

try:
    cursor.execute(sql)
    res = cursor.fetchall()
    for row in res:
        id = row[0]
        name_CHS = row[1]
        name_ENG = row[2]
        smiles = row[3]

        print("id: %s, name_CHS: %s, name_ENG: %s, smiles :%s" % \
            (id,name_CHS,name_ENG,smiles))
except:
    print("Error!")

db.close()