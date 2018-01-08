# 响应json数据
import json
import yate
import athletemodel
# import cgitb

# 打开调试 html错误显示
# cgitb.enable()

# 返回姓名
names = athletemodel.get_namesID_from_store()

# 设置响应格式
print(yate.start_response("application/json"))

# 返回数据
print(json.dumps(names))
