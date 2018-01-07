# 引入json库
import json

# 定义列表
names = ['John', ['Johnny', 'Jack'], 'Michael', ['Mike', 'Mikey', 'Mick']]
# 输出结果
print(type(names))

# 输出为json字符串
to_transfer = json.dumps(names)
# 打印
print(type(to_transfer))

from_transfer = json.loads(to_transfer)
# 打印
print(type(from_transfer))

# 打印原始数据
print(type(names))

