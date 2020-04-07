from business.contractView import ContractView
import unittest,logging,time
class TestContract(unittest.TestCase):
    def test_contract(self):
        '''测试合同列表接口'''  # 此注释将展示到测试报告的测试组类
        C = ContractView()
        C.contracts()
    def test_contract_apply_record(self):
        '''测试合同查阅记录请求接口'''  # 此注释将展示到测试报告的测试组类
        C = ContractView()
        C.contract_apply_record()
    def test_labourContract_add(self):
        '''测试添加劳务合同接口'''  # 此注释将展示到测试报告的测试组类
        C = ContractView()
        form_data = {
            'files[0][url]': 'http: // wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com / file / b1c1e9d22380c8c74502a3e1d68def4f.doc',
            'files[0][file_name]': 'q.doc',
            'files[0][file_ext]': 'doc',
            'files[0][width]': 0,
            'files[0][height]': 0,
            'files[1][url]': 'http: // wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com / file / b1c1e9d22380c8c74502a3e1d68def4f.doc',
            'files[1][file_name]': 'q.doc',
            'files[1][file_ext]': 'doc',
            'files[1][width]': 0,
            'files[1][height]': 0,

            'apply[0][id]': 3,
            'apply[1][id]': 4,
            'apply[2][id]': 5,
            'apply[3][id]': 69,
            'apply[4][id]': 73,
            'contract_type': 2,

            'contract_id': 254,
            'contract_name': '劳务合同0316001',
            'signing_time': '2020-03-16',
            'start_time': '2020-04-01',
            'end_time': '2023-05-06',
            'contract_money': 50000000,
            'bond_money': 20000,
            'labour_services_company': 6,
            'project_side': '项目方01',
            'compliant': '履约委托人01',
            'project_manager': 4,
            'desc': 'description0001'

        }
        C.labourContract_add(form_data)
    def test_contract_add(self):
        '''测试添加招标合同接口'''  # 此注释将展示到测试报告的测试组类
        C = ContractView()
        form_data = {
            'files[0][url]': 'http: // wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com / file / b1c1e9d22380c8c74502a3e1d68def4f.doc',
            'files[0][file_name]': 'q.doc',
            'files[0][file_ext]': 'doc',
            'files[0][width]': 0,
            'files[0][height]': 0,
            'apply[0][id]': 3,
            'apply[1][id]': 4,
            'apply[2][id]': 5,
            'apply[3][id]': 69,
            'apply[4][id]': 73,
            'contract_type': 1,
            'contract_name': '招标合同0316002',
            'signing_time': '2020-03-16',
            'start_time': '2020-04-01',
            'end_time': '2023-05-06',
            'contract_money': 50000000,
            'bond_money': 20000,
            'project_side': '项目方01',
            'compliant': '履约委托人01',
            'project_manager': 4,
            'desc': 'description0001'

        }
        C.contract_add(form_data)