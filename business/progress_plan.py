from base.base import base_url,session_headers
from base.commonfun import Common
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class ProgressPlan:
    def progress_plan_index(self):
        url = base_url + '/progress_plan/index?page=1&page_size=10&building_id=&labour_contract_id='
        msgs = '进度计划列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')
    def progress_plan_detail(self):
        url = base_url + '/progress_plan/detail?id=196'
        msgs = '进度计划详情'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')
    def progress_plan_add(self,data):
        url = base_url + '/progress_plan/add'
        form_data = {
            "plan_time": data['plan_time'],
            "contract_id": data['contract_id'],
            "building_id": data['building_id'],
            "plan_list[0][building_floor]": data['plan_list[0][building_floor]'],
            "plan_list[0][first_sub_project_id]": data['plan_list[0][first_sub_project_id]'],
            "plan_list[0][parent_sub_project_id]": data['plan_list[0][parent_sub_project_id]'],
            "plan_list[0][sub_project_id]": data['plan_list[0][sub_project_id]'],
            "plan_list[0][quantities_count]": data['plan_list[0][quantities_count]'],
            "plan_list[0][quantities_unit]": data['plan_list[0][quantities_unit]'],
            "plan_list[0][construction_norm_count]": data['plan_list[0][construction_norm_count]'],
            "plan_list[0][construction_norm_unit]": data['plan_list[0][construction_norm_unit]'],
            "plan_list[0][plan_num]": data['plan_list[0][plan_num]'],
            "plan_list[0][plan_start_time]": data['plan_list[0][plan_start_time]'],
            "plan_list[0][plan_end_time]": data['plan_list[0][plan_end_time]'],
            "plan_list[0][start_hour]": data['plan_list[0][start_hour]'],
            "plan_list[0][end_hour]": data['plan_list[0][end_hour]'],
            "plan_list[0][work_ahead]": data['plan_list[0][work_ahead]'],
            "plan_list[0][work_after]": data['plan_list[0][work_after]'],
            "plan_list[0][duration]": data['plan_list[0][duration]'],
            "plan_list[0][durationTime]": data['plan_list[0][durationTime]'],
            "plan_list[0][sub_name]": data['plan_list[0][sub_name]'],
            "plan_list[0][plan_time_diff]": data['plan_list[0][plan_time_diff]'],
            "technical_disclosure[0][technical_disclosure_name]": data['technical_disclosure[0][technical_disclosure_name]'],
            "technical_disclosure[0][plan_disclosure_time]": data['technical_disclosure[0][plan_disclosure_time]'],
            "technical_disclosure[0][files][0][file_name]": data['technical_disclosure[0][files][0][file_name]'],
            "technical_disclosure[0][files][0][file_ext]": data['technical_disclosure[0][files][0][file_ext]'],
            "technical_disclosure[0][files][0][url]": data['technical_disclosure[0][files][0][url]'],
            "test_user": data['test_user']

        }

        msgs = '提交成功'
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)
    def progress_plan_testSave(self):
        # 2、试验员录入数据
        url = base_url + '/progress_plan/testSave'
        msgs = '提交成功'
        session_headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'access-token': '2ff7MQ0GpGN/EowbjrlQoxhtMIJf+08tpCi73eE6QNbHakgEuIxTpLbgy5zDe7PK1brCJA',
        }
        form_data = {
            "plan_id": 194,
            "test_info[0][test_name]": "打扫地板",
            "test_info[0][plan_test_time]": "2020-02-14"
        }
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)

