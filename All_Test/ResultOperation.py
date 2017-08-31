#! /usr/bin/env python
# _*_ coding:utf-8 _*_
import json
import OPerationLog
import DBoperation

op_db = DBoperation()


class ResultOperation(object):
    def __init__(self, params_interface):
        self.params_interface = params_interface
        self.id_case = params_interface['id']
        self.result_list_response = params_interface[]
        self.params_to_compare =params_interface['params_to_compare']
        self.code_name_to_compare = params_interface['code_to_compare']

    def compare_result_code(self, result_interface):
        try:
            if json.loads(result_interface):
                temp_result_interface = json.loads(result_interface)
                if temp_result_interface.has_key(self.code_name_to_compare):
                    if temp_result_interface[self.code_name_to_compare] == self.params_interface['code_expect']:
                        result = {'code': '200', 'message': u'关键字参数值相同', 'data': []}
                        sql = "UPDATE tb_interface SET result_interface=%s, code_actual=%s, result_code_compare=%s WHERE id=%s" \
                              % (temp_result_interface, temp_result_interface[self.code_name_to_compare],0,self.id_case)
                        op_db.op_sql(sql)
                    elif temp_result_interface[self.code_name_to_compare] != self.params_interface['code_expect']:
                        result = {'code': '300', 'message': u'关键字参数值不相同', 'data': []}
                        sql = "UPDATE tb_interface SET result_interface=%s, code_actual=%s, result_code_compare=%s WHERE id=%s"
                        op_db.op_sql(sql, (temp_result_interface, temp_result_interface[self.code_name_to_compare],1,self.id_case))
                    else:
                        result = {'code': '400', 'message': u'关键字参数值比较错误', 'data': []}
                        sql = "UPDATE tb_interface SET result_interface=%s, code_actual=%s, result_code_compare=%s WHERE id=%s"
                        op_db.op_sql(sql, (temp_result_interface, temp_result_interface[self.code_name_to_compare], 3, self.id_case))
                else:
                    result = {'code': '200', 'message': u'不包含此关键字code', 'data': []}



    def compare_result_params(self, result_interface):
        pass

    def compare_result_params_complete(self, result_interface):
        pass

if __name__ == "__main__":
    pass