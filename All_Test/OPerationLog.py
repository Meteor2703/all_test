#! /usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'Meteor2703'

import logging
import os


# 写error级别的日志。
def write_error_log(message, file_dir='C:\Alex\Log', filemode='a'):
    """
    :param file_dir: 日志文件目录
    :param message: 异常日志
    :param filemode: 写日志模式，默认为'a'，可选择项为：'a'\'w'
    :return: 无返回值
    """
    logging.basicConfig(filename=os.path.join(file_dir, './ErrorLog.txt'),
                        level=logging.DEBUG,
                        filemode=filemode,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    logger = logging.getLogger(__name__)
    logger.exception(message)
 

# 记录info
def write_info_log(message, file_dir='C:\Alex\Log', filemode='a'):
    """
    :param file_dir: 日志文件目录
    :param message: 日志详情
    :param filemode: 写日志模式，默认为'a'，可选择项为：'a'\'w'
    :return: 无返回值
    """
    logging.basicConfig(filename=os.path.join(file_dir, './InfoLog.txt'),
                        level=logging.DEBUG,
                        filemode=filemode,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    logger = logging.getLogger(__name__)
    logger.info(message)


# 记录debug日志
def write_debug_log(message, file_dir='C:\Alex\Log', filemode='a'):
    """
    :param file_dir: 日志文件目录
    :param message: 日志详情
    :param filemode: 写日志模式，默认为'a'，可选择项为：'a'\'w'
    :return: 无返回值
    """
    logging.basicConfig(filename=os.path.join(file_dir, './DebugLog.txt'),
                        level=logging.DEBUG,
                        filemode=filemode,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    logger = logging.getLogger(__name__)
    logger.debug(message)


# 记录warning日志
def write_warning_log(message, file_dir='C:\Alex\Log', filemode='a'):
    """
    :param file_dir: 日志文件目录
    :param message: 日志详情
    :param filemode: 写日志模式，默认为'a'，可选择项为：'a'\'w'
    :return: 无返回值
    """
    logging.basicConfig(filename=os.path.join(file_dir, './WarningLog.txt'),
                        level=logging.DEBUG,
                        filemode=filemode,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    logger = logging.getLogger(__name__)
    logger.warning(message)

if __name__ == "__main__":
    write_error_log('C:\Alex\Log', "this is exception", filemode='w')