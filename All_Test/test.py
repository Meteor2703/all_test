#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import time
import datetime
import ctypes as ct
import subprocess as sb

print(time.localtime())

print(time.clock())

# time.sleep(3)

print(datetime.datetime.now())
print(datetime.date.isoweekday(datetime.datetime.now()))
# print(datetime.time.second())

d = datetime.datetime.now()
print(d.day, d.hour, d.second)
d2 = d + datetime.timedelta(days=10)
# print(d2)
# libc = ct.cdll.msvcrt
# drivers ="ABCDEFGHIJK"
# driver_list = libc._getdrivers()
# for n in range(26):
#     mask = 1 << n
#     if driver_list & mask :
#         print(drivers[n], 'is available')

sb.call(['cmd', '/c', 'pip list', '/b'])
sb.call([])