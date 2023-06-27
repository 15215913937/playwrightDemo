import sys
import time

import xlrd
import xlwt

# 输入条件：表格，数据在A列，无空格
input_path = input("输入表文件绝对地址：")
out_path = input("输出表文件绝对地址：")
P = input("输入固定参数：")
# 创建一个workbook并设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 添加sheet
worksheet = workbook.add_sheet('414')

# input_path = 'C:\\Users\\sqn\\Desktop\\1.xls'
# out_path = 'C:\\Users\\sqn\\Desktop\\2.xls'
# P = 0.576
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

    # 复制原数据
    for i in range(x):
        worksheet.write(i, 0, sheet1.cell_value(i, 0))

    groupsBy = 0
    count = 1
    groups = 0
    flag = 0
    val = sheet1.cell_value(0, 0)
    area_sum = sheet1.cell_value(0, 0)
    for i in range(1, x):

        if groups % 14 == 13:
            if flag != groups:
                flag = groups
                worksheet.write(groups - 13, 5, round(area_sum * a, 3))
                area_sum = 0
        area_sum += sheet1.cell_value(i, 0)
        if val != sheet1.cell_value(i, 0):
            if i != x - 1:
                area = val * count
                worksheet.write(groups, 1, val)
                worksheet.write(groups, 2, count)
                worksheet.write(groups, 4, area)
                groups += 1
                val = sheet1.cell_value(i, 0)
                count = 1
                continue
            area = val * count
            worksheet.write(groups, 1, val)
            worksheet.write(groups, 2, count)
            worksheet.write(groups, 4, area)

            val = sheet1.cell_value(i, 0)
            count = 1
            groups += 1
            area = val * count
            worksheet.write(groups, 1, val)
            worksheet.write(groups, 2, count)
            worksheet.write(groups, 4, area)
            continue
        count += 1
        if i == x - 1:
            area = val * count
            worksheet.write(groups, 1, val)
            worksheet.write(groups, 2, count)
            worksheet.write(groups, 4, area)
            groups += 1

    if groups % 14 != 13:
        worksheet.write(groups - groups % 14, 5, round(area_sum * a, 3))

    for i in range(groups):
        if i % 14 == 0:
            groupsBy += 1
            worksheet.write(i, 3, 'start' + str(groupsBy))
    # 保存
    workbook.save(out_path)
    sys.stdout.write("转换结束！\n")
    sys.stdout.flush()
    time.sleep(1)
except Exception as e:
    print("发生错误啦：", e)
    sys.stdout.flush()
