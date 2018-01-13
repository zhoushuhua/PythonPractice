# 测试作用域
name = "Head First Python"

def what_happens_here():
    global name # 声明访问全局变量
    print(name)
    name = name + " is a great book！"
    print(name)

# 调用函数
what_happens_here()
# 打印全局变量
print(name)

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
# else:
#     print("__name__ is not equal __main__")

phone_number = "Home:(555)265-2901"
start = phone_number.find("(")
start = start + 1
end = start + 3
area_code = phone_number[start:end]
print("The area code is:" + area_code)

# 使用正则表达式取出区号
import re
results = re.search("\((\d{3})\)", phone_number)
area_code2 = results.group(1)
print("The area code2 is:" + area_code)
