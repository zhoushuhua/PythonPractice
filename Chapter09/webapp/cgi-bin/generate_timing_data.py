import cgitb
import cgi
import yate
import athletemodel

# 打开错误提示
cgitb.enable()
# 获取请求表单
form_data = cgi.FieldStorage()
# 获取选手主键
athlete_id = form_data["which_athlete"].value
# 获取选手
athlete = athletemodel.get_athlete_from_id(athlete_id)
# 响应文件类型
print(yate.start_response())
# html头
print(yate.include_header("NUAC's Timing Data"))
# 提示数据
print(yate.header("Athlete:" + athlete["Name"] + ",DOB：" + athlete["DOB"]))
# 打印提示数据
print(yate.para("The top times for this athlete are:"))
# 打印数据集合
print(yate.u_list(athlete["top3"]))
# 打印数据
print(yate.para("The entire set of timing data is:" + str(athlete["data"]) + ".(duplicates removed)."))
# html尾
print(yate.include_footer({"Home":"/index.html", "Select another athlete":"/cgi-bin/generate_list.py"}))

