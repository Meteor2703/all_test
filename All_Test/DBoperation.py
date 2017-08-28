#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import pymysql
import logging
import os
import BasicConfig


class DbOperation(object):
    # 初始化
    def __init__(self):
        path = os.path.split(os.path.realpath(__file__))[0] + '\\basic.ini'
        cf = BasicConfig(path)
        items = cf.get_all_items_by_section('database')
        self.conn = pymysql.connect(
            host=cf.get_config_by_key('database', 'dbhost'),
            user=items[3][1],
            passwd=items[4][1],
            db=items[2][1],
            port=3306,
            charset='utf8'
        )
        # self.cur = self.conn.cursor()

    # 定义单条数据操作，增删改
    def op_sql(self, param):
        try:
            self.cur.execute(param)
            self.conn.commit()
            return True
        except BaseException as e:
            print('mysql execute error:%d : %s' % (e.args[0], e.args[1]))
            logging.basicConfig(filename=os.path.join(os.getcwd(), './log.txt'),
                                level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
            return False

    # 查询单条数据
    def select_one(self, condition):
        try:
            self.cur.execute(condition)
            results = self.cur.fetchone()
        except BaseException as e:
            results = 'sql001'
            logging.basicConfig(filename=os.path.join(os.getcwd(), './log.txt'),
                                level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        finally:
            return results

    # 查询所有数据
    def select_all(self, condition):
        try:
            self.cur.execute(condition)
            # 光标回到初始位置
            self.cur.scroll(0, mode='absolute')
            results = self.cur.fetchall()
        except BaseException as e:
            results = 'sql002'
            logging.basicConfig(filename=os.path.join(os.getcwd(), './log.txt'),
                                level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        finally:
            return results

    # 插入多条数据
    def insert_more(self, condition):
        try:
            self.cur.executemany(condition)
            self.conn.commit()
            results = True
        except BaseException as e:
            results = 'sql003'
            logging.basicConfig(filename=os.path.join(os.getcwd(), './log.txt'),
                                level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
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
    print(result)
