# 导入db模块
from google.appengine.ext import db

# 生日详细信息
class BirthDetails(db.Model):
    name = db.StringProperty()
    date_of_birth = db.DateProperty()
    time_of_birth = db.TimeProperty()
