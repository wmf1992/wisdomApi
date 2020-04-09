from business.progress_plan import ProgressPlan
import unittest,logging,time
class TestProgressPlan(unittest.TestCase):
    def test_progress_plan_index(self):
        '''测试进度计划列表接口'''  # 此注释将展示到测试报告的测试组类
        M = ProgressPlan()
        M.progress_plan_index()
    def test_progress_plan_detail(self):
        '''测试进度计划详情接口'''  # 此注释将展示到测试报告的测试组类
        M = ProgressPlan()
        M.progress_plan_detail()

    def test_progress_plan_add(self):
        '''测试进度计划详情接口'''  # 此注释将展示到测试报告的测试组类
        M = ProgressPlan()
        
        form_data = {
            "plan_time": "2018-02",
            "contract_id": '41',
            "building_id": 9,
            "plan_list[0][building_floor]": "地基",
            "plan_list[0][first_sub_project_id]": 1,
            "plan_list[0][parent_sub_project_id]": 2,
            "plan_list[0][sub_project_id]": 6,
            "plan_list[0][quantities_count]": 20,
            "plan_list[0][quantities_unit]": "天",
            "plan_list[0][construction_norm_count]": 300,
            "plan_list[0][construction_norm_unit]": "元",
            "plan_list[0][plan_num]": 30,
            "plan_list[0][plan_start_time]": "2020-02-12 07:00:00",
            "plan_list[0][plan_end_time]": "2020-03-07 22:00:00",
            "plan_list[0][start_hour]": 7,
            "plan_list[0][end_hour]": 22,
            "plan_list[0][work_ahead]": 4,
            "plan_list[0][work_after]": 5,
            "plan_list[0][duration]": 24,
            "plan_list[0][durationTime]": 15,
            "plan_list[0][sub_name]": "分项工程2修改",
            "plan_list[0][plan_time_diff]": "24天15时",
            "technical_disclosure[0][technical_disclosure_name]": "交底1",
            "technical_disclosure[0][plan_disclosure_time]": "2020-02-13",
            "technical_disclosure[0][files][0][file_name]": "库存计算规则.xlsx",
            "technical_disclosure[0][files][0][file_ext]": "xlsx",
            "technical_disclosure[0][files][0][url]": "http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/916b6b203b77ce0026381cf014f864a1.xlsx",
            "test_user": 5

        }
        M.progress_plan_add(form_data)
    def test_progress_plan_testSave(self):
        '''测试进度计划详情接口'''  # 此注释将展示到测试报告的测试组类
        M = ProgressPlan()
        form_data = {
            "plan_id": 194,
            "test_info[0][test_name]": "打扫地板",
            "test_info[0][plan_test_time]": "2020-02-14"
        }
        M.progress_plan_add(form_data)




if __name__ == '__main__':
    T = TestProgressPlan()
    T.test_progress_plan_add()