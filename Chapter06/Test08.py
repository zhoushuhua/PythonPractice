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

# 定义类
class Athlete:
        # 初始化对象
        def __init__(self, a_name, a_dob=None, a_times=[]):
                # The code initialize object
                self.name = a_name
                self.dob = a_dob
                self.times = a_times
        # 获取最快的三次时间
        def top3(self):
                return(sorted(set([sanitize(each_item) for each_item in self.times]))[0:3])

        # 向时间列表追加一个数据
        def add_time(self, time_value):
                self.times.append(time_value)

        # 向时间列表追加一个数据列表
        def add_times(self, list_of_times):
                self.times.extend(list_of_times)

# 获取文件数据 并将 数据 按照“,”分隔成列表返回
def get_coach_data(filename):
        try:
                with open(filename) as f:
                        data = f.readline()
                        # 读取数据
                        tmp_list = data.strip().split(",");

                        # 返回字典数据
                        return(Athlete(tmp_list.pop(0),
                                       tmp_list.pop(0),
                                       tmp_list))
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
james.add_time("1.2");
james.add_times(["2.01", "2.02", "1.8"])

print(james.name + "'s fastest times are: " + str(james.times))
print(james.name + "'s fastest times are: " + str(james.top3()))
