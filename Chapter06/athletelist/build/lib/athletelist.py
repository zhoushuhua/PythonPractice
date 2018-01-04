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
