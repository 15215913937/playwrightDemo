# coding = utf-8
# Author: Shenbq
# Date: 2022/1/14 14:13
import json

import requests
import xlwt

# bedId=0
# pageSize=0
# bedName=''
# 创建一个workbook并设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 添加sheet
worksheet = workbook.add_sheet('1556')

# 写入excel, 参数对应 行, 列, 值
worksheet.write(0, 0, label='时间（ID）')
worksheet.write(0, 1, label='床垫')
worksheet.write(0, 2, label='压力')
worksheet.write(0, 3, label='姿势')

url1 = 'https://bedapi.cnzxa.cn/api/sys/bed/logs/operate'
params1 = {
    "bedId": 380,
    "pageSize": 120,
    "currentPage": 1
}
headers = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjI0IiwiZXhwIjoxNzEwODY0MDAwLCJ1c2VybmFtZSI6IjE1MjE1OTEzOTM3In0.W_z7HlGqz6WyfrylI73-c-UH_GW0f3Z65xicMktEoao"
}
headers1 = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjI0IiwiZXhwIjoxNzEwODY0MDAwLCJ1c2VybmFtZSI6IjE1MjE1OTEzOTM3In0.W_z7HlGqz6WyfrylI73-c-UH_GW0f3Z65xicMktEoao",
    "Content-Type": "application/json"
}
r1 = requests.get(url=url1, params=params1, headers=headers)
list1 = r1.json()['data']['list']
ids = []
count1 = 0
count2 = 0
for index, li in enumerate(list1):
    if (li['operateContent'] == '离床 到 仰卧'):
        count1 += 3
        worksheet.write(count1, 0, li['id'])
        worksheet.write(count1, 1, '广ZXA1_000001中2')
        ids.append(li['id'])
print(ids)
pressureList = []
for index, id in enumerate(ids):

    url2 = 'https://bedapi.cnzxa.cn/api/sys/bed/logs/operate/pressure'
    url3 = 'http://bedapi.test.cnzxa.cn/api/test/decidePositionSimple'
    params2 = {
        "operateId": id,
        "denoise": "true",
        "pageSize": 100,
        "currentPage": 1
    }
    r2 = requests.get(url=url2, params=params2, headers=headers)
    if (r2.json()['data'] == {}):
        s1 = [0] * 168
        s2 = [0] * 168
        s3 = [0] * 168
    else:
        list2 = r2.json()['data']['list']
        s1 = list2[len(list2) - 1]['pressureList']
        s2 = list2[len(list2) - 2]['pressureList']
        s3 = list2[len(list2) - 3]['pressureList']
    # print(s)
    data1 = {
        "pressureList": s1
    }
    r3_1 = requests.post(url=url3, data=json.dumps(data1), headers=headers1)

    data2 = {
        "pressureList": s2
    }
    r3_2 = requests.post(url=url3, json=data2, headers=headers1)
    data3 = {
        "pressureList": s3
    }
    r3_3 = requests.post(url=url3, data=json.dumps(data3), headers=headers1)
    count2 += 1
    worksheet.write(count2, 2, str(s1))
    worksheet.write(count2, 3, r3_1.json()['data'])
    count2 += 1
    worksheet.write(count2, 2, str(s2))
    worksheet.write(count2, 3, r3_2.json()['data'])
    count2 += 1
    worksheet.write(count2, 2, str(s3))
    worksheet.write(count2, 3, r3_3.json()['data'])
    # pressureList.append(str)

# print(pressureList)
# 保存
workbook.save('广ZXA1_000001中2.xls')
