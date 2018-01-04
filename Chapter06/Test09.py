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

# 定义类AthleteList并继承至list
class AthleteList(list):
        # 初始化对象
        def __init__(self, a_name, a_dob=None, a_times=[]):
                # The code initialize object
                list.__init__([])
                self.name = a_name
                self.dob = a_dob
                self.extend(a_times)
        # 获取最快的三次时间
        def top3(self):
                return(sorted(set([sanitize(each_item) for each_item in self]))[0:3])

# 获取文件数据 并将 数据 按照“,”分隔成列表返回
def get_coach_data(filename):
        try:
                with open(filename) as f:
                        data = f.readline()
                        # 读取数据
                        tmp_list = data.strip().split(",");
                        # 返回字典数据
                        return(AthleteList(tmp_list.pop(0), tmp_list.pop(0), tmp_list))
        except IOError as error:
                print('File error:'+str(error))
                return(None)

# 获取sarah个人资料及成绩数据
james = get_coach_data('james.txt')
# 获取sarah个人资料及成绩数据
julie = get_coach_data('julie.txt')
# 获取sarah个人资料及成绩数据
mikey = get_coach_data('mikey.txt')
# 获取sarah个人资料及成绩数据
sarah = get_coach_data('sarah.txt')

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))

print("新功能测试：")

# 测试新功能
james.append("1.2");
james.extend(["2.01", "2.02", "1.8"])

print(james.name + "'s fastest times are: " + str(james))
print(james.name + "'s fastest times are: " + str(james.top3()))
