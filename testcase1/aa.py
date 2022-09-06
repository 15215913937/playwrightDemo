# coding = utf-8
# Author: Shenbq
# Date: 2022/9/6 18:04

import yaml
def getYml(yml_file):
    with open(yml_file,encoding='utf-8') as file:
        content = file.read()
