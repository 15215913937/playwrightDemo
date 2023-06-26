# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/3/22 10:00
import time
from selenium import webdriver
from PIL import ImageGrab
import requests
import pymysql

# 参数区域
from PIL import ImageGrab

flag = '230324_sit'
environment = 'test'
savePath0 = 'D:\\workspace\\bed_position\\screencap\\0'
savePath1 = 'D:\\workspace\\bed_position\\screencap\\1'

config = {
    'host': 'mysql.test.cnzxa.cn',
    'port': 23306,
    'user': 'user',
    'passwd': 'Comfab.088',
    'db': 'test',
    'charset': 'utf8',
}

conn = pymysql.connect(**config)
# 生成游标对象
cur = conn.cursor()

# selectSql = "select * from bed_pressure where flag=%s and position_recognition=%s" % (flag, position_recognition)
selectSql1 = "select * from bed_pressure where flag=%s and bed_id = %s and position_recognition=0"
selectSql2 = "select * from bed_pressure where flag=%s and bed_id = %s and position_recognition!=0"
# upSql = "update bed_pressure set position_recognition = %s where id = %s"
insertSql = "insert into bed_pressure(pressure_data,flag,environment,bed_id,position_recognition) values (%s,%s,%s,%s,%s)"

# 获取床垫压力日志
url_pord = "https://bedapi.cnzxa.cn/api/sys/bed/logs/pressure"
url_test = "https://bedapi.test.cnzxa.cn/api/sys/bed/logs/pressure"

# 睡姿识别
url1 = 'http://bedapi.test.cnzxa.cn/api/test/decidePositionSimple'

headers_prop = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjI0IiwiZXhwIjoxNzEwODY0MDAwLCJ1c2VybmFtZSI6IjE1MjE1OTEzOTM3In0.W_z7HlGqz6WyfrylI73-c-UH_GW0f3Z65xicMktEoao"
}
headers_test = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjE2MiIsImV4cCI6MTcxMTAzNjgwMCwidXNlcm5hbWUiOiIxNTIxNTkxMzkzNyJ9.7wxVUJO8kX-_Y9jyQK9BaUzw2dq5RAeAvKw7Xp_bFyI"
}
headers1 = {
    "Content-Type": "application/json"
}

params = {
    "denoise": "true",
    "bedId": 1555,
    "startTime": "2023-03-24 17:06:24",
    "endTime": "2023-03-24 17:22:45",
    "currentPage": 1,
    "pageSize": 10000,
}

start_time = time.time()

res = requests.get(url=url_test, params=params, headers=headers_test)
data0 = res.json()['data']['list']
# cur.execute(insertSql)
# conn.commit()
# data = cur.fetchall()

# for datum in data:
#     # print(datum)
#     pressure = datum[1].replace(" ", "")
#     array = pressure[1: len(pressure) - 1].split(',')
#     array1 = []
#     for a in array:
#         array1.append(int(a))
#     json_data = {
#         "pressureList": array1
#     }
#     res = requests.post(url=url1, json=json_data, headers=headers1)
#     position_recognition = res.json()['data']
#     try:
#         cur.execute(
#             "update bed_pressure set position_recognition = %s where id = %s" % (position_recognition, datum[0]))
#         conn.commit()
#     except:
#         conn.rollback()

for d in data0:
    pressure_data = str(d['pressureList'])
    json_data = {
        "pressureList": d['pressureList']
    }
    res = requests.post(url=url1, json=json_data, headers=headers1)
    position_recognition = res.json()['data']
    try:
        cur.execute(insertSql, [pressure_data, flag, environment, params['bedId'], position_recognition])  # 执行sql语句
        conn.commit()  # 提交到数据库执行
    except:
        conn.rollback()  # 如果发生错误则回滚

    # 截图

cur.execute(selectSql1, [flag,params['bedId']])
conn.commit()
data1 = cur.fetchall()

cur.execute(selectSql2, [flag,params['bedId']])
conn.commit()
data2 = cur.fetchall()

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
bbox = (0, 180, 400, 900)

for datum in data1:
    clear.click()
    input.clear()
    val = datum[1]
    input.send_keys(val)
    add.click()
    time.sleep(1)
    im = ImageGrab.grab(bbox)
    # 截图存放位置
    im.save((savePath0 + "\\%s.png") % (datum[0]))
for datum in data2:
    clear.click()
    input.clear()
    val = datum[1]
    input.send_keys(val)
    add.click()
    time.sleep(1)
    im = ImageGrab.grab(bbox)
    # 截图存放位置
    im.save((savePath1 + "\\%s.png") % (datum[0]))

driver.quit()
end_time = time.time()
duration = end_time - start_time

cur.close()  # 关闭游标
conn.close()  # 关闭连接
print("耗时 %f 秒" % duration)
