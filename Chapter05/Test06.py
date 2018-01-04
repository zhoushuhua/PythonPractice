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

        # 使用列表推导统一格式后排序
        print(sorted([sanitize(each_item) for each_item in james]))
        print(sorted([sanitize(each_item) for each_item in julie]))
        print(sorted([sanitize(each_item) for each_item in mikey]))
        print(sorted([sanitize(each_item) for each_item in sarah]))
except IOError as error:
        print("IOError:" + str(error))
 


