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
    def month_bulk_meterial_plan_detail(self,plan_id):
        url = base_url + '/month_bulk_meterial_plan/detail?id=%d' %plan_id
        msgs = '月大宗材料计划详情'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    def month_bulk_meterial_plan_add(self,data):
        url = base_url + '/month_bulk_meterial_plan/add'
        msgs = '提交成功'
        C = Common()
        method = 'post'
        form_data = {
            "contract_id": data['contract_id'],
            "building_id": data['building_id'],
            "plan_time": data['plan_time'],
            "meterial_list": data['meterial_list']
        }

        C.get_exception(method, url, msgs, session_headers, form_data=form_data)
    def month_bulk_meterial_plan_approval(self,data):
        url = base_url + '/month_bulk_meterial_plan_approval/check'
        msgs = '操作成功'
        C = Common()
        method = 'post'
        form_data = {
            "plan_id": data['plan_id'],
            "approval_opinions": data['approval_opinions'],
            "check": data['check'],
            "back": data['back'],
            "score": data['score'],
            "images": data['images'],
            "files": data['files']
        }
        for session_header in approval_session_headers:
            C.get_exception(method, url, msgs, session_header, form_data=form_data)
            time.sleep(3)