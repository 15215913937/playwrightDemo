# coding = utf-8
# Author: Shenbq
# Date: 2022/10/27 14:10
import time

import xlrd
from selenium import webdriver
from PIL import ImageGrab
# 打开文件位置
file = 'C:\\Users\\sqn\\Desktop\\2.xlsx'
wb = xlrd.open_workbook(file)

sheet1 = wb.sheet_by_index(0)
x = sheet1.nrows
y = sheet1.ncols

# print(x, y) 69,13
userNum = int((x - 1) / 4)
driver = webdriver.Chrome()
# 打开网址
driver.get("http://mettressapi.cnzxa.cn/swagger-ui.html#!/25968254543731938598/getPositionDataUsingPOST")
driver.maximize_window()
driver.implicitly_wait(5)
# 元素定位
token = driver.find_element_by_id('mtoken0.9689725615722966')
token.send_keys('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiIxNTIxNTkxMzkzNyIsInRlc3RlckZsYWciOiIxIiwiZG9SZWFsV29yayI6IjAiLCJpZCI6IjI0IiwiZXhwIjoxNjY3MzE4NDAwLCJ1c2VybmFtZSI6IuayiOWlh-eUtyJ9.LU_5jL0N-UQ_utYU-kv1tmXZcfK1wjePCmdXXK_UJuk')

# for j in range(userNum):
#     clear.click()
#     input.clear()
#     for i in range(4):
#         val = sheet1.cell_value(4 * j + i + 1, 3)
#         input.send_keys(val)
#         add.click()
#         input.clear()
#     name = sheet1.cell_value(4 * j + 1, 9)
#     input.send_keys(name)
#     time.sleep(1)