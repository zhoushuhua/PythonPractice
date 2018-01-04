# 定义集合
james=[]
julie=[]
mikey=[]
sarah=[]

# 读取数据
try:
        # 读取数据
        with open('james.txt') as jamesFile,open('julie.txt') as julieFile,open('mikey.txt') as mikeyFile,open('sarah.txt') as sarahFile:
                        
                for each_line in jamesFile:
                        james = each_line.split(',')
                index = len(james);
                while not index < 0:
                        index = index - 1
                        james[index]=james[index].strip()
                        
                for each_line in julieFile:
                        julie = each_line.split(',')
                index = len(julie);
                while not index < 0:
                        index = index - 1
                        julie[index]=julie[index].strip()
                        
                for each_line in mikeyFile:
                        mikey = each_line.split(',')
                index = len(mikey);
                while not index < 0:
                        index = index - 1
                        mikey[index]=mikey[index].strip()
                        
                for each_line in sarahFile:
                        sarah = each_line.split(',')
                index = len(sarah);
                while not index < 0:
                        index = index - 1
                        sarah[index]=sarah[index].strip()
        print(james)
        print(julie)
        print(mikey)
        print(sarah)
except IOError as error:
        print("IOError:" + str(error))
