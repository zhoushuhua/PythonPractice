# 导入sqlite3
import sqlite3
import glob
import athletemodel

# 连接数据库文件
connection = sqlite3.connect('coachdata.sqlite')

# 创建游标
cursor = connection.cursor()

# 查询当前时间
# cursor.execute("""DROP TABLE athletes""")
# cursor.execute("""DROP TABLE timing_data""")
cursor.execute("""CREATE TABLE athletes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    name TEXT NOT NULL,
                    dob DATE NOT NULL)""")
cursor.execute("""CREATE TABLE timing_data(  
                    athlete_id INTEGER NOT NULL,
                    value Text NOT NULL,
                    FOREIGN KEY (athlete_id) REFERENCES athletes)""")

# 提价执行命令
connection.commit()

# 初始化athletes表
# 扫描文件
data_files = glob.glob("webapp/data/*.txt")
# 获取选手和数据值
athletes = athletemodel.put_to_store(data_files)
# 新增到数据库中
for athlete in athletes:
    cursor.execute("INSERT INTO athletes(name, dob) values(?, ?)", (athletes[athlete].name, athletes[athlete].dob))

# 提价执行命令
connection.commit()

# 初始化timing_data表
cursor.execute("SELECT id,name FROM athletes")

# 提价执行命令
connection.commit()

# 查询数据
for (a_id, name) in cursor.fetchall():
    # 获取数据
    for timing in athletes[name].clean_data:
        # 新增数据
        cursor.execute("INSERT INTO timing_data(athlete_id, value) values(?, ?)", (a_id, timing))
    #提交数据
    connection.commit()

# 查询数据
cursor.execute("SELECT athlete_id, value From timing_data")
connection.commit()
print(cursor.fetchall())
# 关闭连接
connection.close()
