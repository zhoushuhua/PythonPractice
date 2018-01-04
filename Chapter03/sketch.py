import os
# 获取当前目录
os.getcwd()
# 切换目录
os.chdir('D:\\WS\\Python\\Chapter03')
# 重新获取目录
os.getcwd()
# 读取数据
data = open('sketch01.txt')
# 循环读取文件
for each_line in data:
        if each_line.find(':') != -1:
                (role, line_spoken) = each_line.split(':', maxsplit=1)
                print(role, end = '')
                print(' said ', end = '')
                print(line_spoken, end = '')
        else:
                print(each_line)
# 关闭文件
data.close()
