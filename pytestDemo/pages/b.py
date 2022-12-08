# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2022/12/7 16:03
import os.path

print(os.path.abspath(os.getcwd()))
print(os.getcwd())
path = os.getcwd()
a = os.path.abspath(os.path.join(os.path.dirname(__file__),'../configs/ymls/login.yml'))
print(a)