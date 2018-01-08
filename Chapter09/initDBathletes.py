# 导入sqlite3
import sqlite3
import glob
import athletemodel

# 连接数据库文件
connection = sqlite3.connect('coachdata.sqlite')

# 创建游标
cursor = connection.cursor()

# 扫描文件
data_files = glob.glob("webapp/data/*.txt")
# 获取选手和数据值
athletes = athletemodel.put_to_store(data_files)
# 新增到数据库中
for athlete in athletes:
    cursor.execute("INSERT INTO athletes(name, dob) values(?, ?)", (athletes[athlete].name, athletes[athlete].dob))

# 提价执行命令
connection.commit()

# 关闭连接
connection.close()
