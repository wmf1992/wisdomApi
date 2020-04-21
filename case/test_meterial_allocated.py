#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest,logging,time
from business.meterial_allocated import MeterialAllocated

class TestMeterialAllocated(unittest.TestCase):
    '''
       状态：{
           -1：待提交
           -2：待录入
           0：审批中
       }
       '''

    def test_meterial_allocated_index(self):
        M= MeterialAllocated()
        M.meterial_allocated_index()


    def test_meterial_allocated_detail(self):
        M = MeterialAllocated()
        M.meterial_allocated_detail(8)

    def test_meterial_allocated_add(self):
        M = MeterialAllocated()
        form_data = {
            'access_code': '',
            'access_time': '2020-04-21',
            'warehouse_id': 6,
            'to_warehouse_id': 8,
            'meterial_list': '[{"meterial_id":13,"num":73}]'
        }

        M.meterial_allocated_add(form_data)

