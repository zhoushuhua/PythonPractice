#! /usr/local/bin/python3(Linux环境重要)

# import os
# import cgi
# import time
# import sys
# import yate
# import cgitb

# 打开错误提示
# cgitb.enable()

# 显示
# print(yate.start_response("text/plain"))
# 获取请求信息
# addr = os.environ["REMOTE_ADDR"]
# host = os.environ["REMOTE_HOST"]
# method = os.environ["REQUEST_METHOD"]

# 当前时间
# cur_time = time.asctime(time.localtime())
# print(host+ "," + addr + "," + cur_time + ":" + method + ":", end='', file=sys.stderr)

# 获取输入数据
# form_data = cgi.FieldStorage()
# for each_form_item in form_data.keys():
    # print(each_form_item + '->' + form_data[each_form_item].value, end = '', file = sys.stderr)

# 换行
# print(file=sys.stderr)
# print("OK.")

import cgi
import sqlite3
import yate

# 设置响应头
print(yate.start_response("text/plain"))

# 数据库名称
db_name = "coachdata.sqlite"
# 获取请求数据
form_data = cgi.FieldStorage()
# 获取ID
athlete_id = form_data["athlete_id"].value
# 获取时间
athlete_time = form_data["athlete_time"].value

# 连接数据库
conn = sqlite3.connect(db_name)
# 打开游标
cursor = conn.cursor()
# 添加数据
cursor.execute("INSERT INTO timing_data(athlete_id, value) VALUES(?,?)", (athlete_id, athlete_time))
# 提交数据
cursor.commit()
# 关闭连接
conn.close()
# 返回提示
print("OK")
