# coding = utf-8
# Author: Shenbq
# Date: 2022/10/12 17:21
import itertools
import math
import statistics


def partition(l, size):
    for i in range(0, len(l), size):
        yield list(itertools.islice(l, i, i + size))


s = '''
0,1,7,12,8,1,0,1,0,1,7,19,15,3,0,0,0,5,15,30,21,9,1,0,0,12,37,41,35,10,11,0,0,23,68,78,52,8,13,0,0,15,70,89,42,12,0,2,0,22,33,74,49,14,0,0,10,13,64,80,0,0,0,7,0,0,66,36,69,24,0,2,0,9,65,71,0,12,0,0,0,6,44,66,44,9,0,0,0,0,10,17,35,7,0,0,0,1,6,0,1,6,0,0,0,6,30,19,9,0,0,0,0,0,0,0,18,13,0,0,0,0,0,0,20,4,0,0,0,0,0,0,19,0,0,0,0,0,0,0,21,3,1,1,0,0,0,0,24,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0'''

lst = s.strip().split(",")

pt = partition(lst, 8)
for i, val in enumerate(pt):
    # print(i + 1, val)
    f = list(map(int, val))
    print(i + 1, "表面压力和：", sum(f))
