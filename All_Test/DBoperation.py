#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import pymysql
import os
from BasicConfig import BasicConfig
import OPerationLog as OpLog


class DbOperation(object):
    # 初始化
    def __init__(self):
        path = os.path.split(os.path.realpath(__file__))[0] + '\\basic.ini'
        cf = BasicConfig(path)
        config = cf.get_config_by_key('database_test', 'config')
        # print(config)
        # print(type(eval(config)))
        self.conn = pymysql.connect(**eval(config))
        # items = cf.get_all_items_by_section('database')
        # print(type(items))
        # print(items)
        # self.conn = pymysql.connect(
        #     host=cf.get_config_by_key('database', 'host'),
        #     port=eval(items[1][1]),
        #     db=items[2][1],
        #     user=items[3][1],
        #     passwd=items[4][1],
        #     charset=items[5][1],
        #     cursorclass=eval(items[6][1])
        # )
        self.cur = self.conn.cursor()

    # 定义单条数据操作，增删改
    def op_sql(self, param, args=None):
        try:
            self.cur.execute(param, args)
            self.conn.commit()
            return True
        except BaseException as e:
            print('mysql execute error:%d : %s' % (e.args[0], e.args[1]))
            OpLog.write_error_log(e)
            return False

    # 查询单条数据
    def select_one(self, condition, args=None):
        try:
            self.cur.execute(condition, args)
            results = self.cur.fetchone()
        except BaseException as e:
            results = 'sql001'
            OpLog.write_error_log(e)
        finally:
            return results

    # 查询所有数据
    def select_all(self, condition, args=None):
        try:
            self.cur.execute(condition, args)
            # 光标回到初始位置
            self.cur.scroll(0, mode='absolute')
            results = self.cur.fetchall()
        except BaseException as e:
            results = 'sql002'
            OpLog.write_error_log(e)
        finally:
            return results

    # 插入多条数据
    def insert_more(self, condition, args=None):
        try:
            self.cur.executemany(condition, args)
            self.conn.commit()
            results = True
        except BaseException as e:
            results = 'sql003'
            OpLog.write_error_log(e)
        finally:
            return results

    # 关闭游标和数据库连接
    def __del__(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    test = DbOperation()
    sql = 'SELECT * FROM `douban` limit 1;'
    result = test.select_one(sql)
    # print(type(result))
    # print(result)