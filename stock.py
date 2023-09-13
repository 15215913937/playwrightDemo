# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/21 10:55

from time import sleep
import requests
import numpy as np

BASE_URL = 'https://stock.xueqiu.com/v5/stock/'
url = {
    # 榜单：根据order_by，涨幅：percent，成交量：volume，成交额：amount
    'stock_list': BASE_URL + 'screener/quote/list.json',
    # 龙虎榜
    'winners_list': BASE_URL + 'hq/longhu.json',
    # 股票数据
    'stock_data': BASE_URL + 'chart/kline.json'
}
params = {
    # 榜单
    'stock_list': {'page': 1,
                   'size': 30,
                   'order': 'desc',
                   'order_by': '',
                   'exchange': 'CN',
                   'market': 'CN',
                   'type': 'sha'},
    # 龙虎榜
    'winners_list': {'date': ''},
    # 股票数据
    'stock_data': {'begin': '',
                   'period': 'day',
                   'type': 'before',
                   'symbol': ''}
}

session = requests.Session()
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'}
session.get('https://xueqiu.com/')

# ---分割线---

from datetime import datetime, timedelta

now = datetime.now()

# 指定时间
target_time_start = datetime.now().replace(hour=9, minute=30, second=0, microsecond=0)
target_time_end = datetime.now().replace(hour=15, minute=30, second=0, microsecond=0)

# 当天交易 0已结束 1未结束
is_ok = 1

if now < target_time_start:
    print("当日交易还未开始")
elif now > target_time_end:
    is_ok = 0
    print("当日交易结束")
else:
    print("当日交易进行中...")

today = datetime.today()
week = today.weekday()
date = today.strftime('%Y-%m-%d')
date_str = datetime.strptime(date, '%Y-%m-%d')
timestamp = date_str.timestamp()

# 日期设置
days = 7
winners_list = []

# 龙虎榜

for i in range(days):
    day = str(int(timestamp) - 86400 * (i + is_ok)) + '000'
    print('///')
    print(str(i + is_ok) + '天前(' + str((now - timedelta(days=i + is_ok)).strftime('%Y-%m-%d')) + ') : ' + day)
    params['stock_data']['date'] = day
    r4 = session.get(url['winners_list'], params=params['stock_data'])
    r4_data = r4.json()
    len_data = len(r4_data['data']['items'])

    if len_data == 0:
        print('休息')
        continue

    for s in r4_data['data']['items']:
        symbol = s['symbol']
        name = s['name']
        close = s['close']
        percent = s['percent']
        volume = s['volume']
        amount = s['amount']
        type_name = s['type_name']
        tn = ''
        for i in range(len(type_name)):
            tn = tn + ' ' + str(i + 1) + '、' + type_name[i]
        print(name + '(' + symbol + ') : ' + tn)

# 风险系数==
# 市场收益率
params['stock_data']['begin'] = '1694016000000'
params['stock_data']['symbol'] = 'SH000001'
market_return = session.get(url['stock_data'], params=params['stock_data'])
data1 = market_return.json()
s1 = data1['data']['item']
print(len(s1))
print(s1)

# 日三榜==
isLooping = True
while isLooping:
    params['stock_list']['order_by'] = 'percent'

    r1 = session.get(url['stock_list'], params=params['stock_list'])
    data1 = r1.json()
    s1 = data1['data']['list']

    params['stock_list']['order_by'] = 'volume'

    r2 = session.get(url['stock_list'], params=params['stock_list'])
    data2 = r2.json()
    s2 = data2['data']['list']

    params['stock_list']['order_by'] = 'amount'

    r3 = session.get(url['stock_list'], params=params['stock_list'])
    data3 = r3.json()
    s3 = data3['data']['list']

    # 涨跌幅榜
    rise_fall_list = []
    # 成交量排行榜
    volume_ranking = []
    # 成交额排行榜
    turnover_ranking = []

    for s in s1:
        rise_fall_list.append(s['name'])
    for s in s2:
        volume_ranking.append(s['name'])
    for s in s3:
        turnover_ranking.append(s['name'])

    print('------' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '------')
    from functools import reduce

    # 找出双榜交集
    result_2 = np.intersect1d(rise_fall_list, volume_ranking)
    print("====================== 上双榜 ======================")
    print(result_2)
    # 找出三榜交集
    result_3 = reduce(np.intersect1d, (rise_fall_list, volume_ranking, turnover_ranking))
    print("====================== 上三榜 ======================")
    print(result_3)
    sleep(3)
    isLooping = False

session.close()
