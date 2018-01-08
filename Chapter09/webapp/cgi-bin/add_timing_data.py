#! /usr/local/bin/python3(Linux环境重要)

import os
import cgi
import time
import sys
import yate
import cgitb

# 打开错误提示
cgitb.enable()

# 显示
print(yate.start_response("text/plain"))
# 获取请求信息
addr = os.environ["REMOTE_ADDR"]
host = os.environ["REMOTE_HOST"]
method = os.environ["REQUEST_METHOD"]

# 当前时间
cur_time = time.asctime(time.localtime())
print(host+ "," + addr + "," + cur_time + ":" + method + ":", end='', file=sys.stderr)

# 获取输入数据
form_data = cgi.FieldStorage()
for each_form_item in form_data.keys():
    print(each_form_item + '->' + form_data[each_form_item].value, end = '', file = sys.stderr)

# 换行
print(file=sys.stderr)
print("OK.")
