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

        # 使用列表推导同意数据格式并排序
        james = sorted([sanitize(each_item) for each_item in james])
        julie = sorted([sanitize(each_item) for each_item in julie])
        mikey = sorted([sanitize(each_item) for each_item in mikey])
        sarah = sorted([sanitize(each_item) for each_item in sarah])

        # 使用列表推导统一格式后排序
        print(james)
        print(julie)
        print(mikey)
        print(sarah)
        print('-----------------------------------------------------')

        # 去除重复的数据
        unique_james = []
        for each_item in james:
                if each_item not in unique_james:
                        unique_james.append(each_item)
                        
        unique_julie = []
        for each_item in julie:
                if each_item not in unique_julie:
                        unique_julie.append(each_item)
                        
        unique_mikey = []
        for each_item in mikey:
                if each_item not in unique_mikey:
                        unique_mikey.append(each_item)
                        
        unique_sarah = []
        for each_item in sarah:
                if each_item not in unique_sarah:
                        unique_sarah.append(each_item)

        # 去重后的数据
        print(unique_james)
        print(unique_julie)
        print(unique_mikey)
        print(unique_sarah)
        print('-----------------------------------------------------')
                        
        # 取去重复数据后的前3项数据(列表分片)
        print(unique_james[0:3])
        print(unique_julie[0:3])
        print(unique_mikey[0:3])
        print(unique_sarah[0:3])
        print('-----------------------------------------------------')
except IOError as error:
        print("IOError:" + str(error))
 


