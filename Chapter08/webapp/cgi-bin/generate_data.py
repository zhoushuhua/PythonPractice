# 响应json数据
import json
import yate
import athletemodel
import cgi

# 返回姓名
athletes = athletemodel.get_from_store()
# 获取请求数据
form_data = cgi.FieldStorage()
# 获取请求数据结果
athlete_name = form_data['which_athlete'].value

# 设置响应格式
print(yate.start_response("application/json"))
# 返回数据
print(json.dumps(athletes[athlete_name].to_dict))
