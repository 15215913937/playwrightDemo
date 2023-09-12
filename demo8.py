# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/8/11 15:44
from datetime import datetime, timedelta
from dateutil import parser
import time


def get_timestamp(days_before):
    today = datetime.today()
    # week = today.weekday()
    # date_str = today.strftime('%Y-%m-%d')
    day = today - timedelta(days=days_before)
    return day.timestamp()


days = 7
for i in range(days):
    print(int(get_timestamp(i + 1)) * 1000)
    # ts = int(get_timestamp(i + 1)) * 1000
    # print(time.strftime("%Y%m%d", time.localtime(ts)))
# today = datetime.today()
# week = today.weekday()
# date_str = today.strftime('%Y-%m-%d')
# date = parser.parse(date_str)
# timestamp = date.timestamp()
#
# for i in range(7):
#     print(str(int(timestamp) - 86400 * (i + 1)) + '000')
