# 导入sqlite3
import sqlite3

# 连接数据库文件
connection = sqlite3.connect('coachdata.sqlite')

# 创建游标
cursor = connection.cursor()

# 查询当前时间
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

# 关闭连接
connection.close()
