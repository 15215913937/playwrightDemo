
import xlrd
import xlwt

input_path = input("输入表文件绝对地址：")
out_path = input("输出表文件绝对地址：")
# 创建一个workbook并设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 添加sheet
worksheet = workbook.add_sheet('414')

# file = 'C:\\Users\\sqn\\Desktop\\414表格.xls'
wb = xlrd.open_workbook(input_path)
sheet1 = wb.sheet_by_index(0)
x = sheet1.nrows
y = sheet1.ncols
groups = x // 14

b = 0
for i in range(x):
    worksheet.write(i, 3, sheet1.cell_value(i, 0))
for i in range(groups):
    flag = "start" + str(i)
    worksheet.write(i * 14, 2, flag)
    val = sheet1.cell_value(i * 14, 0)
    count = 1
    a = i * 14
    for j in range(13):
        if j == 13 - 1:
            if val == sheet1.cell_value(i * 14 + j + 1, 0):
                worksheet.write(a, 0, val)
                count += 1
                worksheet.write(a, 1, count)
                a += 1
                break
            if val != sheet1.cell_value(i * 14 + j + 1, 0):
                worksheet.write(a, 0, val)
                worksheet.write(a, 1, count)
                count = 1
                val = sheet1.cell_value(i * 14 + j + 1, 0)
                a += 1
                worksheet.write(a, 0, val)
                worksheet.write(a, 1, count)
                a += 1
                break
        if val != sheet1.cell_value(i * 14 + j + 1, 0):
            worksheet.write(a, 0, val)
            worksheet.write(a, 1, count)
            count = 1
            val = sheet1.cell_value(i * 14 + j + 1, 0)
            a += 1
            continue
        count += 1
# 保存
workbook.save(out_path)
