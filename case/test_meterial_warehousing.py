#!/usr/bin/python
# -*- coding: UTF-8 -*-
from business.meterial_warehousing import  MeterialWarehousing
import unittest,logging,time
from mysqlDb.meterial_warehousing_db import MeterialWarehousingDb
class TestMeterialWarehousing(unittest.TestCase):
    '''
       状态：{
           -1：待提交
           -2：待录入
           0：审批中
       }
       '''
    def test_meterial_warehousing_db(self, statu):
        P = MeterialWarehousingDb()
        id = P.meterial_warehousing_list(statu)
        return id
    def test_meterial_warehousing_index(self):
        M= MeterialWarehousing()
        M.meterial_warehousing_index()


    def test_meterial_warehousing_detail(self):
        M = MeterialWarehousing()
        access_id = self.test_meterial_warehousing_db(1)
        M.meterial_warehousing_detail(access_id)

    def test_meterial_warehousing_add(self):
        M = MeterialWarehousing()
        form_data = {
            "purchasing_id": 149,
            "is_end_purchasing": 0,
            "access_code": "",
            "access_time": '2020-02-12',
            "warehouse_id": 26,
            "building_id": 3,
            "warehouse_name": "仓库2020010201",
            "building_id": 143,
            "meterial_list[0][meterial_id]": 112,
            "meterial_list[0][num]": 1,
            "meterial_list[0][meterial_name]": "GUTFUG",
            "meterial_list[0][meterial_code]": "R454RYGFHG",
            "meterial_list[0][image]": "http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/64e8c6f5dc105152bfaca08dec2b9f4f.gif",
            "meterial_list[0][unit_price]": 12,
            "meterial_list[0][product_time]": "2020-02-01",
            "meterial_list[0][expire_time]": "2020-02-14"
        }
        M.meterial_warehousing_add(form_data)

    def test_warehousing_approval_check(self):
        M = MeterialWarehousing()
        access_id = self.test_meterial_warehousing_db(0)

        form_data = {
            "access_id": access_id,
            "approval_opinions": "无意见",
            "check": 1,
            "back": "",
            "score": 1,
            "images": "",
            "files": ""
        }
        M.warehousing_approval_check(form_data)
if __name__ == '__main__':
    T = TestMeterialWarehousing()
    T.test_meterial_warehousing_add()
    T.test_warehousing_approval_check()
    T.test_meterial_warehousing_detail()
    T.test_meterial_warehousing_index()