import find_it
import tm2secs2tm

# 查找最接近的时间
def find_nearest_time(look_for, target_list):
    # 格式化查询数据
    look_for = tm2secs2tm.time2secs(tm2secs2tm.format_time(look_for))
    target_list = [tm2secs2tm.time2secs(tm2secs2tm.format_time(each_item)) for each_item in target_list]
    return(tm2secs2tm.secs2time(find_it.find_closest(look_for, target_list)))


# 定义字典信息
row_data = {}
# 获取个数据
with open("PaceData.csv") as paces:
    # 先获取标题
    column_headings = paces.readline().strip().split(",")
    # 去掉第一个数据
    column_headings.pop(0)
    # 循环获取数据
    for each_line in paces:
        row = each_line.strip().split(",")
        row_label = row.pop(0)
        # 定义内部字典
        inner_dict = {}
        for i in range(len(row)):
            inner_dict[tm2secs2tm.format_time(row[i])] = column_headings[i]
        # 将数据与列标题关联
        row_data[row_label] = inner_dict

# 提示数据输入
distance_run = input("Enter the distance attempted:")
recorded_time = input("Enter the recorded time:")
predicted_distance = input("Enter the distance you want a prediction for:")

closest_time = find_nearest_time(recorded_time, row_data[distance_run])
closest_column_heading = row_data[distance_run][closest_time]
prediction = [k for k in row_data[predicted_distance].keys()
                  if row_data[predicted_distance][k] == closest_column_heading]

print("The predicted time running " + predicted_distance + "is:" + prediction[0])
