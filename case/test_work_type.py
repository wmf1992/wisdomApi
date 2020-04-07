from business.worktypeView import WorktypeView
import unittest,logging,time
class TestWorkType(unittest.TestCase):
    def test_work_type(self):
        '''测试工种列表接口'''  # 此注释将展示到测试报告的测试组类
        M = WorktypeView()
        M.work_type()
    def test_work_type_add(self):
        '''测试添加工种接口'''  # 此注释将展示到测试报告的测试组类
        M = WorktypeView()
        T = time.time()
        intT = int(T)
        form_data = {
            'work_num': 'ZZ0317%d' %intT,
            'work_name': '装潢工'
        }
        M.work_type_add(form_data)