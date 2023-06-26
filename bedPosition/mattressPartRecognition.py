# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/3/31 16:54

from time import sleep, time

import requests
from PIL import ImageGrab
from DataBases import DataBases as db
from selenium import webdriver


# 导入数据
# def importPressure(env, flag, url, bedId, headers, **params):
def importPressure(url, headers, params):
    # self.params = params

    res = requests.post(url=url, json=params, headers=headers)
    r = res.json()
    # print(r['data']['wrist'][0])
    return r['data']['wrist'][0]


if __name__ == '__main__':
    # 数据库配置
    config = {
        'host': 'mysql.test.cnzxa.cn',
        'port': 23306,
        'user': 'user',
        'passwd': 'Comfab.088',
        'db': 'test',
        'charset': 'utf8',
    }

    # 实例化数据库对象sor
    sor = db(host=config['host'], port=config['port'], user=config['user'], password=config['passwd'],
             database=config['db'])
    # res = requests.request(method=method, url=url, json=params, headers=headers)
    selectSql1 = "select id,pressure_data from bed_pressure where flag like '%230624_col' and position = 1"
    getAll = sor.get_all(selectSql1)
    # 云端部位识别
    url = 'http://bedapi.test.cnzxa.cn/api/test/predictPart'
    hearder = {
        'Content-Type': 'application/json'
    }

    # importPressure(url, hearder, params)
    for one in getAll:
        arr = [int(x) for x in one[1].split(',')]
        params = {
            "pressureList": arr,
            "dbPosition": 1
        }

        c_waist = importPressure(url, hearder, params)
        updatesql1 = "update bed_pressure set cloud_waist = %s where id = %d"%(c_waist, one[0])
        sor.update(updatesql1,)
