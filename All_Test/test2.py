#! /usr/bin/env python
# _*_ coding:utf-8 _*_

from BasicConfig import BasicConfig
import os

path = os.path.split(os.path.realpath(__file__))[0] + '\\basic.ini'
cf = BasicConfig(path)
items = cf.get_all_items_by_section('database')
print(items)
