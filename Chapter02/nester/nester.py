# 导入sys模块
import sys
#递归打印list集合内容
def print_lol(the_list, indent=False, level=0, pFile=sys.stdout):
	#取出集合中的数据项并判断数据项是否为集合
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, indent, level+1, pFile)
		else:
			if indent:
				for num in range(level):
					print('\t', end='', file = pFile)
			print(each_item, file = pFile)
