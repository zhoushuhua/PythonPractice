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
                        return(data.strip().split(","))
        except IOError as error:
                print('File error:'+str(error))
                return(None)

# 读取数据
try:
        # 获取sarah个人资料及成绩数据
        sarah = get_coach_data('sarah2.txt')

        # 弹出第一个数据 姓名 弹出第二个数据 日期
        sarah_dict = {}
        (sarah_dict['Name'], sarah_dict['DOB']) = sarah.pop(0), sarah.pop(0)

        # 打印排序数据
        sarah_dict['Times'] = sarah

        # 清理数据
        print(sarah_dict['Name']+"'s fastest times are: "+str(sorted([sanitize(each_item) for each_item in sarah_dict['Times']])[0:3]))
except IOError as error:
        print("IOError:" + str(error))
 


