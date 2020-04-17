#!/usr/bin/python
# -*- coding: UTF-8 -*-
from business.month_bulk_meterial_plan import MonthBulkMeterialPlan
import unittest,logging,time
class TestMonthBulkMeterialPlan(unittest.TestCase):
    '''
       状态：{
           -1：待提交
           -2：待录入
           0：审批中
       }
       '''
    def test_month_bulk_meterial_plan_index(self):
        '''测试月大宗材料计划列表接口'''  # 此注释将展示到测试报告的测试组类
        M = MonthBulkMeterialPlan()
        M.month_bulk_meterial_plan_index()

    def test_month_bulk_meterial_plan_detail(self):
        '''测试月大宗材料计划详情页接口'''  # 此注释将展示到测试报告的测试组类
        M = MonthBulkMeterialPlan()
        M.month_bulk_meterial_plan_detail()
    def test_month_bulk_meterial_plan_add(self):
        '''测试月大宗材料计划添加接口'''  # 此注释将展示到测试报告的测试组类
        M = MonthBulkMeterialPlan()
        M.month_bulk_meterial_plan_add()
    def test_month_bulk_meterial_plan_approval(self):
        '''测试月大宗材料计划审批接口'''  # 此注释将展示到测试报告的测试组类
        M = MonthBulkMeterialPlan()
        M.month_bulk_meterial_plan_approval()
