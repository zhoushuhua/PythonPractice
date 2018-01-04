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
        clean_james = [sanitize(each_item) for each_item in james]
        clean_julie = [sanitize(each_item) for each_item in julie]
        clean_mikey = [sanitize(each_item) for each_item in mikey]
        clean_sarah = [sanitize(each_item) for each_item in sarah]
                

        # 排序
        jamesBk = sorted(clean_james, reverse=True)
        print(clean_james)
        print(jamesBk)
        julieBk = sorted(clean_julie, reverse=True)
        print(clean_julie)
        print(julieBk)
        mikeyBk = sorted(clean_mikey, reverse=True)
        print(clean_mikey)
        print(mikeyBk)
        sarahBk = sorted(clean_sarah, reverse=True)
        print(clean_sarah)
        print(sarahBk)
except IOError as error:
        print("IOError:" + str(error))
 


