# coding = utf-8
# Author: Shenbq
# Date: 2022/1/14 14:13
import datetime
import random
import string
import time
import unittest

# a = datetime.datetime.now()
a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

a = a.replace(" ", "_")
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print(ran_str)
print(a)
