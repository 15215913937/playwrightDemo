# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/11 15:44
import requests

url = "https://bedapi.test.cnzxa.cn/api/pro/bed?bedId=1892"
headers1 = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNzIzMzA1NjAwLCJ1c2VybmFtZSI6ImFkbWluIn0.ybDbmf92EFv9cxOFXlWcrLIF2LZfBdT1jDqrK6vJ2oE",
    "Content-Type": "application/json"
}
response = requests.get(url=url, headers=headers1)
json = response.json()
print(json['data']['pressureList'])
