from business.staffView import StafView
import unittest,logging,time
class TestStaff(unittest.TestCase):
    def test_get_staff(self):
        '''测试劳务人员列表接口'''  # 此注释将展示到测试报告的测试组类
        M = StafView()
        M.get_staff()

    def test_labourForceDetails(self):
        '''测试劳务人员详情页接口'''  # 此注释将展示到测试报告的测试组类
        M = StafView()
        M.labourForceDetails()
    def test_get_staff_black(self):
        '''测试劳务人员黑名单列表接口'''  # 此注释将展示到测试报告的测试组类
        M = StafView()
        M.get_staff_black()
    def test_staff_add(self):
        '''测试添加劳务人员接口'''  # 此注释将展示到测试报告的测试组类
        M = StafView()
        T = time.time()
        intT = int(T)
        form_data = {
            'avatar': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/a3d11afa6a8ae82938f1070ae1c4022c.jpg',
            'name': '劳务人员031702',
            'staff_num': 'LWRY%d' %intT,
            'work_type_id': 30,
            'gender': 1,
            'province_code': 150000,
            'city_code': 150100,
            'birthday': '1981-04-03',
            'mobile': '18859663968',
            'company_id': 9,
            'major_years': '5年',
            'initiation_time': '2011-06-01',
            'level': '5级',
            'id_num': '350524199205105568',
            'card_img_front': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/7f9dfa436d0f2d988d95700221e34889.jpg',
            'card_img_back': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/7f9dfa436d0f2d988d95700221e34889.jpg'
        }
        M.staff_add(form_data)