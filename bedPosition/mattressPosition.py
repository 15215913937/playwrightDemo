# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/3/31 16:54

from time import sleep, time

import pymysql
import requests


def importPressure(url, headers, params):
    # self.params = params

    res = requests.post(url=url, json=params, headers=headers)
    r = res.json()
    # print(r['data']['wrist'][0])
    wrist = r['data']['wrist']
    return ','.join([str(n) for n in wrist])


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
    sor = pymysql.connect(host=config['host'], port=config['port'], user=config['user'], password=config['passwd'],
                          database=config['db'])
    # 创建游标
    cur = sor.cursor()
    # res = requests.request(method=method, url=url, json=params, headers=headers)
    selectSql1 = "select id,pressure_data from bed_pressure where flag not like '%noise' and position = 1"
    cur.execute(selectSql1)
    getAll = cur.fetchall()
    # 云端部位识别
    url = 'http://bedapi.test.cnzxa.cn/api/test/predictPart'
    hearder = {
        'Content-Type': 'application/json'
    }

    # importPressure(url, hearder, params)
    for one in getAll:
        if one[1][0]!='[':
            arr = [int(x) for x in one[1].split(',')]
        else:
            arr = [int(x) for x in one[1][1:-1].split(',')]
        params = {
            "pressureList": arr,
            "dbPosition": 1
        }

        c_waist = importPressure(url, hearder, params)
        print(c_waist)
        # updatesql1 = "update bed_pressure set cloud_waist = '%s' where id = %d" % (c_waist, one[0])
        # cur.execute(updatesql1)
        # sor.commit()

    cur.close()
    sor.close()
