import logging

import requests
import time
from datetime import datetime

test_key = {
    '1922': 'tx-tyqVQBuSRjB2DCziXbe_ZoX3f21rr1vVrp1CBMNc=',
    '1892': '2PyA7xB3UOTC36Rg5rlXYv6ldC-8yXEf6zdH-ZeioQ8='
}
prop_key = {
    '744': 'abmSxjSYlFWDGFDXXJXX6ncvV5MYjPRl6U6_iTbjgjY=',
    '810': 'kXD9MBhRue8VgMoIBFZybVl0AbJIrUDD872ilnj2cRI='
}


def run_api(count, now, bed_id, env):
    if env == 0:
        url1 = "http://bedopenapi.test.cnzxa.cn/api/bed/match-pressure?key=" + test_key.get(bed_id)
        url2 = "https://bedapi.test.cnzxa.cn/api/pro/bed?bedId=" + bed_id
        headers1 = {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MSwiZXhwIjoxNzIzMzA1NjAwLCJ1c2VybmFtZSI6ImFkbWluIn0.ybDbmf92EFv9cxOFXlWcrLIF2LZfBdT1jDqrK6vJ2oE",
            "Content-Type": "application/json"
        }
    elif env == 1:
        url1 = "http://bedopenapi.cnzxa.cn/api/bed/match-pressure?key=" + prop_key.get(bed_id)
        url2 = "https://bedapi.cnzxa.cn/api/pro/bed?bedId=" + bed_id
        headers1 = {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjQsImV4cCI6MTcyMzU2NDc5OSwidXNlcm5hbWUiOiIxNTIxNTkxMzkzNyJ9.ulBuTLQeE3eNwM9BcTj8AR72L_Gel7iRgWbzgCgM2Uo",
            "Content-Type": "application/json"
        }
    print(now + " - Start job " + str(count) + " ...")
    try:
        response1 = requests.get(url1)
        response2 = requests.get(url=url2, headers=headers1)
    except Exception as e:
        logging.exception("Request failed : %s", e)

    json = response2.json()
    print(response1.text)
    print(json['data']['pressureList'])


# env 0 测试 1 正式
env = 1
bed_id = '810'
count = 0
while True:
    count += 1
    run_api(count, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), bed_id, 1)
    time.sleep(3)
