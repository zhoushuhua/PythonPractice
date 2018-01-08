# 导入sqlite3
import sqlite3

# 连接数据库文件
conn = sqlite3.connect('test.sqlite')

# 创建游标
cursor = conn.cursor()

# 查询当前时间
cursor.execute("""SELECT DATE('NOW')""")

# 提价执行命令
conn.commit()

# 关闭连接
conn.close()
