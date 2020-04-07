from business.meterial import MeterialView
import unittest,logging,time
class TestMeterial(unittest.TestCase):
    def test_get_meterial(self):
        '''测试材料列表接口'''  # 此注释将展示到测试报告的测试组类
        M = MeterialView()
        M.get_meterial()
    def test_meterial_add(self):
        '''测试添加材料接口'''  # 此注释将展示到测试报告的测试组类
        M = MeterialView()
        form_data = {
            'image': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/a9f15e98bff56309f3bb31739420e1df.jpg',
            'meterial_code': '',
            'meterial_name': 'huanghua菜',
            'type_name': '',
            'type_id': 127,
            'meterial_spec': 500,
            'meterial_unit': 'g',
            'warning_num': '',
            'parent_type_id': 6,
            'second_type_id': 8
        }
        M.meterial_add(form_data)
    def test_get_meterial_approval(self):
        '''测试材料审核列表接口'''  # 此注释将展示到测试报告的测试组类
        M = MeterialView()
        M.get_meterial_approval()
    def test_meterial_approval_check(self):
        '''测试添加材料审批通过接口'''  # 此注释将展示到测试报告的测试组类
        M = MeterialView()
        form_data = {

            'meterial_code': 'CL031804',
            'meterial_name': '娃娃菜',
            'parent_type_id': 6,
            'second_type_id': 8,
            'type_id': 127,
            'meterial_spec': 500,
            'meterial_unit': 'g',
            'image': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/a9f15e98bff56309f3bb31739420e1df.jpg',
            'warning_num': 20,
            'is_need_approval': 1,
            'edit_user': 3,
            'create_time': '2020-04-07',
            'status': 0,
            'type_text': '三级金属',
            'status_text': '审批中',
            'edit_username': '总经理张三01',
            'is_approval_right': 1,
            'files': '',
            'images': '',
            'approval_opinions': '无意见',
            'check': 1,

        }
        M.meterial_approval_check(form_data)