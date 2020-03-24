from business.baseMenu import BaseMenu
import unittest,logging,time
class TestBaseMenu(unittest.TestCase):
    '''测试/rule/leftMenu接口'''  # 此注释将展示到测试报告的测试组类
    def test_base_menu(self):
        '''测试/rule/leftMenu列表接口'''  # 此注释将展示到测试报告的测试组类
        t = BaseMenu()
        t.leftMenu()
    def test_behavior(self):
        '''测试/rule/behavior'''
        t = BaseMenu()
        t.behavior()
    def test_user_info(self):
        '''测试/user/info接口'''  # 此注释将展示到测试报告的测试组类
        t = BaseMenu()
        t.userInfo()
    def test_toDoBusiness(self):
        '''测试/index/toDoBusiness接口'''  # 此注释将展示到测试报告的测试组类
        t = BaseMenu()
        t.toDoBusiness()

    def test_toDoList(self):
        '''测试/index/toDoList'''  # 此注释将展示到测试报告的测试组类
        t = BaseMenu()
        t.toDoList()





if __name__ == '__main__':
    l = TestBaseMenu()
    l.test_base_menu()
    l.test_behavior()
