# coding = utf-8
# Author: Shenbq
# Date: 2021/12/15 13:22
from collections import Counter
import xlrd
import xlwt

# 打开文件
file = 'C:\\Users\\Administrator\\Desktop\\墙板数据模板\\墙板数据模板.xlsx'
wb = xlrd.open_workbook(file)
# 获取所有工作表名字
# print(wb.sheet_names())
sheet1 = wb.sheet_by_index(0)
# 获取按行所有的数据
mrow = sheet1.nrows
# 获取按列所有的数据
mcol = sheet1.ncols
# print(mrow, mcol)
data = []
# 提取数据
for i in range(mrow):
    for j in range(mcol):
        type = sheet1.cell(i, j).ctype
        if type == 2:
            data.append(int(sheet1.cell(i, j).value))

count = Counter(data).most_common()
# 升序
count = sorted(count, key=lambda x: x[0])

# 新建表
workbook = xlwt.Workbook(encoding='utf-8')
# 命名工作表
new_sheet = workbook.add_sheet('导出计数_列A')
new_sheet.write(0, 0, '列A')
new_sheet.write(0, 1, '计数')
# 存入数据
for i in range(len(count)):
    new_sheet.write(i + 1, 0, count[i][0])
    new_sheet.write(i + 1, 1, count[i][1])
# 保存
workbook.save('墙板数据.xls')
