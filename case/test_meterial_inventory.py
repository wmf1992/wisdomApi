#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest,logging,time
from mysqlDb.meterial_inventory_db import MeterialInventoryDb
from business.meterial_inventory import MeterialInventory

class TestMeterialInventory(unittest.TestCase):
    '''
       状态：{
           -1：待提交
           -2：待录入
           0：审批中
       }
       '''
    def test_meterial_inventory_db(self, statu):
        P = MeterialInventoryDb()
        id = P.meterial_inventory_list(statu)
        return id
    def test_meterial_inventory_index(self):
        M= MeterialInventory()
        M.meterial_inventory_index()


    def test_meterial_inventory_detail(self):
        M = MeterialInventory()
        access_id = self.test_meterial_inventory_db(1)
        M.meterial_inventory_detail(access_id)

    def test_meterial_inventory_add(self):
        M = MeterialInventory()
        form_data = {
            "access_code": "",
            "access_time": '2019-09',
            "warehouse_id":6,
            "meterial_list[0][id]": 3,
            "meterial_list[0][meterial_code]": 'HDPE',
            "meterial_list[0][meterial_name]": "臻力 塑料垃圾桶",
            "meterial_list[0][parent_type_id]": 6,
            "meterial_list[0][second_type_id]": 8,
            "meterial_list[0][type_id]": 112,
            "meterial_list[0][meterial_spec]": "240L",
            "meterial_list[0][meterial_unit]": "套",
            "meterial_list[0][image]": "https://img0.912688.com/4a478b1f-b471-4b11-b7e4-452a20c35b89.jpg#",
            "meterial_list[0][is_need_approval]": 0,
            "meterial_list[0][type_text]": "复合材料三级",
            "meterial_list[0][meterial_id]": 3,
            "meterial_list[0][meterial_total_stock]": 12,
            "meterial_list[0][stock_num]": 12,
            "meterial_list[0][diff_num]": 3,
            "meterial_list[0][desc]":"",
            "meterial_list[0][num]": 15,
            "meterial_list[0][product_time]": "2020-02-12",
            "meterial_list[0][expire_time]": "2020-02-28",
            "meterial_list[0][unit_price]": 44
        }
        M.meterial_inventory_add(form_data)

    def test_inventory_approval_check(self):
        M = MeterialInventory()
        access_id = self.test_meterial_inventory_db(0)

        form_data = {
            "access_id": access_id,
            "approval_opinions": "无意见",
            "check": 1,
            "back": "",
            "score": 1,
            "images": "",
            "files": ""
        }
        M.inventory_approval_check(form_data)
if __name__ == '__main__':
    T = TestMeterialInventory()
    T.test_meterial_inventory_add()
    T.test_meterial_inventory_detail()
    T.test_meterial_inventory_index()
    T.test_inventory_approval_check()