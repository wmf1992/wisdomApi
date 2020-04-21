#!/usr/bin/python
# -*- coding: UTF-8 -*-
from business.meterial_outbound import  MeterialOutbound
import unittest,logging,time
from mysqlDb.meterial_outbound_db import MeterialOutboundDb
class TestMeterialOutbound(unittest.TestCase):
    '''
       状态：{
           -1：待提交
           -2：待录入
           0：审批中
       }
       '''
    def test_meterial_outbound_db(self, statu):
        P = MeterialOutboundDb()
        id = P.meterial_outbound_list(statu)
        return id
    def test_meterial_outbound_index(self):
        M= MeterialOutbound()
        M.meterial_outbound_index()


    def test_meterial_outbound_detail(self):
        M = MeterialOutbound()
        access_id = self.test_meterial_outbound_db(1)
        M.meterial_outbound_detail(access_id)

    def test_meterial_outbound_add(self):
        M = MeterialOutbound()
        form_data = {
            "plan_id": 288,
            "access_code": "",
            "access_time": '2020-02-11',
            "warehouse_id": 6,
            "building_id": 9,
            "meterial_list": '[{"meterial_id":13,"meterial_name":"法国牛排","meterial_code":"CL12050005","num":1,"froze_num":2,"stock_num":18,"image":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/e60795e82fd44d539ebb15c1bef823c2.jpg"}]',
            "images": '[{"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/466f868eeae9c2b23e575dd4f9277420.jpg","file_name":"QQ图片20191017144139.jpg","file_ext":"jpg","width":0,"height":0,"type":0}]',
            "files": '[{"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/916b6b203b77ce0026381cf014f864a1.xlsx","file_name":"库存计算规则.xlsx","file_ext":"xlsx","width":0,"height":0,"type":1}]'

        }
        M.meterial_outbound_add(form_data)

    def test_outbound_approval_check(self):
        M = MeterialOutbound()
        access_id = self.test_meterial_outbound_db(0)

        form_data = {
            "access_id": access_id,
            "approval_opinions": "无意见",
            "check": 1,
            "back": "",
            "score": 1,
            "images": "",
            "files": ""
        }
        M.outbound_approval_check(form_data)
if __name__ == '__main__':
    T = TestMeterialWarehousing()
    T.test_meterial_outbound_add()
    T.test_outbound_approval_check()
    T.test_meterial_outbound_detail()
    T.test_meterial_outbound_index()