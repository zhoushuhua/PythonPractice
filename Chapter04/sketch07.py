# 导入模块
import os
import pickle
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
        with open(fileName) as data: 
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
except IOError:
        print("The data file is missing!")
        
# 完成数据处理有重新保存数据
try:
        # 初始化文件
        with open('man_data.txt', 'wb') as man_file,open('other_data.txt', 'wb') as other_file: 
                # 写数据
                pickle.dump(man, man_file)
                # 写数据
                pickle.dump(other, other_file)
        # 显示已经成功写完数据
        print("Finished!")
except IOError:
        print("Write data to file error!")
except pickle.PickleError as perr:
        print("Pickling error:"+str(perr))
