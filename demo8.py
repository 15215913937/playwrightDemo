# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/11 15:44
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

days = 7

for i in range(days):
    day = str(int(timestamp) - 86400 * (i + is_ok)) + '000'
    print(str(i + is_ok) + '天前 : ' + day)
