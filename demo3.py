# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/3/22 11:33
import requests

# 创建一个workbook并设置编码
import xlwt

# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/3/22 10:00
import requests
import pymysql

config1 = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'db': 'zxa_test_data',
    'charset': 'utf8',
}
config2 = {
    'host': 'mysql.test.cnzxa.cn',
    'port': 23306,
    'user': 'user',
    'passwd': 'Comfab.088',
    'db': 'test',
    'charset': 'utf8',
}

url1 = 'http://bedapi.test.cnzxa.cn/api/test/decidePositionSimple'
headers1 = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjI0IiwiZXhwIjoxNzEwODY0MDAwLCJ1c2VybmFtZSI6IjE1MjE1OTEzOTM3In0.W_z7HlGqz6WyfrylI73-c-UH_GW0f3Z65xicMktEoao",
    "Content-Type": "application/json"
}
conn = pymysql.connect(**config2)
# 生成游标对象
cur = conn.cursor()

selectSql = "select * from bed_pressure where flag = 23032301"
upSql = "update bed_pressure set pressure_data = %s where id = %s"
cur.execute(selectSql)
conn.commit()
# 通过fetchall方法获得数据
data = cur.fetchall()
# s = data[0][2]
# s = s.replace(" ", "")
# array = s[1: len(s) - 1].split(',')
# array1=[]
# for a in array:
#     array1.append(int(a))

for datum in data:
    # str = "[" + datum[1] + "]"
    # try:
    #     cur.execute(upSql, [str, datum[0]])
    #     conn.commit()
    # except Exception as e:
    #     print(e)
    #     conn.rollback()
    pressure = datum[1]
    print(pressure)
    # pressure = pressure.replace(" ", "")
    # array = pressure[1: len(pressure) - 1].split(',')
    # array1 = []
    # for a in array:
    #     array1.append(int(a))
    #     # print(a)
    #
    # json_data = {
    #     "pressureList": array1
    # }
    # res = requests.post(url=url1, json=json_data, headers=headers1)
    # print(res.json()['data'])

cur.close()  # 关闭游标
conn.close()  # 关闭连接

# url = "https://bedapi.cnzxa.cn/api/sys/bed/logs/pressure"
# headers = {
#     "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjI0IiwiZXhwIjoxNzEwODY0MDAwLCJ1c2VybmFtZSI6IjE1MjE1OTEzOTM3In0.W_z7HlGqz6WyfrylI73-c-UH_GW0f3Z65xicMktEoao"
# }
# params = {
#     "denoise": "false",
#     "bedId": 371,
#     "startTime": "2023-03-20 16:36:10",
#     "endTime": "2023-03-20 16:46:37",
#     "currentPage": 1,
#     "pageSize": 10000,
# }
# res = requests.get(url=url, params=params, headers=headers)
# data1 = res.json()['data']['list']
# for d in data1:
#     # print(d['pressureList'])
#     pressure_data = str(d['pressureList'])
#     flag = '230322_noise'
#     environment = 'prop'
#     insertSql = "insert into bed_pressure(pressure_data,flag,environment,bed_id) values (%s,%s,%s,%s)"
#     try:
#         cur.execute(insertSql, [pressure_data, flag,environment,params['bedId']])  # 执行sql语句
#         conn.commit()  # 提交到数据库执行
#     except:
#         conn.rollback()  # 如果发生错误则回滚
# # 通过fetchall方法获得数据
# # data = cur.fetchall()
# # for datum in data:
# #     print(datum)
#
# cur.close()  # 关闭游标
# conn.close()  # 关闭连接
#
#
# workbook = xlwt.Workbook(encoding='utf-8')
# # 添加sheet
# worksheet = workbook.add_sheet('pressure_noise')
#
# # 写入excel, 参数对应 行, 列, 值
# worksheet.write(0, 0, label='pressure_noise')
# worksheet.write(0, 1, label='flag')
#
# url = "https://bedapi.cnzxa.cn/api/sys/bed/logs/pressure"
# headers = {
#     "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjI0IiwiZXhwIjoxNzEwODY0MDAwLCJ1c2VybmFtZSI6IjE1MjE1OTEzOTM3In0.W_z7HlGqz6WyfrylI73-c-UH_GW0f3Z65xicMktEoao"
# }
# params = {
#     "denoise": "false",
#     "bedId": 371,
#     "startTime": "2023-03-01 00:00:00",
#     "endTime": "2023-03-31 23:59:59",
#     "currentPage": 1,
#     "pageSize": 10,
# }
# res = requests.get(url=url, params=params, headers=headers)
# data1 = res.json()['data']['list']
# count1 = 1
# flag = '230322_noise'
# for d in data1:
#     print(d)
#     worksheet.write(count1, 0, str(d['pressureList']))
#     worksheet.write(count1, 1, flag)
#     count1 += 1
# workbook.save('C:\\Users\\sqn\\Desktop\\pressure_noise.csv')
