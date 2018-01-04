import os
# 获取当前目录
os.getcwd()
# 切换目录
os.chdir('D:\\WS\\Python\\Chapter03')
# 重新获取目录
os.getcwd()
fileName = 'sketch011.txt'
# 读取数据
try:
        data = open(fileName)
        # 循环读取文件
        for each_line in data:
                try:
                        (role, line_spoken) = each_line.split(':', maxsplit=1)
                        print(role, end = '')
                        print(' said ', end = '')
                        print(line_spoken, end = '')
                except:
                        pass #print(each_line)
        # 关闭文件
        data.close()
except:
        print("The data file is missing!")
