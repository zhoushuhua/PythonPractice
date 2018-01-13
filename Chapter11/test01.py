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
        row_data[row_label] = row

num_cols = len(column_headings)
print(num_cols, end=' -> ')
print(column_headings)

num_2mi = len(row_data["2mi"])
print(num_2mi, end = '->')
print(row_data["2mi"])

num_Marathon = len(row_data["Marathon"])
print(num_Marathon, end = '->')
print(row_data["Marathon"])









