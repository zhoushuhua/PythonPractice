import athletemodel
import yate
import glob
import cgitb

# 打开错误调试
cgitb.enable()

# 获取选手
athlete_names = athletemodel.get_namesID_from_store()
# 打印响应信息
print(yate.start_response())
# 加载html头部
print(yate.include_header("NUAC's List of Athletes"))
# 加载表单开始部分
print(yate.start_form("generate_timing_data.py"))
# 打印提示
print(yate.para("Select an athlete from the list to work with:"))

# 利用For循环加载单选按钮
for athlete_name in athlete_names:
    print(yate.radio_button("which_athlete", str(athlete_name["id"]), athlete_name["name"]))
# 加载表单结束部分
print(yate.end_form("Select"))

print(yate.include_footer({"Home":"/index.html"}))
