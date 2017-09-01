#! /usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'Meteor2703'

import configparser
import os

# 默认配置文件地址
init_path = os.path.split(os.path.realpath(__file__))[0] + '\\basic.ini'


class BasicConfig(object):
    def __init__(self, file_path=init_path):
        self.path = file_path

    # 获取config配置文件
    def get_config_by_key(self, section, key):
        config = configparser.ConfigParser()
        # path = os.path.split(os.path.realpath(__file__))[0] + '\\basic.ini'
        config.read(self.path)
        return config.get(section, key)

    # 获取所有的节点
    def get_all_sections(self):
        config = configparser.ConfigParser()
        config.read(self.path)
        return config.sections()

    # 根据节点获取下面的所有操作项keys
    def get_all_keys_by_section(self, section):
        config = configparser.ConfigParser()
        config.read(self.path)
        return config.options(section)

    # 根据节点获取下面所有操作项的items
    def get_all_items_by_section(self, section):
        config = configparser.ConfigParser()
        config.read(self.path)
        return config.items(section)


if __name__ == "__main__":
    path = os.path.split(os.path.realpath(__file__))[0] + '\\basic.ini'
    config = BasicConfig(path)
    # ll = config.get_config_by_key('database', 'dbhost')
    # print(ll)
    # l1 = config.get_all_sections()
    # print(l1)
    # l2 = config.get_all_keys_by_section('database')
    # print(l2)
    l3 = config.get_all_items_by_section('database')
    l4 = dict(l3)
    print(l4)
