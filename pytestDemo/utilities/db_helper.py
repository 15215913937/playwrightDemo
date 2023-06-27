# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2022/12/16 10:57

import pandas as pd
import pymysql
from sqlalchemy import create_engine


class DBHelper(object):
    # 初始化MySQL数据库连接
    def __init__(self, host_name='127.0.0.1', db_name='sqn_home', user_name='root', pwd='root'):
        self.engine = create_engine(
            "mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=host_name, db=db_name, user=user_name, pw=pwd))

    def db_query(self, sql_query):
        with self.engine.connect() as conn:
            df = pd.read_sql_query(sql_query, conn)
        self.engine.dispose()
        return df.values.tolist()


if __name__ == '__main__':
    sql_query = '''select username,name,phone from user'''
    val = DBHelper().db_query(sql_query)
    print(val)
