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

# 读取成绩
def readScore(fileName):
        try:
                with open(fileName) as file:
                        return(file.readline().strip().split(","))
        except IOError as error:
                print("IOError  " + fileName + ":" + str(error))
                return(None)

# 读取数据
try:
        # 读取数据
        james = readScore('james.txt');
        julie = readScore('julie.txt');
        mikey = readScore('mikey.txt');
        sarah = readScore('sarah.txt');

        # 使用列表推导同意数据格式并排序
        james = [sanitize(each_item) for each_item in james]
        julie = [sanitize(each_item) for each_item in julie]
        mikey = [sanitize(each_item) for each_item in mikey]
        sarah = [sanitize(each_item) for each_item in sarah]

        # 使用列表推导统一格式后排序
        print(james)
        print(julie)
        print(mikey)
        print(sarah)
        print('-----------------------------------------------------')

        # 去除重复的数据
        unique_james = set(james)
        unique_julie = set(julie)
        unique_mikey = set(mikey)
        unique_sarah = set(sarah)

        # 去重后的数据
        print(unique_james)
        print(unique_julie)
        print(unique_mikey)
        print(unique_sarah)
        print('-----------------------------------------------------')
                        
        # 取去重复数据后的前3项数据(列表分片)
        print(sorted(unique_james)[0:3])
        print(sorted(unique_julie)[0:3])
        print(sorted(unique_mikey)[0:3])
        print(sorted(unique_sarah)[0:3])
        print('-----------------------------------------------------')
except IOError as error:
        print("IOError:" + str(error))
 


