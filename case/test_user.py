from business.userView import UserView
import unittest,logging,time
class TestUsers(unittest.TestCase):
    def test_users(self):
        '''测试员工列表接口'''  # 此注释将展示到测试报告的测试组类
        M = UserView()
        M.users()

    def test_userinfo(self):
        '''测试员工详情页接口'''  # 此注释将展示到测试报告的测试组类
        M = UserView()
        M.userinfo()