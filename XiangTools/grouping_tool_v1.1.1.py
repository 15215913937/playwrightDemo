import sys
import time

import xlrd
import xlwt

# 输入条件：表格，数据在A列，无空格
input_path = input("输入表文件绝对地址：")
out_path = input("输出表文件绝对地址：")
P = input("输入面积转换参数：")
COUNT = input("设置自定义面积的参数个数：")
# 创建一个workbook并设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 添加sheet
worksheet = workbook.add_sheet('new_data')

# input_path = 'C:\\Users\\sqn\\Desktop\\3.xls'
# out_path = 'C:\\Users\\sqn\\Desktop\\2.xls'
# P = 1
# COUNT = 13

a = float(P) * 1000 / 1000000
b = int(COUNT)

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

    # for i in range(x):
    #     worksheet.write(i, 0, sheet1.cell_value(i, 0))

    val = sheet1.cell_value(0, 0)
    val_flag = 0
    count = 1
    area = val
    id = 0
    group = 0

    for i in range(1, x):

        if sheet1.cell_value(i, 0) == val:
            count += 1
            area += sheet1.cell_value(i, 0)
            if i == x - 1:
                worksheet.write(id + group, 0, val)
                worksheet.write(id + group, 1, count)
                worksheet.write(id + group, 2, round(area * a, 3))
            continue

        worksheet.write(id + group, 0, val)
        worksheet.write(id + group, 1, count)

        id += 1
        count = 1
        val = sheet1.cell_value(i, 0)
        if id % b == 0:
            worksheet.write(id - 1 + group, 2, round(area * a, 3))
            area = val
            group += 1
            if i == x - 1:
                worksheet.write(id + group, 0, val)
                worksheet.write(id + group, 1, count)
                worksheet.write(id + group, 2, round(area * a, 3))
        else:
            area += val
            if i == x - 1:
                worksheet.write(id + group, 0, val)
                worksheet.write(id + group, 1, count)
                worksheet.write(id + group, 2, round(area * a, 3))

    workbook.save(out_path)
    sys.stdout.write("转换结束！\n")
    sys.stdout.flush()
    time.sleep(1)
except Exception as e:
    print("发生错误啦：", e)
    sys.stdout.flush()
