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
driver.get("http://bedimg.test.cnzxa.cn/#/")
driver.maximize_window()
# 元素定位
input = driver.find_element_by_xpath(
    '/html/body/uni-app/uni-pages/uni-pages-wrapper/uni-pages-body/uni-view/uni-view[1]/uni-input/div/input')
add = driver.find_element_by_xpath(
    '/html/body/uni-app/uni-pages/uni-pages-wrapper/uni-pages-body/uni-view/uni-view[1]/uni-view[1]')
clear = driver.find_element_by_xpath(
    '/html/body/uni-app/uni-pages/uni-pages-wrapper/uni-pages-body/uni-view/uni-view[1]/uni-view[2]')
clear.click()
input.clear()
# 截图区域设置
bbox = (0, 0, 1400, 900)
for j in range(userNum):
    clear.click()
    input.clear()
    for i in range(4):
        val = sheet1.cell_value(4 * j + i + 1, 3)
        input.send_keys(val)
        add.click()
        input.clear()
    name = sheet1.cell_value(4 * j + 1, 9)
    input.send_keys(name)
    time.sleep(1)
    im = ImageGrab.grab(bbox)
    # 截图存放位置
    im.save('C:\\Users\\sqn\\Desktop\\采集截图2\\%s.png' % name)
