import os
# 获取当前目录
os.getcwd()
# 切换目录
os.chdir('D:\\WS\\Python\\Chapter04')
# 重新获取目录
os.getcwd()
fileName = 'sketch.txt'
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
        # 关闭文件
        data.close()
except IOError:
        print("The data file is missing!")
        
# 完成数据处理有重新保存数据
try:
        # 初始化文件
        man_file = open('man_data.txt', 'w')
        other_file = open('other_data.txt', 'w')
        # 写数据
        print(man, file = man_file)
        # 写数据
        print(other, file = other_file)
        # 显示已经成功写完数据
        print("Finished!")
except IOError:
        print("Write data to file error!")
finally:
        # 刷新数据缓冲区（将缓冲区中的数据写入磁盘）
        if 'man_file' in locals():
                man_file.close()
        if 'other_file' in locals():
                other_file.close()
