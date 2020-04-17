from business.quality_check import QualityCheck
from mysqlDb.quality_check_db import QualityCheckDb
import unittest,logging,time
from mysqlDb.progress_plan_db import ProgressPlanDb
class TestQualityCheck(unittest.TestCase):
    def test_quality_check_db(self):
        Q = QualityCheckDb()
        check_id = Q.quality_check_list(0)
        return check_id
    def test_quality_check_detail(self):
        Q = QualityCheck()
        check_id = self.test_quality_check_db()
        Q.quality_check_detail(check_id)
    def test_quality_check_add(self):
        '''测试添加质量检查接口'''  # 此注释将展示到测试报告的测试组类
        Q = QualityCheck()
        form_data = {
            "sub_project_id": 6,
            "tender_contract_id": 78,
            "building_id": 17,
            "check_time": "2020-02-12",
            "labour_score": 93,
            "owner_score": 90,
            "lack_num": 0,
            "deal_num": 0,
            "undeal_num": 0,
            "modify_ids": "82,79",
            "check_desc": "无",
            "check_file": '[{"file_name":"组织架构导入成员下载模板.xlsx","file_ext":"xlsx","width":0,"height":0,"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/fb341e023efbc28b149a86b5935e8675.xlsx"}]',
            "labour_file": '[{"file_name":"库存计算规则.xlsx","file_ext":"xlsx","width":0,"height":0,"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/916b6b203b77ce0026381cf014f864a1.xlsx"}]',
            "owner_file": '[{"file_name":"组织架构导入成员下载模板.xlsx","file_ext":"xlsx","width":0,"height":0,"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/fb341e023efbc28b149a86b5935e8675.xlsx"}]',
            "labour_contract_id": "",
            "goodness_score": 97

        }

        Q.quality_check_add(form_data)

    def test_quality_check_index(self):
        '''测试质量检查列表接口'''  # 此注释将展示到测试报告的测试组类
        from_data = {
            'sub_project_id': 6,
            'check_start_time': '2020-02-02',
            'status': 1,
            'check_code': 'ZBHTHT',
            'contract_name': '招标合同',
            'start_time': '2020-01-03',
            'building_num': '1',
            'edit_user': '三',
            'page': 1,
            'page_size': 10
        }
        pinUlr = '?'
        for key, value in from_data.items():
            pinUlr = pinUlr + '%s' % key + '=' + '%s' % value + '&'
        Q = QualityCheck()
        Q.quality_check_index(pinUlr)
    def test_quality_check_approval(self):
        quality_check_id = self.test_quality_check_db()

        Q = QualityCheck()
        form_data = {
            "quality_check_id": quality_check_id,
            "approval_opinions": "无意见",
            "check": 1,
            "back": "",
            "score": 1,

        }
        form_data_score = {
            "files": [],
            "reback_file": [{
            "url": "http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/916b6b203b77ce0026381cf014f864a1.xlsx",
            "file_name": "库存计算规则.xlsx", "file_ext": "xlsx", "width": 0, "height": 0, "type": 1}],
            "images": [],
            "reback_score": 99,
            "new_lack_num": 1,
            "total_undeal_num": 2,
            "reback_check_desc": "无",
            "score": 2,
            "reback_modify_ids": "82,79",
            "quality_check_reback": 1,
            "check": 1,
            "goodness_score": 90,
            "quality_check_id": quality_check_id
        }
        Q.quality_check_approval(form_data,form_data_score)
if __name__ == '__main__':
    T=TestQualityCheck()
    # T.test_quality_check_add()
    # T.test_quality_check_approval()
    # T.test_quality_check_index()
    T.test_quality_check_detail()