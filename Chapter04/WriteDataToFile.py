import os
# 获取当前目录
os.getcwd()
# 切换目录
os.chdir('D:\\WS\\Python\\Chapter04')
# 重新获取目录
os.getcwd()
fileName = 'outdata.txt'
try:
	#打开文件
        outfile = open(fileName, 'w')
        print('Test Write Data To File', file=outfile)
        # 刷新缓冲区到到磁盘
        outfile.close()
        # 输出完成提示
        print('Finshed Write Data To File!')
except IOError:
        print("The data file is missing!")
