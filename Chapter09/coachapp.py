import android  # 导入android
import json     # json库
import time     # 时间库

from urllib import urlencode    #
from urllib2 import urlopen     #

hello_msg = "Welcome to coach Kelly's Timing App"
list_title = "Here is your list of athletes:"
quit_msg = "Quiting coach Kelly's App."
web_server = "http://192.168.25.76:8080"
# 获取姓名列表
get_name_cgi = "/cgi-bin/generate_names.py"

# 向服务器请求数据
def send_to_server(url, post_data=None):
    if post_data:
        page = urlopen(url, urlencode(post_data))
    else:
        page = urlopen(url)
    return(page.read().decode("utf8"))

# 创建Android对象
app = android.Android()

# 更新状态函数
def status_update(msg, how_long = 2):
    app.makeToast(msg)
    time.sleep(how_long)

# 显示提示信息
status_update(hello_msg)
# 获取选手列表名字
athlete_names = json.loads(send_to_server(web_server + get_name_cgi))
# 创建弹出框
app.dialogCreateAlert(list_title)
app.dialogSetSingleChoiceItems(athlete_names)
app.dialogSetPositiveButtonText('Select')
app.dialogSetNegativeButtonText('Quit')
app.dialogShow()

# 获取选中结果
resp = app.dialogGetResponse().result

# 判断是否选中了某个选手
if resp['which'] in ('positive'):
    
    # 获取数据对象
    get_data_cgi = "/cgi-bin/generate_data.py"
    # 返回选中列表的索引信息
    selected_athlete = app.dialogGetSelectedItems().result[0]
    # 获取对应的选手姓名
    which_athlete = athlete_names[selected_athlete]
    
    # 向服务器请求数据
    athlete = json.loads(send_to_server(web_server + get_data_cgi, {"which_athlete" : which_athlete}))
    # 弹出框提示信息
    athlete_title = athlete['name'] + "(" + athlete['DOB'] + ") top3  times:"
    app.dialogCreateAlert(athlete_title)
    app.dialogSetItems(athlete['top3'])
    app.dialogSetPositiveButtonText("OK")
    app.dialogShow()

    # 等待用户点击
    resp = app.dialogGetResponse().result

# 显示退出提示信息
status_update(quit_msg)
