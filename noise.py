# coding = utf-8
# Author: Shenbq
# Date: 2022/10/31 18:06
import itertools
import time

import redis

r = redis.Redis(host='172.17.1.92', port=6379, db=4)


def partition(l, size):
    for i in range(0, len(l), size):
        yield list(itertools.islice(l, i, i + size))


def format(s):
    lst = s.strip().split(",")

    pt = partition(lst, 8)
    for i, val in enumerate(pt):
        print(i + 1, val)


while True:

    result = r.get('bed_nopeople_data_094730343535393100310024')
    result = str(result)
    start_index = result.index(',[') + 2
    end_index = result.index(']]')
    result = result[start_index:end_index]
    format(result)
    # print(result)
    time.sleep(3)
