from ChemSQLMan import *

Chl = ChemLib("localhost","root","981722694","testchem","tb_namechem")
Chl.ShowAll()
Chl.Insert("测试","Test","C=C","0.0")