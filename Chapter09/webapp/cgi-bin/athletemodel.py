# 数据管理（存储和获取）
import sqlite3

# 数据库名称
db_name = "coachdata.sqlite"

# 获取姓名
def get_names_from_store():

    # 打开连接
    conn = sqlite3.connect(db_name)
    # 打开游标
    cursor = conn.cursor()
    # 查询命令
    results = cursor.execute("""SELECT name From athletes""")
    # 提交查询命令
    conn.commit()
    # 返回结果
    names = [row[0] for row in results.fetchall()]
    # 关闭连接
    conn.close()
    # 返回结果
    return(names)

def get_namesID_from_store():

    # 打开连接
    conn = sqlite3.connect(db_name)
    # 打开游标
    cursor = conn.cursor()
    # 查询命令
    results = cursor.execute("""SELECT id,name From athletes""")
    # 提交查询命令
    conn.commit()
    # 返回结果
    names_ids = [{"id": row[0], "name": row[1]} for row in results.fetchall()]
    # 关闭连接
    conn.close()
    # 返回结果
    return(names_ids)

# 获取选手详细信息
def get_athlete_from_id(athlete_id):
    # 打开连接
    conn = sqlite3.connect(db_name)
    # 打开游标
    cursor = conn.cursor()
    # 查询命令
    results = cursor.execute("""SELECT name, dob FROM athletes WHERE id = ?""", (athlete_id))
    # 提交
    conn.commit()
    # 返回姓名和生日
    (name, dob) = results.fetchone()
    # 查询时间
    results = cursor.execute("""SELECT value From timing_data WHERE athlete_id = ?""", (athlete_id))
    # 提交
    conn.commit()
    # 获取时间数据
    times = [row[0] for row in results.fetchall()]
    # 关闭连接
    conn.close()
    # 最终返回结果
    return({
        "Name" : name,
        "DOB": dob,
        "data" : times,
        "top3" : sorted(times)[0:3]
        })
