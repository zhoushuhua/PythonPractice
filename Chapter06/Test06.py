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

# 获取文件数据 并将 数据 按照“,”分隔成列表返回
def get_coach_data(filename):
        try:
                with open(filename) as f:
                        data = f.readline()
                        # 读取数据
                        tmp_list = data.strip().split(",");

                        # 返回字典数据
                        return({
                                'Name':tmp_list.pop(0),
                                'DOB':tmp_list.pop(0),
                                'Times':sorted([sanitize(each_item) for each_item in tmp_list]),
                                'FTimes':sorted(set([sanitize(each_item) for each_item in tmp_list]))[0:3]
                                })
        except IOError as error:
                print('File error:'+str(error))
                return(None)

# 读取数据
try:
        # 获取sarah个人资料及成绩数据
        james_dict = get_coach_data('james.txt')
        # 获取sarah个人资料及成绩数据
        julie_dict = get_coach_data('julie.txt')
        # 获取sarah个人资料及成绩数据
        mikey_dict = get_coach_data('mikey.txt')
        # 获取sarah个人资料及成绩数据
        sarah_dict = get_coach_data('sarah.txt')
        
        # 打印数据
        print(james_dict['Name']+"'s fastest times are: "+str(james_dict['FTimes']))
        print(julie_dict['Name']+"'s fastest times are: "+str(julie_dict['FTimes']))
        print(mikey_dict['Name']+"'s fastest times are: "+str(mikey_dict['FTimes']))
        print(sarah_dict['Name']+"'s fastest times are: "+str(sarah_dict['FTimes']))
except IOError as error:
        print("IOError:" + str(error))
 


