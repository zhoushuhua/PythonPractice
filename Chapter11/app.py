from find_it import find_closest
from tm2secs2tm import format_time,secs2time,time2secs
import android

# 查找最接近的时间
def find_nearest_time(look_for, target_list):
    # 格式化查询数据
    look_for = time2secs(format_time(look_for))
    target_list = [time2secs(format_time(each_item)) for each_item in target_list]
    return(secs2time(find_closest(look_for, target_list)))

# 定义选择数据集
distances = ["2mi", "5k", "5mi", "15k", "10mi", "20k", "13.1mi", "25k", "30k", "Marathon"]
hello_msg = "Welcome to the Marathon Club's app"
quit_msg = "Quiting the Matathon Club's App."


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
            inner_dict[format_time(row[i])] = column_headings[i]
        # 将数据与列标题关联
        row_data[row_label] = inner_dict

# 提示数据输入
# distance_run = input("Enter the distance attempted:")
# recorded_time = input("Enter the recorded time:")
# predicted_distance = input("Enter the distance you want a prediction for:")

# closest_time = find_nearest_time(recorded_time, row_data[distance_run])
# closest_column_heading = row_data[distance_run][closest_time]
# prediction = [k for k in row_data[predicted_distance].keys()
#                   if row_data[predicted_distance][k] == closest_column_heading]

# print("The predicted time running " + predicted_distance + "is:" + prediction[0])

app = android.Android()

def status_update(msg, how_long = 2):
    app.makeToast(msg)
    time.sleep(how_long)

# 创建弹出框
def do_dialog(title, data, func, ok = "Select", notok = "Quit"):
    app.dialogCreateAlert(title)
    func(data)
    app.dialogSetPositiveButtonText(ok)
    if notok is not None:
        app.dialogSetNegativeButtonText(notok)
    app.dialogShow()
    return(app.dialogGetResponse().result)

status_update(hello_msg)
# 创建
resp = do_dialog("Pick a distance", distances, app.dialogSetSingleChoiceItem)
if resp["which"] in ["positive"]:
    distance_run = app.dialogGetSelectedItems().result[0]
    distance_run = distances[distance_run]
    records_time = app.dialogGetInput("Enter a " + distance_run + " time:", "Use HH:MM:SS format:").result

    closest_time = find_nearest_time(format_time(records_time), row_data[distance_run])
    closest_column_heading = row_data[distance_run][closest_time]
    resp = do_dialog("Pick a distance to predict", distances, app.dialogSetSingleChoiceItem)
    if resp["which"] in ["positive"]:
        predicted_distance = app.dialogGetSelectedItems().result[0]
        predicted_distance = distances[distance_run]
        prediction = [k for k in row_data[predicted_distance].keys()
                          if row_data[predicted_distance][k] == closest_column_heading]
        do_dialog("The predicted time runing " + predicted_distance + " is:", prediction, app.dialogSetItems, "OK", None)
        
status_update(quit_msg)
