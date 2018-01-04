# 定义类
class Athlete:
        # 初始化对象
        def __init__(self, a_name, a_dob=None, a_times=[]):
                # The code initialize object
                self.name = a_name
                self.dob=a_dob
                self.times=a_times

# 初始化类
sarah = Athlete('Sarah Sweeney', '2002-6-17', ["2:58", "2.58", "1.56"])
james = Athlete("James Jones")
# 引用变量类型
print(type(sarah))
print(type(james))
# 引用变量内存地址
print(sarah)
print(james)
# 打印变量
print(sarah.name)
print(sarah.dob)
print(sarah.times)
print('---------------------------------')
print(james.name)
print(james.dob)
print(james.times)
