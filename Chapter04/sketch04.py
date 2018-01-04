import os
# 获取当前目录
os.getcwd()
# 切换目录
os.chdir('D:\\WS\\Python\\Chapter04')
# 重新获取目录
os.getcwd()
# 读取数据
try:
        with open('out.txt', 'w') as out_file:
                print('Test with……', file=out_file)

        print("Finished!")
except IOError as error:
        print("file error:" + str(error))
