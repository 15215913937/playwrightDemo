# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/21 10:55

from time import sleep
import requests

url = {
    'rise_fall_url': 'https://stock.xueqiu.com/v5/stock/screener/quote/list.json?page=1&size=30&order=desc&order_by=percent&exchange=CN&market=CN&type=sha',
    'volume_url': 'https://stock.xueqiu.com/v5/stock/screener/quote/list.json?type=sha&order_by=volume&order=desc&size=30&page=1',
    'turnover_url': 'https://stock.xueqiu.com/v5/stock/screener/quote/list.json?type=sha&order_by=amount&order=desc&size=30&page=1',
    'winners_list': 'https://stock.xueqiu.com/v5/stock/hq/longhu.json?date='
}

session = requests.Session()
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'}
session.get('https://xueqiu.com/')
# while True:
r1 = session.get(url['rise_fall_url'])
data1 = r1.json()
s1 = data1['data']['list']

r2 = session.get(url['volume_url'])
data2 = r2.json()
s2 = data2['data']['list']

r3 = session.get(url['turnover_url'])
data3 = r3.json()
s3 = data3['data']['list']

# 分割线
from datetime import datetime

now = datetime.now()

# 指定时间
target_time_start = datetime.now().replace(hour=9, minute=30, second=0, microsecond=0)
target_time_end = datetime.now().replace(hour=15, minute=30, second=0, microsecond=0)
is_ok = 1
# print(target_time)
if now < target_time_start:
    print("当日交易还未开始")
elif now > target_time_end:
    is_ok = 0
    print("当日交易结束")
else:
    print("当日交易进行中")

today = datetime.today()
week = today.weekday()
date = today.strftime('%Y-%m-%d')
date_str = datetime.strptime(date, '%Y-%m-%d')
timestamp = date_str.timestamp()

days = 1
winners_list = []
for i in range(days):
    day = str(int(timestamp) - 86400 * (i + is_ok)) + '000'
    print(str(i + is_ok) + '天前 : ' + day)
    r4 = session.get(url['winners_list'] + day)
    r4_data = r4.json()
    for s in r4_data['data']['items']:
        symbol = s['symbol']
        name = s['name']
        close = s['close']
        percent = s['percent']
        volume = s['volume']
        amount = s['amount']
        type_name = s['type_name']
        tn = ''

        print(type_name)
        # for t in type_name:
        #     tn = ','.join(t)
        # print(name + '(' + symbol + '),' + tn)
        # print(s)
    # print(r4_data['data']['items'])
# print(winners_list)

# 涨跌幅榜
rise_fall_list = []
# 成交量排行榜
volume_ranking = []
# 成交额排行榜
turnover_ranking = []

stock_dict = {}

for s in s1:
    rise_fall_list.append(s['name'])
for s in s2:
    volume_ranking.append(s['name'])
for s in s3:
    turnover_ranking.append(s['name'])

# print(data1)
print('------' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '------')
from functools import reduce

# # 找出双榜交集
# result_2 = np.intersect1d(rise_fall_list, volume_ranking)
# print("====================== 上双榜 ======================")
# print(result_2)
# # 找出三榜交集
# result_3 = reduce(np.intersect1d, (rise_fall_list, volume_ranking, turnover_ranking))
# print("====================== 上三榜 ======================")
# print(result_3)
sleep(3)
