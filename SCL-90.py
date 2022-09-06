# coding = utf-8
# Author: Shenbq
# Date: 2022/6/29 11:38

# 题目总数
from random import randint

count = 99
# 题目
title = list(range(1, 100))
print(title)
print(type(title))
# 假设所有题目按顺序1-5分
for i in range(len(title)):
    title[i] = randint(1, 5)
    print('第{}题：{}'.format(i, title[i]))
# 总分
total_points = sum(title)
print("总分：{}".format(total_points))
# 阳性项目数：yx_count
yx_count = 0
for i in range(len(title)):
    if title[i] >= 2:
        yx_count += 1
print("阳性项目数：{}".format(count))
