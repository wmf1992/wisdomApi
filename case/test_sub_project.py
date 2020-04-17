#!/usr/bin/python
# -*- coding: UTF-8 -*-
from business.sub_project import SubProject
import unittest,logging,time
from mysqlDb.sub_project import SubProjectDb
class TestSubProject(unittest.TestCase):
    '''
    状态：{
        -1：待提交
        -2：待录入
        0：审批中
    }
    '''

    def test_sub_project_list_db(self, statu):
        P = SubProjectDb()
        id = P.sub_project_list(statu)
        return id
    def test_sub_project_index(self):
        '''测试工程结算列表接口'''  # 此注释将展示到测试报告的测试组类
        M = SubProject()
        M.sub_project_index()


    def test_sub_project_detail(self):
        '''测试工程结算详情接口'''  # 此注释将展示到测试报告的测试组类
        S = SubProject()
        project_settlement_id = self.test_sub_project_list_db(0)
        data = S.sub_project_detail(project_settlement_id)
        # print(data)
        # 施工内容列表的id
        project_settlement_list_id = data['data']['project_settlement_list'][0]['id']
        return project_settlement_list_id

    def test_sub_project_add(self):
        '''测试添加工程结算接口'''  # 此注释将展示到测试报告的测试组类
        S = SubProject()
        form_data = {
            "start_time": "2020-02-11",
            "end_time": "2020-02-29",
            "contract_id": 232,
            "labor_contract_id": 242,
            "building_id": 131,
            "sub_project_ids": 6,
            "compliant": "委托人1",
            "project_side": "劳务公司110501",
            "pay_rate": 90,
            "labour_contract_id": "",
            "settlement_list[0][construction_content]": "粉刷墙壁",
            "settlement_list[0][quantities_count]": 1,
            "settlement_list[0][quantities_unit]": 1,
            "settlement_list[0][unit_price]": 200,
            "settlement_list[0][desc]": "无",
        }
        S.sub_project_add(form_data)
    def test_sub_project_check(self):
        '''测试工程结算审批接口'''  # 此注释将展示到测试报告的测试组类
        S = SubProject()
        project_settlement_id = self.test_sub_project_list_db(0)
        project_settlement_list_id = self.test_sub_project_detail()
        # print(project_settlement_id)
        # 不需要填写结算信息
        form_data = {
            "project_settlement_id": project_settlement_id,
            "approval_opinions": "无意见",
            "check": 1,
            "back": "",
            "score": 2

        }
        # 需要填写结算信息
        form_data_info = {
            "files": [],
            "images": [],
            "approval_opinions": "无",
            "score": 3,
            "check": 1,
            "project_settlement_id": project_settlement_id
        }

        checkCost_form_data = {
            'approval_quantities_count': 1,
            'approval_unit_price': 1000,
            'id': project_settlement_list_id
        }

        settingPayRate_form_data = {
            'project_settlement_id': project_settlement_id,
            'approval_pay_rate': 99
        }

        S.sub_project_check(form_data,form_data_info,checkCost_form_data,settingPayRate_form_data)

if __name__ == '__main__':
    T = TestSubProject()
    T.test_sub_project_add()
    T.test_sub_project_check()
    # T.test_sub_project_detail()
    # T.test_sub_project_index()