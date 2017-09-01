#! /usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'Meteor2703'


import urllib
import http.client
from BasicConfig import BasicConfig
import OPerationLog as OpLog


class HttpInterface(object):
    def __init__(self, path):
        self.cf = BasicConfig(path)

    def __http_code(self, url):
        try:
            if url != '':
                code = urllib.urlopen(url).getcode()
            else:
                code = '1001'
        except Exception as e:
            code = '9999'
            OpLog.write_error_log(e)
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
                    return "1002"
            elif interface_url == '':
                return "1003"
            else:
                return "1004"  # 接口地址有问题
        except Exception as e:
            OpLog.write_error_log(e)
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
            OpLog.write_error_log(e)
            return "9999"

    def http_request(self, interface_url, headerdata, param, type, environment='test_environment'):
        try:
            if type.upper() == "GET":
                result = self.__http_get(interface_url, headerdata, param, environment)
            elif type.upper() == "POST":
                result = self.__http_post(interface_url, headerdata, param, environment)
            else:
                result = '1005'
        except Exception as e:
            OpLog.write_error_log(e)
            return "9999"
        return result


if __name__ == "__main__":
    url = ""
    header_data = ""
    params = ""
    type1 = "GET"
    rq = HttpInterface()
    rq.http_request(url, headerdata=header_data, param=params, type=type1)
