# 数据管理（存储和获取）
import pickle
from athletelist import AthleteList

# 从文本文件中获取数据
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        # 读取数据
        tmp_list = data.strip().split(",");
        # 返回字典数据
        return(AthleteList(tmp_list.pop(0), tmp_list.pop(0), tmp_list))
    except IOError as error:
        print('File error:'+str(error))
    # 返回空数据
    return(None)

# 存储数据 参数是一个文件名列表
def put_to_store(filename_list):
    store_data = {}
    # 循环集合取出姓名
    for each_name in filename_list:
        athlete = get_coach_data(each_name)
        store_data[athlete.name] = athlete
    print(store_data)
        
    try:
        # 打开数据文件
        with open('store_data.pkl', 'wb') as store_file:
            # 存储数据
            pickle.dump(store_data, store_file)
    except IOError as error:
        print("Write pickle data error:" + str(error))
    return(store_data)
    
# 获取数据
def get_from_store():
    store_data = {}
    try:
        # 打开数据文件
        with open('store_data.pkl', 'rb') as store_data:
            # 存储数据
            store_data = pickle.load(store_data)
    except IOError as error:
        print("Write pickle data error:" + str(error))
    return(store_data)

# 返回选手列表（以字符串返回）
def get_names_from_store():
    # 获取数据
    athlete_list = get_from_store()
    # 使用列表推导返回姓名集合
    name_list = [athlete_list[e_i].name for e_i in athlete_list]
    # 返回姓名集合
    return(name_list)
