import sys
import time

import xlrd
import xlwt

# 输入条件：表格，数据在A列，无空格
# input_path = input("输入表文件绝对地址：")
# out_path = input("输出表文件绝对地址：")
# P = input("输入固定参数：")
# 创建一个workbook并设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 添加sheet
worksheet = workbook.add_sheet('new_data')

input_path = 'C:\\Users\\sqn\\Desktop\\1.xls'
out_path = 'C:\\Users\\sqn\\Desktop\\2.xls'
P = 0.576
a = float(P) * 1000 / 1000000

wb = xlrd.open_workbook(input_path)
sheet1 = wb.sheet_by_index(0)
x = sheet1.nrows
y = sheet1.ncols

try:
    if y != 1:
        sys.stdout.write("确保所有原数据都在第一列（A列）\n")
        exit(1)
    if x == 1:
        sys.stdout.write("确保有数据\n")
        exit(1)

    # 初始化值
    val = sheet1.cell_value(0, 0)
    # 当前值的个数
    count = 1
    # 当前小组的总和
    sum = val * count
    # 当前值所属大组
    group = 1
    # 当前值所属小组
    group_id = 1
    # 当前大组的总和
    sum_sum = sheet1.cell_value(0, 0)
    # 大组中，小组最后一个标记
    flag = 0

    # 写入第一行数据
    worksheet.write(0, 0, val)
    worksheet.write(0, 1, count)
    worksheet.write(0, 2, sum_sum)
    worksheet.write(0, 3, group_id)
    worksheet.write(0, 4, group)

    for i in range(1, x):
        if flag == 1:
            group += 1
            flag = 0
            sum_sum = sheet1.cell_value(i, 0)
        else:
            sum_sum += sheet1.cell_value(i, 0)
        worksheet.write(i, 0, sheet1.cell_value(i, 0))
        if sheet1.cell_value(i, 0) == sheet1.cell_value(i - 1, 0):
            count += 1
        else:
            group_id += 1
            count = 1
            val = sheet1.cell_value(i, 0)
        worksheet.write(i, 1, count)
        worksheet.write(i, 2, sum_sum)
        worksheet.write(i, 3, group_id)
        worksheet.write(i, 4, group)
        if (i == x - 1) or (group_id % 14 == 0 and sheet1.cell_value(i + 1, 0) != val):
            flag = 1
            worksheet.write(group - 1, 5, round(sum_sum * a, 3))

    workbook.save(out_path)
    sys.stdout.write("转换结束！\n")
    sys.stdout.flush()
    time.sleep(1)
except Exception as e:
    print("发生错误啦：", e)
    sys.stdout.flush()
