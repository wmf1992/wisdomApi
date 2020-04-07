from business.labour_services import LabourServicesView
import unittest,logging,time
class TestLabourServices(unittest.TestCase):
    def test_get_labour_services(self):
        '''测试劳务公司列表接口'''  # 此注释将展示到测试报告的测试组类
        L = LabourServicesView()
        print(34)
        L.get_labour_services()
    def test_get_labour_services_black(self):
        '''测试劳务公司黑名单列表接口'''  # 此注释将展示到测试报告的测试组类
        L = LabourServicesView()
        L.get_labour_services_black()
    def test_labour_services_add(self):
        '''测试添加劳务公司接口'''  # 此注释将展示到测试报告的测试组类
        L = LabourServicesView()
        T = time.time()
        intT = int(T)
        form_data = {
            'company_name': '劳务公司%d' %intT,
            'legal_person_name': '法定代表人01',
            'province_code': 150000,
            'city_code': 150100,
            'area_code': 150123,
            'address': '软件园',
            'contacts': '联系人01',
            'contacts_mobile': '18859663158',
            'original_business_license_id': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/22543476a8a01a20ba789efcb9a1b688.png',
            'copy_business_license_id': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/268290ab1a0e45b6974e19b9b1e421d6.png',
            'opening_permit_id': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/49753df0d37fd44cc210839e52e9fb3c.png',
            'letter_of_attorney_id': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/753837ac685f2206390123ab453f2015.jpg',
            'front_legal_person_idcard_id': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/5875577bb3fb889c3622bbac8df0cdfa.jpg',
            'back_legal_person_idcard_id': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/ab28e193d0621a56fea166a64932a4ed.jpg',
            'sort': 2
        }
        L.labour_services_add(form_data)