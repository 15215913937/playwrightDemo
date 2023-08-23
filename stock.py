# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/21 10:55
import sys
from time import sleep
from datetime import datetime

import requests

url = {
    'rise_fall_url': 'https://stock.xueqiu.com/v5/stock/screener/quote/list.json?page=1&size=30&order=desc&order_by=percent&exchange=CN&market=CN&type=sha',
    'volume_url': 'https://stock.xueqiu.com/v5/stock/screener/quote/list.json?type=sha&order_by=volume&order=desc&size=50&page=1',
    'turnover_url': 'https://stock.xueqiu.com/v5/stock/screener/quote/list.json?type=sha&order_by=amount&order=desc&size=50&page=1'
}

session = requests.Session()
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'}
session.get('https://xueqiu.com/')

while True:
    r1 = session.get(url['rise_fall_url'])
    data1 = r1.json()
    s1 = data1['data']['list']

    r2 = session.get(url['volume_url'])
    data2 = r2.json()
    s2 = data2['data']['list']

    r3 = session.get(url['turnover_url'])
    data3 = r3.json()
    s3 = data3['data']['list']
    # 涨跌幅榜
    rise_fall_list = []
    # 成交量排行榜
    volume_ranking = []
    # 成交额排行榜
    turnover_ranking = []
    stock_dict = {}

    for s in s1:
        # print(s['name'])
        rise_fall_list.append(s['name'])
    for s in s2:
        volume_ranking.append(s['name'])
    for s in s3:
        turnover_ranking.append(s['name'])

    # print(data1)
    print('------'+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+'------')
    print(rise_fall_list)
    print(volume_ranking)
    print(turnover_ranking)
    sleep(3)
