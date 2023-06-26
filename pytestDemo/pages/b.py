# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2022/12/7 16:03
import logging
import os.path

# print(os.path.abspath(os.getcwd()))
# print(os.getcwd())
# path = os.getcwd()
# a = os.path.abspath(os.path.join(os.path.dirname(__file__),'../configs/ymls/login.yml'))
# print(a)

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

logging.info("测试")