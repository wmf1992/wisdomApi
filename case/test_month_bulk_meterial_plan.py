#!/usr/bin/python
# -*- coding: UTF-8 -*-
from business.month_bulk_meterial_plan import MonthBulkMeterialPlan
import unittest,logging,time
from mysqlDb.month_bulk_meterial_plan_db import MonthBulkMeterialPlanDb
class TestMonthBulkMeterialPlan(unittest.TestCase):
    '''
       状态：{
           -1：待提交
           -2：待录入
           0：审批中
       }
       '''
    def test_month_bulk_meterial_plan_db(self, statu):
        P = MonthBulkMeterialPlanDb()
        id = P.month_bulk_meterial_list(statu)
        return id
    def test_month_bulk_meterial_plan_index(self):
        '''测试月大宗材料计划列表接口'''  # 此注释将展示到测试报告的测试组类
        M = MonthBulkMeterialPlan()
        M.month_bulk_meterial_plan_index()

    def test_month_bulk_meterial_plan_detail(self):
        '''测试月大宗材料计划详情页接口'''  # 此注释将展示到测试报告的测试组类
        M = MonthBulkMeterialPlan()
        plan_id = self.test_month_bulk_meterial_plan_db(0)
        M = MonthBulkMeterialPlan()
        M.month_bulk_meterial_plan_detail(plan_id)
    def test_month_bulk_meterial_plan_add(self):
        '''测试月大宗材料计划添加接口'''  # 此注释将展示到测试报告的测试组类
        M = MonthBulkMeterialPlan()
        form_data = {
            "contract_id": 41,
            "building_id": 9,
            "plan_time": '2018-02',
            "meterial_list": '[{"meterial_code":"CL12050005","meterial_name":"法国牛排","parent_type_id":6,"second_type_id":8,"type_id":112,"meterial_spec":"500g","meterial_unit":"盒","image":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/e60795e82fd44d539ebb15c1bef823c2.jpg","is_need_approval":1,"type_text":"复合材料三级","meterial_id":13,"desc":"","plan_num":2,"enter_time":"2020-02-11"}]'

        }
        M.month_bulk_meterial_plan_add(form_data)
    def test_month_bulk_meterial_plan_approval(self):
        '''测试月大宗材料计划审批接口'''  # 此注释将展示到测试报告的测试组类
        M = MonthBulkMeterialPlan()
        plan_id = self.test_month_bulk_meterial_plan_db(0)
        form_data = {
            "plan_id": plan_id,
            "approval_opinions": "无意见",
            "check": 1,
            "back": "",
            "score": 1,
            "images": "",
            "files": ""
        }
        M.month_bulk_meterial_plan_approval(form_data)
if __name__ == '__main__':
    T = TestMonthBulkMeterialPlan()
    T.test_month_bulk_meterial_plan_add()
    T.test_month_bulk_meterial_plan_approval()
    T.test_month_bulk_meterial_plan_detail()
    T.test_month_bulk_meterial_plan_index()