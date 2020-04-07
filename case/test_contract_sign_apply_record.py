from business.contract_sign_apply_record import ContractSignApplyRecordView
import unittest,logging,time
class TestContractSignApplyRecord(unittest.TestCase):
    '''测试合同签订申请'''  # 此注释将展示到测试报告的测试组类
    def test_contract_sign_apply_record_index(self):
        '''测试合同签订申请列表接口'''  # 此注释将展示到测试报告的测试组类
        t = ContractSignApplyRecordView()
        t.contract_sign_apply_record_index()
    def test_contract_sign_apply_record_add(self):
        '''测试合同签订申请添加接口'''  # 此注释将展示到测试报告的测试组类
        t = ContractSignApplyRecordView()
        form_data = {
            'contract_id': 78,
            'building_id': '',
            'apply_code': 'SQ030700001',
            'b_name': '乙方',
            'workload': '50天',
            'cost_price': '600000000',
            'plan_time': '2020-03-17',
            'project_address': '福建省厦门市集美区软件园三期',
            'construction_scope': '软件园所有的绿化带',
            'description': '翻种草坪',
            'case_description': '所有的草坪必须替换最新品种的草',
            'labour_contract_id': ''
        }
        t.contract_sign_apply_record_add(form_data)