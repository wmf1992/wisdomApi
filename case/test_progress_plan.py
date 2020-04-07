from business.progress_plan import ProgressPlan
import unittest,logging,time
class TestProgressPlan(unittest.TestCase):
    def test_progress_plan_index(self):
        '''测试进度计划列表接口'''  # 此注释将展示到测试报告的测试组类
        M = ProgressPlan()
        M.progress_plan_index()
    def test_progress_plan_detail(self):
        '''测试进度计划详情接口'''  # 此注释将展示到测试报告的测试组类
        M = ProgressPlan()
        M.progress_plan_detail()