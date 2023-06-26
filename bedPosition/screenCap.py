# coding = utf-8
# Author: Shenbq
# Date: 2022/10/27 14:10
import time

import xlrd
from selenium import webdriver
from PIL import ImageGrab

# 打开文件位置
file = 'C:\\Users\\sqn\\Desktop\\bedPosition\\广ZXA1_000001中1\\广ZXA1_000017中1.xls'
wb = xlrd.open_workbook(file)

sheet1 = wb.sheet_by_index(0)
x = sheet1.nrows
y = sheet1.ncols

# print(x, y) 139 4
# userNum = int((x - 1) / 4)
driver = webdriver.Chrome()
# 打开网址
driver.get("http://bedimg.test.cnzxa.cn/#/")
driver.maximize_window()
# 元素定位
input = driver.find_element_by_xpath(
    '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-input/div/input')
add = driver.find_element_by_xpath(
    '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[1]')
clear = driver.find_element_by_xpath(
    '/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view[2]')
clear.click()
input.clear()
# 截图区域设置
bbox = (0, 0, 1400, 900)
for i in range(int(x / 3 - 1)):
    clear.click()
    input.clear()
    val1 = sheet1.cell_value(3 * i + 1, 2)
    input.send_keys(val1)
    add.click()
    input.clear()
    val2 = sheet1.cell_value(3 * i + 2, 2)
    input.send_keys(val2)
    add.click()
    input.clear()
    val3 = sheet1.cell_value(3 * i + 3, 2)
    input.send_keys(val3)
    add.click()
    time.sleep(1)
    im = ImageGrab.grab(bbox)
    # 截图存放位置
    im.save('C:\\Users\\sqn\\Desktop\\bedPosition\\广ZXA1_000001中1\\screencap\\%s.png' % (i + 1))
driver.quit()
