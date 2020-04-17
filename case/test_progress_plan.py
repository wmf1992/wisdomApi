#!/usr/bin/python
# -*- coding: UTF-8 -*-
from business.progress_plan import ProgressPlan
import unittest,logging,time
from mysqlDb.progress_plan_db import ProgressPlanDb
class TestProgressPlan(unittest.TestCase):
    '''
    状态：{
        -1：待提交
        -2：待录入
        0：审批中
    }
    '''

    def test_progress_plan_list_db(self,statu):
        P = ProgressPlanDb()
        id = P.progress_plan_list(statu)
        return id
    def test_progress_plan_index(self):
        '''测试进度计划列表接口'''  # 此注释将展示到测试报告的测试组类
        M = ProgressPlan()
        M.progress_plan_index()


    def test_progress_plan_detail(self):
        '''测试进度计划详情接口'''  # 此注释将展示到测试报告的测试组类
        M = ProgressPlan()
        plan_id = self.test_progress_plan_list_db(0)

        M.progress_plan_detail(plan_id)

    def test_progress_plan_add(self):
        '''测试添加进度计划接口'''  # 此注释将展示到测试报告的测试组类
        M = ProgressPlan()
        
        form_data = {
            "plan_time": "2016-02",
            "contract_id": '41',
            "building_id": 9,
            "plan_list[0][building_floor]": "地基",
            "plan_list[0][first_sub_project_id]": 1,
            "plan_list[0][parent_sub_project_id]": 2,
            "plan_list[0][sub_project_id]": 6,
            "plan_list[0][quantities_count]": 20,
            "plan_list[0][construction_norm_count]": 300,
            "plan_list[0][construction_norm_unit]": "元",
            "plan_list[0][quantities_unit]": "天",
            "plan_list[0][plan_num]": 30,
            "plan_list[0][plan_start_time]": "2020-02-12 07:00:00",
            "plan_list[0][plan_end_time]": "2020-03-07 22:00:00",
            "plan_list[0][start_hour]": 7,
            "plan_list[0][end_hour]": 22,
            "plan_list[0][work_ahead]": 4,
            "plan_list[0][work_after]": 5,
            "plan_list[0][duration]": 24,
            "plan_list[0][durationTime]": 15,
            "plan_list[0][sub_name]": "分项工程2修改",
            "plan_list[0][plan_time_diff]": "24天15时",
            "technical_disclosure[0][technical_disclosure_name]": "交底1",
            "technical_disclosure[0][plan_disclosure_time]": "2020-02-13",
            "technical_disclosure[0][files][0][file_name]": "库存计算规则.xlsx",
            "technical_disclosure[0][files][0][file_ext]": "xlsx",
            "technical_disclosure[0][files][0][url]": "http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/916b6b203b77ce0026381cf014f864a1.xlsx",
            "test_user": 5

        }
        M.progress_plan_add(form_data)
    def test_progress_plan_testSave(self):
        '''测试实验员录入数据接口'''  # 此注释将展示到测试报告的测试组类
        M = ProgressPlan()
        plan_id = self.test_progress_plan_list_db(-2)

        form_data = {
            "plan_id" :plan_id,
            "test_info[0][test_name]": "打扫地板",
            "test_info[0][plan_test_time]": "2020-02-14"
        }
        M.progress_plan_testSave(form_data)
    # 3、发起人提交审批
    def test_progress_plan_submit(self):
        '''测试发起人提交审批'''
        M = ProgressPlan()
        plan_id = self.test_progress_plan_list_db(-1)

        M.progress_plan_submit(plan_id)
    # 4.审批人审批
    def test_progress_plan_approval_add(self):
        '''测试审批人审批'''
        plan_id = self.test_progress_plan_list_db(0)
        M = ProgressPlan()
        form_data = {
            "progress_plan_id": plan_id,
            "approval_opinions": "无意见",
            "check": 1,
            "back": "",
            "score": 3,
            'files': '',
            'images': ''
        }
        M.progress_plan_approval_add(form_data)



if __name__ == '__main__':
    T = TestProgressPlan()

    T.test_progress_plan_index()
    # T.test_progress_plan_add()
    T.test_progress_plan_testSave()
    T.test_progress_plan_submit()
    T.test_progress_plan_approval_add()
    T.test_progress_plan_detail()