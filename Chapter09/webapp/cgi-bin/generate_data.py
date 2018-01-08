# 响应json数据
import json
import yate
import athletemodel
import cgi

# 获取请求数据
form_data = cgi.FieldStorage()
# 获取请求数据结果
athlete_id = form_data['which_athlete'].value
# 获取数据
athlete = athletemodel.get_athlete_from_id(athlete_id)

# 设置响应格式
print(yate.start_response("application/json"))
# 返回数据
print(json.dumps(athlete))
