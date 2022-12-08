# coding = utf-8
# Author: Shenbq
# Date: 2021/12/15 13:22
import datetime
import os.path
from time import strftime as sf,localtime as lt
from collections import Counter
import xlrd
import xlwt


# 打开文件
filepath = 'C:\\Users\\Administrator\\Desktop\\墙板数据模板\\墙板数据模板.xlsx'
wb = xlrd.open_workbook(filepath)

# 获取工作表
sheet = wb.sheet_by_index(0)
# 获取行数
mrow = sheet.nrows
# 获取列数
mcol = sheet.ncols
# print(mrow, mcol)

data = []
# 提取数据
for i in range(mrow):
    for j in range(mcol):
        type = sheet.cell(i, j).ctype
        if type == 2:
            data.append(int(sheet.cell(i, j).value))

count = Counter(data).most_common()
# 升序
count = sorted(count, key=lambda x: x[0])

# print(count)

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
newDataName = '新墙板数据' + sf('%Y%m%d%H%M%S', lt())+ '.xls'
fullAddress = 'C:\\Users\\Administrator\\Desktop\\墙板数据模板\\整理后数据\\'+newDataName
workbook.save(fullAddress)
# print("输出成功")
# 模拟双击打开表
os.system(fullAddress)
