# 响应json数据
import json
import yate
import athletemodel
import cgi

# 获取请求数据
form_data = cgi.FieldStorage()
# 获取请求数据结果
sel_athlete = form_data['which_athlete'].value

# 返回姓名
athletes = athletemodel.get_from_store()

# 设置响应格式
print(yate.start_response("application/json"))

# 返回数据
print(json.dumps(athletes[sel_athlete]))
