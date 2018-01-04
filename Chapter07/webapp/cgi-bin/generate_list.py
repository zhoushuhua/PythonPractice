import athletemodel
import yate
import glob

# 查询文件列表
data_files = glob.glob("data/*.txt")
athletes = athletemodel.put_to_store(data_files)
# 打印响应信息
print(yate.start_response())
# 加载html头部
print(yate.include_header("Coach Kelly's List of Athletes"))
# 加载表单开始部分
print(yate.start_form("generate_timing_data.py"))
# 打印提示
print(yate.para("Select an athlete from the list to work with:"))

# 利用For循环加载单选按钮
for each_athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))
# 加载表单结束部分
print(yate.end_form("Select"))

print(yate.include_footer({"Home":"/index.html"}))
