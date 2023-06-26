# -*- coding: utf-8 -*-
# Author: Shenbq
# Date: 2023/3/23 22:42
class DataBases():
    def __init__(self, host, port, user, password, database, charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

    # 创建连接数据库方法
    def connect(self):
        import pymysql
        try:
            # 创建数据库连接
            self.db = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                      database=self.database, charset=self.charset)
            # 创建游标
            self.cursor = self.db.cursor()
            return True
        except:
            return False

    def close(self):  # 关闭方法
        self.cursor.close()  # 关闭游标
        self.db.close()  # 关闭数据库

    # 查询
    def get_one(self, sql):  # 返回一条符合条件的查询结果
        result = 0
        try:
            self._reConn()
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print('select error', e)
        return result

    def get_all(self, sql):  # 返回全部符合条件的查询结果
        result = 0
        try:
            self._reConn()
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print("select error", e)
        return result

    def __edit(self, sql):  # 创建主函数
        result = 1  # 设置结果集，用于调用的时候做判断
        try:  # 这里是使用的try语句来尝试进行操作
            self._reConn()
            self.cursor.execute(sql)
            self.db.commit()  # 注意的是，如果是对数据库做了修改、删除、增加的操作，那么一定要commit提交，查询和创建表不需要提交
            self.close()
        except Exception as e:  # 如果操作失败，报出操作异常，且游标进行回滚
            print('error :', e)
            result = 0
            self.db.rollback()
        return result

    # 封装修改方法、删除方法、插入数据方法
    def insert(self, sql):
        # 插入语句  ，以下三个都是一样的，只是调用的时候，我们看起来更加清晰而已
        return self.__edit(sql)  # 通过主函数的处理，来去执行sql语句

    def delete(self, sql):  # 删除语句
        return self.__edit(sql)

    def update(self, sql):  # 修改语句
        return self.__edit(sql)

    def _reConn(self, num=28800, stime=3):  # 重试连接总次数为1天,这里根据实际情况自己设置,如果服务器宕机1天都没发现就......
        import time
        _number = 0
        _status = True
        while _status and _number <= num:
            try:
                self.db.ping()  # cping 校验连接是否异常
                _status = False
            except:
                if self.connect() == True:  # 重新连接,成功退出
                    _status = False
                    break
                _number += 1
                time.sleep(stime)  # 连接不成功,休眠3秒钟,继续循环，直到成功或重试次数结束
            if _number != 0:
                print("尝试数据库重新连接，当前已重连 %s 次" % _number)
