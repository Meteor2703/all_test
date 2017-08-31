#! /usr/bin/env python
# _*_ coding:utf-8 _*_

import urllib
import logging
import os
import http.client
from BasicConfig import BasicConfig


class HttpInterface(object):
    def __init__(self, path):
        self.cf = BasicConfig(path)

    def __http_code(self, url):
        try:
            if url != '':
                code = urllib.urlopen(url).getcode()
            else:
                code = '1000'
        except Exception as e:
            code = '9999'
            logging.basicConfig(filename=os.path.join(os.getcwd(), './log.txt'),
                                level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
        return code

    def __http_get(self, interface_url, headerdata, param, environment='test_environment'):
        try:
            if interface_url != '':
                requrl = interface_url + param
                httpClient = http.client.HTTPConnection(self.cf.get_config_by_key(environment, 'host'),
                                                        port=self.cf.get_config_by_key(environment, 'port'),
                                                        timeout=self.cf.get_config_by_key(environment, 'timeout')
                                                        )
                httpClient.request('GET', requrl, body=None, headers=headerdata)
                response = httpClient.getresponse()
                print(response)
                if response.status == 200:
                    return response.read()
                else:
                    return "3004"
            elif interface_url == '':
                return "3002"
            else:
                return "3003"  # 接口地址有问题
        except Exception as e:
            logging.basicConfig(filename=os.path.join(os.getcwd(), './log.txt'),
                                level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
            return "9999"

    def __http_post(self, interface_url, headerdata, param, environment='test_environment'):
        try:
            if interface_url != '':
                httpClient = http.client.HTTPConnection(self.cf.get_config_by_key(environment, 'host'),
                                                        port=self.cf.get_config_by_key(environment, 'port'),
                                                        timeout=self.cf.get_config_by_key(environment, 'timeout')
                                                        )
                httpClient.request('GET', interface_url, body=param, headers=headerdata)
                response = httpClient.getresponse()
                print(response)
                if response.status == 200:
                    return response.read()
                else:
                    return "3004"
            elif interface_url == '':
                return "3002"
            else:
                return "3003"  # 接口地址有问题
        except Exception as e:
            logging.basicConfig(filename=os.path.join(os.getcwd(), './log.txt'),
                                level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
            return "9999"

    def http_request(self, interface_url, headerdata, param, type, environment='test_environment'):
        try:
            if type.upper() == "GET":
                result = self.__http_get(interface_url, headerdata, param, environment)
            elif type.upper() == "POST":
                result = self.__http_post(interface_url, headerdata, param, environment)
            else:
                result = '1000'
        except Exception as e:
            logging.basicConfig(filename=os.path.join(os.getcwd(), './log.txt'),
                                level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
            logger = logging.getLogger(__name__)
            logger.exception(e)
            return "9999"
        return result


if __name__ == "__main__":
    url = ""
    header_data = ""
    params = ""
    type1 = "GET"
    rq = HttpInterface()
    rq.http_request(url, headerdata=header_data, param=params, type=type1)
