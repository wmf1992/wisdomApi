from business.technical_disclosure_scheme import technicalDisclosureSchemeView
import unittest,logging,time
class TechnicalDisclosureScheme(unittest.TestCase):
    '''测试技术交底接口'''  # 此注释将展示到测试报告的测试组类
    def test_left_menu(self):
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

if __name__ == '__main__':
    l = TechnicalDisclosureScheme()
    l.test_technical_disclosure_scheme()
    l.test_technical_disclosure_scheme_add()
