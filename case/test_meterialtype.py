from business.meterialtypeView import MeterialtypeView
import unittest,logging,time
class TestMeterialtype(unittest.TestCase):
    def test_get_meterial_type(self):
        '''测试材料分类列表'''
        print(333)
        M=MeterialtypeView()
        M.get_meterial_type()
    def test_meterial_type_add(self):
        '''测试添加材料分类'''
        M = MeterialtypeView()
        M.meterial_type_add()