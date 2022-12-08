# coding = utf-8
# Author: Shenbq
# Date: 2022/10/12 17:21
import itertools


def partition(l, size):
    for i in range(0, len(l), size):
        yield list(itertools.islice(l, i, i + size))


s = '''
    14.3750,14.3750,14.3750,14.3750,14.3750,14.3750,10.5859,10.5859,10.5859,10.5859,11.6797,11.6797,11.6797,11.6797,18.3594,18.3594,16.0547,16.0547,16.0547,16.0547,4.8828,4.8828,13.9063,13.9063,13.9063,13.9063,13.9063,13.9063,11.0938,11.0938,4.2188,4.2188,20.5859
'''

lst = s.strip().split(",")

pt = partition(lst, 2)
for i, val in enumerate(pt):
    print(i + 1, val)
