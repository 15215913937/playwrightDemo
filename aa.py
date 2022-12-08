# coding = utf-8
# Author: Shenbq
# Date: 2022/11/11 15:40
import os
# 获取当前路径
abspath = os.getcwd()
# 获取上级路径
fatherPath = os.path.abspath('..\\utils\\common.yml')
print(fatherPath)