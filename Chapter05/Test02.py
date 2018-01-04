# 定义集合
james=[]
julie=[]
mikey=[]
sarah=[]

# 定义函数
def sanitize(time_string):
        if '-' in time_string:
                splitter= '-'
        elif ':' in time_string:
                splitter= ':'
        else:
                return(time_string)
        (mins, secs) = time_string.split(splitter, maxsplit = 1)
        return(mins+'.'+secs)

# 读取数据
try:
        # 读取数据
        with open('james.txt') as jamesFile:
                james = jamesFile.readline().strip().split(",");
        with open('julie.txt') as julieFile:
                julie = julieFile.readline().strip().split(",");
        with open('mikey.txt') as mikeyFile:
                mikey = mikeyFile.readline().strip().split(",");
        with open('sarah.txt') as sarahFile:
                sarah = sarahFile.readline().strip().split(",");

        # 转换时间格式
        i = len(james)
        while not i < 1 :
                i = i - 1;
                james[i] = sanitize(james[i])
        i = len(julie)
        while not i < 1 :
                i = i - 1;
                julie[i] = sanitize(julie[i])
        i = len(mikey)
        while not i < 1 :
                i = i - 1;
                mikey[i] = sanitize(mikey[i])
        i = len(sarah)
        while not i < 1 :
                i = i - 1;
                sarah[i] = sanitize(sarah[i])
                

        # 排序
        jamesBk = sorted(james, reverse=True)
        print(james)
        print(jamesBk)
        julieBk = sorted(julie, reverse=True)
        print(julie)
        print(julieBk)
        mikeyBk = sorted(mikey, reverse=True)
        print(mikey)
        print(mikeyBk)
        sarahBk = sorted(sarah, reverse=True)
        print(sarah)
        print(sarahBk)
except IOError as error:
        print("IOError:" + str(error))
 


