import os
# 获取当前目录
os.getcwd()
# 切换目录
os.chdir('D:\\WS\\Python\\Chapter04')
# 重新获取目录
os.getcwd()
fileName = 'sketch0.txt'
# 定义空列表
man=[]
other=[]
# 读取数据
try:
        data = open(fileName)
        # 循环读取文件
        for each_line in data:
                try:
                        (role, line_spoken) = each_line.split(':', maxsplit=1)
                        # 将line_spoken请前后的空格删除
                        line_spoken = line_spoken.strip()
                        if role == 'Man':
                                man.append(line_spoken)
                        elif role == 'Other Man':
                                other.append(line_spoken)
                except ValueError:
                        pass #print(each_line)
except IOError as error:
        print("The data file is missing:" + str(error))
finally:
        # 关闭
        if 'data' in locals():
                data.close()
