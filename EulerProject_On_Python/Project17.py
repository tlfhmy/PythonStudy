from MyProfile import Table
from random import randint
numnam = {1:"one",2:"two",3:"three",4:"four",5:"five",\
6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",\
12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",\
17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",\
40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",\
100:"one hundred",1000:"one thousand"}



def NumToName(num,names):
    if((num>1000) | (num<1)):
        return ""
    if(num in names):
        return names[num]
    else:
        temp = ""
        digt = str(num)
        if(len(digt) == 3):
            temp += NumToName(int(digt[0]),names)
            temp += " hundred"
            if(int(digt[1:3]) in numnam):
                temp += " and "
                temp += NumToName(int(digt[1:3]),names)
                return temp
            elif(int(digt[1:3]) == 0):
                return temp
            else:
                temp += " and "
                temp += NumToName(int(digt[1]+"0"),names)
                temp += " "
                temp += NumToName(int(digt[2]),names)
                return temp
        else:
            temp += NumToName(int(digt[0]+"0"),names)
            temp += " "
            temp += NumToName(int(digt[1]),names)
            return temp

m = Table(lambda p: NumToName(p,numnam),1,1000)
print(sum(list(map(lambda p:len(p.replace(" ","")),m))))