# 定义类
class Athlete:
        # 初始化对象
        def __init__(self, value=""):
                # The code initialize object
                self.thing = value
        # 返回初始化长度
        def how_big(self):
                return(len(self.thing))
print('Test')

# 使用对象
a = Athlete("Zhangsan")
b = Athlete("Lisi")

# 打印对象
print("Object A:"+str(a))
print("Object B:"+str(b))

print("Object A.howBig:"+str(a.how_big()))
print("Object B.howBig:"+str(b.how_big()))
