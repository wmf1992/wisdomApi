from business.technical_disclosure_scheme import technicalDisclosureSchemeView
import unittest,logging,time
class TechnicalDisclosureScheme(unittest.TestCase):
    '''测试技术交底接口'''  # 此注释将展示到测试报告的测试组类
    def test_technical_disclosure_scheme_list(self):
        '''测试技术交底u列表接口'''  # 此注释将展示到测试报告的测试组类
        t = technicalDisclosureSchemeView()
        t.technical_disclosure_scheme()
    def test_technical_disclosure_scheme_add(self):
        '''测试添加技术交底与方案表单接口'''  # 此注释将展示到测试报告的测试组类
        t = technicalDisclosureSchemeView()
        data = {
            'sub_project_id': 6,
            'contract_id': 4,
            'building_id': 15,
            'plan_time': '2020-03-24',
            # 'contract_id': 4,
            'type': 1,
            'modify_ids': '',
            'description': 'description00',
            'page_num': 1,
            'files': '[{"file_name":"q.doc","file_ext":"doc","width":0,"height":0,"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/b1c1e9d22380c8c74502a3e1d68def4f.doc"}]',
            'labour_contract_id': ''
        }
        t.technical_disclosure_scheme_add(data)
    # 测试技术交底与方案待审核接口
    def test_technical_disclosure_scheme_approval(self):
        '''测试技术交底与方案待审核接口'''  # 此注释将展示到测试报告的测试组类
        t = technicalDisclosureSchemeView()
        data = {
            'approval_type': 1,
            'sub_project_id': 6,
            'plan_code': 'RJYGY-JSJDFA-15-00015',
            'contract_name': '软件园公寓',
            'building_num': '软三b区',
            'plan_start_time': '2020-03-06',
            'plan_end_time': '2020-03-28',
            'plan_type': '',
            'edit_username': '总经理张三0',
            'status': '',
            'create_start_time': '2020-02-24',
            'create_end_time': '2020-04-04',
            'page': 1,
            'page_size': 10,
        }

        t.technical_disclosure_scheme_approval(data)
    # 测试技术交底与方案详情页
    def test_technical_disclosure_scheme_detail(self):
        '''测试技术交底与方案详情页接口'''  # 此注释将展示到测试报告的测试组类
        detailID =70
        t = technicalDisclosureSchemeView()
        t.technical_disclosure_scheme_detail(detailID)

    # 测试技术交底与方案审批详情页接口
    def test_technical_disclosure_scheme_approval_detail(self):
        '''测试技术交底与方案审批详情页接口'''  # 此注释将展示到测试报告的测试组类
        detailID =70
        t = technicalDisclosureSchemeView()
        t.technical_disclosure_scheme_approval_approval_detail(detailID)

if __name__ == '__main__':
    l = TechnicalDisclosureScheme()
    l.test_technical_disclosure_scheme_list()
    l.test_technical_disclosure_scheme_add()
    l.test_technical_disclosure_scheme_approval()
    l.test_technical_disclosure_scheme_approval_detail()
