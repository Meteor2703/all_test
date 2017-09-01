#! /usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'Meteor2703'

import json
import OPerationLog as OpLog
from DBoperation import DbOperation

op_db = DbOperation()


class ResultOperation(object):
    def __init__(self, params_interface):
        self.params_interface = params_interface
        self.id_case = params_interface['id']
        self.result_list_response = []
        self.params_to_compare =params_interface['params_to_compare']
        self.code_name_to_compare = params_interface['code_to_compare']

    def compare_result_code(self, result_interface):
        """
        :param result_interface: 实际的响应结果
        :return: 返回一个字典，其中code：2000：相等，3000：不相等，3001：参数值比较错误，9999：返回数据错误
        """
        try:
            # loads：反序列化（字符串变更为python中的字典），dumps：序列化
            if json.loads(result_interface):
                temp_result_interface = json.loads(result_interface)
                if temp_result_interface.has_key(self.code_name_to_compare):
                    if temp_result_interface[self.code_name_to_compare] == self.params_interface['code_expect']:
                        result = {'code': '2000', 'message': u'关键字参数值相同', 'data': []}
                        sql = "UPDATE tb_interface SET result_interface='%s', code_actual='%s', result_code_compare='%s' WHERE id=%s" \
                              % (str(temp_result_interface), temp_result_interface[self.code_name_to_compare],0,self.id_case)
                        op_db.op_sql(sql)
                    elif temp_result_interface[self.code_name_to_compare] != self.params_interface['code_expect']:
                        result = {'code': '3000', 'message': u'关键字参数值不相同', 'data': []}
                        sql = "UPDATE tb_interface SET result_interface=%s, code_actual=%s, result_code_compare=%s WHERE id=%s"
                        op_db.op_sql(sql, (str(temp_result_interface), temp_result_interface[self.code_name_to_compare],1,self.id_case))
                    else:
                        result = {'code': '3001', 'message': u'关键字参数值比较错误', 'data': []}
                        sql = "UPDATE tb_interface SET result_interface=%s, code_actual=%s, result_code_compare=%s WHERE id=%s"
                        op_db.op_sql(sql, (str(temp_result_interface), temp_result_interface[self.code_name_to_compare], 3, self.id_case))
                else:
                    result = {'code': '9999', 'message': u'返回数据错误', 'data': []}
        except Exception as e:
            result = {'code': '9999', 'message': u'比较返回值code出现异常', 'data': []}
            sql = "UPDATE tb_interface SET result_interface=%s, result_code_compare=%s WHERE id=%s"
            op_db.op_sql(sql, (str(temp_result_interface), 9, self.id_case))
            OpLog.write_error_log('C:\Alex\Log', e)
        finally:
            return result

    # 循环获取返回参数的key
    def loop_get_result_params(self, result_interface):
        try:
            if isinstance(result_interface, str):
                result_dic = json.loads(result_interface)
            else:
                result_dic = result_interface
            if result_dic:
                for key,value in result_dic.items():
                    if isinstance(value, (list, dict)):
                        self.result_list_response.append(key)
                        for l in value:
                            # print(type(l))
                            self.loop_get_result_params(l)
                    else:
                        self.result_list_response.append(key)
            result = {'code': '2000', 'message': u'成功获取到返回参数的所有key', 'data': set(self.result_list_response)}
        except Exception as e:
            result = {'code': '9999', 'message': u'获取返回参数的key出错', 'data': []}
            OpLog.write_error_log('C:\Alex\Log', e)
        finally:
            # print(self.result_list_response)
            return result

    def compare_result_params_complete(self, result_interface):
        """
        :param result_interface: response值
        :return: 2000：完整，3002：不完整，3003：调用方法出错，9999：出现异常
        """
        try:
            temp_compare_params = self.loop_get_result_params(result_interface)
            if temp_compare_params['code'] == '2000':
                if set(self.params_to_compare).issubset(temp_compare_params['data']):
                    sql = "UPDATE tb_interface SET params_actual=%s, result_params_compare=%s WHERE id=%s"
                    sql_result = op_db.op_sql(sql, (str(temp_compare_params), 0, self.id_case))
                    if sql_result:
                        result = {'code': '2000', 'message': u'完整性比较结果是完整', 'data': sql_result}
                    else:
                        raise "执行sql报错，具体错误请查看错误日志"
                else:
                    sql = "UPDATE tb_interface SET params_actual=%s, result_params_compare=%s WHERE id=%s"
                    sql_result = op_db.op_sql(sql, (str(temp_compare_params), 1, self.id_case))
                    if sql_result:
                        result = {'code': '3002', 'message': u'完整性比较结果是不完整', 'data': sql_result}
                    else:
                        raise "执行sql报错，具体错误请查看错误日志"
            else:
                sql = "UPDATE tb_interface SET result_params_compare=%s WHERE id=%s"
                op_db.op_sql(sql, (2, self.id_case))
                result = {'code': '3003', 'message': u'调用loop_get_result_params出错', 'data': []}
        except Exception as e:
            sql = "UPDATE tb_interface SET result_params_compare=%s WHERE id=%s"
            op_db.op_sql(sql, (3, self.id_case))
            result = {'code': '9999', 'message': u'参数完整性比较异常', 'data': []}
            OpLog.write_error_log('C:\Alex\Log', e)
        finally:
            return result


if __name__ == "__main__":
    params_interface = {'table_name': 'test', 'update_time': '2017-8-21 00:52:44', 'result_interface': u'',
                        'result_code_compare': 0, 'exe_mode': u'post', 'code_to_compare': u'resultCode',
                        'params_actual': None, 'case_status': 0,
                        'params_interface': u'{"latitude": "NULL", "pageNo": 0, "longitude": "123.154212"}',
                        'result_params_compare': None, 'code_expect': u'000', 'code_actual': u'', 'create_time': None,
                        'exe_level': 0,
                        'url_interface': u'http://192.168.1.88:8080/personalOrder/getNearbyServiceMerchantList',
                        'header_interface': u'{"Content-Length": " 0", "UUID": " 862096032360278", "POSTFIX": " 9BCE6A51E0DDE0D759A55D199E691919CF3E492C9B77EA3985D6C2291B71A6274ABD93FA91EF65AC9660EC51C4D97DA1", "SYSTEM": " 5.1", "Host": " 192.168.1.88", "VERSION": " 2.6.1.161221", "User-Agent": " okhttp/3.3.1", "PHONE": " ", "Connection": " Keep-Alive", "CLIENT_TYPE": " 1", "APIVERSION": " 1.0", "TIME": " 1483597250589", "MODEL": " OPPO+R9m", "CLIENT_FLAG": " 1", "CHANNEL": " Default", "Accept-Encoding": " gzip"}',
                        'id': 1, 'params_to_compare': "[u'totalPage', u'pageNo', u'merchantInfos', u'userId']"}
    result_interface = '{"message": "获取附近服务商成功",' \
                       '"nextPage": 1,' \
                       '"pageNo": 0,' \
                       '"merchantInfos": ' \
                       '[{"phone": "15100000000",' \
                       '"star": 5,"totalQualityEvaluation": 0,"photoUrls": "","latitude": 0},' \
                       '{"phone": "15200000000","detail": null,"sex": null,"serviceFrequency": 0}],' \
                       '"resultCode": "000",' \
                       '"totalPage": 66746}'
    rs = ResultOperation(params_interface)
    ll = rs.compare_result_params_complete(result_interface)
    print(ll)