# coding = utf-8
# Author: Shenbq
# Date: 2022/10/27 15:10
import numpy as np
import xlrd

file = 'C:\\Users\\sqn\\Desktop\\1.xlsx'
wb = xlrd.open_workbook(file)
sheet1 = wb.sheet_by_index(0)
x = sheet1.nrows
y = sheet1.ncols
xrow = 21
ycol = 8

# for i in range(4):
#     val = sheet1.cell_value(i + 1, 3)
#     # 获取头离床行数
#     print(val)
val = sheet1.cell_value(1, 3)
list = {}

# print(type(val))
val1 = val.replace('[', '')
val2 = val1.replace(']', '')
val3 = val2.replace(' ','')
# print(type(val2))
a = val3.split(',')

# for i in range(len(a)):
#     list[i] = int(a[i])
# print(list)
print(int(a[2]))
for i in range(len(a)):
    print(i)
nval = np.array(a)
picture = nval.reshape(xrow, ycol)
# print(picture)
# # print(int(picture[0,0]))
# #
# # for i in range(len(picture)):
# #     print(picture[i])
# # print("分割线")
# # var = picture[0]
# # # 默认最大压力行数是7
# # maxPressureLine = 7
# # # 默认最大压力值0
# # maxPressureVal = 0
# for i in range(7, len(a)):
#     print(picture[i])
#
#     # for j in range(len(picture[i])):
#     #     maxPressureVal = picture[i,j]
#     #     print(picture[i, j])
#     # print("换行线")
