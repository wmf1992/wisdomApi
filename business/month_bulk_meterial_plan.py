'''
月大宗材料计划
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from base.base import base_url,session_headers,approval_session_headers,score_session_headers
from base.commonfun import Common
import threading
import requests,json,time
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class MonthBulkMeterialPlan:
    def month_bulk_meterial_plan_index(self):
        url = base_url + '/month_bulk_meterial_plan/index'
        msgs = '月大宗材料计划列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')
    def month_bulk_meterial_plan_detail(self):
        url = base_url + '/month_bulk_meterial_plan_approval/flowed?plan_id=10'
        msgs = '月大宗材料计划详情'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    def month_bulk_meterial_plan_add(self):
        url = base_url + '/month_bulk_meterial_plan/add'
        msgs = '提交成功'
        C = Common()
        method = 'post'
        form_data = {
            "contract_id": 41,
            "building_id": 9,
            "plan_time": '2020-12',
            "meterial_list": '[{"meterial_code":"CL12050005","meterial_name":"法国牛排","parent_type_id":6,"second_type_id":8,"type_id":112,"meterial_spec":"500g","meterial_unit":"盒","image":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/e60795e82fd44d539ebb15c1bef823c2.jpg","is_need_approval":1,"type_text":"复合材料三级","meterial_id":13,"desc":"","plan_num":2,"enter_time":"2020-02-11"}]'

        }

        C.get_exception(method, url, msgs, session_headers, form_data=form_data)
    def month_bulk_meterial_plan_approval(self):
        url = base_url + '/month_bulk_meterial_plan_approval/check'
        msgs = '提交成功'
        C = Common()
        method = 'post'
        form_data = {
            "plan_id": 105,
            "approval_opinions": "无意见",
            "check": 1,
            "back": "",
            "score": 1,
            "images": "",
            "files": ""
        }
        for session_header in approval_session_headers:
            C.get_exception(method, url, msgs, session_header, form_data=form_data)
            time.sleep(3)