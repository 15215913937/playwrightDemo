# # -*- coding: utf-8 -*-
# # Author: Shenbq
# # Date: 2023/8/1 9:01
#
# import sys
# import time
#
# import xlrd
# import xlwt
# from collections import Counter
#
# # input_path = input("输入表文件绝对地址：")
# # out_path = input("输出表文件绝对地址：")
# # 创建一个workbook并设置编码
# workbook = xlwt.Workbook(encoding='utf-8')
# # 添加sheet
# worksheet = workbook.add_sheet('new_data')
#
input_path = 'C:\\Users\\sqn\\Desktop\\1.xlsx'
output_path = 'C:\\Users\\sqn\\Desktop\\2.xlsx'
#
#
# def find_duplicates(arr):
#     counter = Counter(arr)
#     duplicates = [element for element, count in counter.items() if count > 1]
#     return counter, duplicates
#
#
# wb = xlrd.open_workbook(input_path)
# sheet1 = wb.sheet_by_index(0)
# x = sheet1.nrows
# y = sheet1.ncols
# count = 0
# worksheet.write(0, 0, "原始数据过滤")
# worksheet.write(0, 1, "值")
# worksheet.write(0, 2, "个数")
# original_data = []
#
# for i in range(x):
#     for j in range(y):
#         if sheet1.cell_value(i, j) != '':
#             count += 1
#             original_data.append(sheet1.cell_value(i, j))
#             worksheet.write(count, 0, sheet1.cell_value(i, j))
#
# counter = Counter(original_data)
# data = [s for s in counter.keys()]
# print(type(data[3]))
# for i in range(len(data)):
#     if "-" in data[i]:
#         worksheet.write(i + 1, 1, int(data[i].split('-')[1]))
#     else:
#         worksheet.write(i + 1, 1, int(data[i]))
#
#     worksheet.write(i + 1, 2, counter.get(data[i]))
# # 保存
# workbook.save(out_path)
# sys.stdout.write("转换结束！\n")
# sys.stdout.flush()
# time.sleep(1)
import pandas as pd
import openpyxl

def stat_count(df):
    return df['A'].value_counts()


def write_excel(df, excel_path):
    df.to_excel(excel_path)


try:
    df = pd.read_excel(input_path)

    vc = stat_count(df)

    write_excel(vc, output_path)

except Exception as e:
    print("Error:", e)