import os
import sys
import shutil

#读取文本文件
#入口：
#    filename 文件名
#    encoding 文件的编码方式
#      "gbk" (默认编码方式）  相当于记事本的 ansi
#      "utf-8"
#      "utf-16"
#返回：
#   字符串数组，每个元素代表文本文件的一行
def readFile( filename,encoding = "utf-8" ):
    ret = []
    try:
        f=open(filename,"rb")
        x=f.read()
        f.close()
        s=x.decode(encoding )
        del(x)
        s=s.replace("\r\n","\n")
        ret=s.split("\n")
        if len(ret)>0 :
            y=ret[0]
            if len(y)>1 and y[0]=="\ufeff":
                ret[0]=y[1:]
    except:
        print("\r\n错误信息：\r\n",sys.exc_info()[0],"\r\n")
    return ret

#判断一个路径sPath是否文件夹？
#返回： True = 是
#       False = 不是
def isDir( sPath ):
    ret = False
    if os.path.exists(sPath):
        if os.path.isdir( sPath ):
            ret = True
    return ret

#判断一个路径sPath是否文件？
#返回： True = 是
#       False = 不是
def isFile( sPath ):
    ret = False
    if os.path.exists(sPath):
        if os.path.isfile( sPath ):
            ret = True
    return ret

#获取 某文件夹中的所有文件列表
#返回值：该文件夹中的所有文件的文件名
def getFileList( sPath ):
    ret = []
    if isDir( sPath ):
        sPath = sPath.replace("\\","/")
        if sPath[len(sPath)-1] !='/':
            sPath=sPath+'/';
        L= os.listdir(sPath)
        for s in L:
            s1=sPath+s
            if isFile(s1):
                ret.append(s)
    return ret
#获取 某文件夹中的所有文件夹列表
#返回值：该文件夹中的所有子文件夹的文件夹名
def getDirList( sPath ):
    ret = []
    if isDir( sPath ):
        sPath = sPath.replace("\\","/")
        if sPath[len(sPath)-1] !='/':
            sPath=sPath+'/';
        L= os.listdir(sPath)
        for s in L:
            s1=sPath+s
            if isDir(s1):
                ret.append(s)
    return ret
#从全路径文件名中提取文件的目录
def getFilePath( sPath ):
    t_path,t_filename = os.path.split( sPath )
    n=len(t_path)
    if n>0:
        t_path = t_path.replace("/","\\")
        if t_path[-1]!="\\":
            t_path = t_path+"\\"
    return t_path

#从全路径文件名中提取文件名
def getFileName( sPath ):
    t_path,t_filename = os.path.split( sPath )
    return t_filename

#从文件名中提取文件的扩展名
def getFileExt( sPath ):
    t ,t_ext = os.path.splitext( sPath )
    return t_ext

#创建子目录
#返回值： True =成功 ， False = 创建子目录失败
def createDir( sDir):
    ret = True
    try:
        os.makedirs( sDir)
    except:
        ret =False
        if isDir( sDir ):
            ret = True
        else:
            print("\r\n错误信息：\r\n",sys.exc_info()[0],"\r\n")
    return ret
        
#删除文件
#返回值： True =删除文件成功 ，
#        False = 无法删除文件
def killFile( filename):
    ret = True 
    if isFile( filename):
        try:
            os.remove(filename)
        except:
            ret = False
            print("\r\n错误信息：\r\n",sys.exc_info()[0],"\r\n")
    return ret

#复制文件
#入口:
#        srcFileName  源文件名
#        targFileName 目标文件名
#返回值： True = 文件复制成功 ，
#        False = 文件复制失败
def copyFile( srcFileName, targFileName):
    if not isFile(srcFileName):
        print("源文件不存在：",srcFileName)
        return False
    fpath,fname=os.path.split(targFileName)
    if not isDir(fpath):
        createDir(fpath)         
    if not isDir(fpath):
        print("无法创建目标文件夹:",fpath)
        return False
    try:
        shutil.copyfile(srcFileName,targFileName)
        ret = True
    except:
        ret = False
        print("\r\n错误信息：\r\n",sys.exc_info()[0],"\r\n")
    return ret


#文件改名
#返回值： True = 文件改名成功 ，
#        False = 文件改名失败
def renameFile( oldFileName, newFileName):
    ret = True
    sp1,sname1=os.path.split( oldFileName )
    sp2,sname2=os.path.split( newFileName )
    sp1= os.path.realpath(sp1)
    sp2= os.path.realpath(sp2)
    sp1 =sp1.lower()
    sp2 =sp2.lower() 
    sname1 = sname1.lower()
    sname2 = sname2.lower()
    if sp1==sp2 and sname1==sname2:
        return ret
    if not isFile(oldFileName):
        ret = False
    else:
        try:
            if sp1==sp2:
                os.rename(oldFileName,newFileName)
            else:
                if not isDir(sp2):
                    createDir(sp2)
                if not isDir(sp2):
                    print("无法创建目标文件夹:",sp2)
                if isFile( newFileName):
                    killFile(newFileName)
                shutil.move(oldFileName,newFileName)             
        except:
            ret =False
            print("\r\n错误信息：\r\n",sys.exc_info()[0],"\r\n")
    return ret


        


#以下为测试代码：
if __name__ == "__main__":
    s="c:\\xyz\\123.txt"
    print( "文件全路径名=",s)
    print( "文件夹名=", getFilePath(s))
    print( "文件名=  ", getFileName(s))
    print( "文件扩展名=", getFileExt(s))
    
    
