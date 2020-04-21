'''
材料出库
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
class MeterialOutbound:
    def meterial_outbound_index(self):
        url = base_url + '/outbound/index?page=1&page_size=10'
        msgs = '出库单'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')
    def meterial_outbound_detail(self,access_id):
        url = base_url + '/outbound/detail?id=%d' %access_id
        msgs = '出库单详情'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')
    def meterial_outbound_add(self,data):
        url = base_url + '/outbound/add'
        msgs = '提交成功'
        C = Common()
        method = 'post'
        form_data = {
            "plan_id": data['plan_id'],
            "access_code": data['access_code'],
            "access_time": data['access_time'],
            "warehouse_id": data['warehouse_id'],
            "building_id": data['building_id'],
            "meterial_list": data['meterial_list'],
            "images": data['images'],
            "files": data['files']

        }

        C.get_exception(method, url, msgs, session_headers, form_data=form_data)

    def outbound_approval_check(self,data):
        url = base_url + '/outbound_approval/check'
        msgs = '操作成功'
        C = Common()
        method = 'post'
        print(data['access_id'])
        form_data = {
            "access_id": data['access_id'],
            "approval_opinions": data['approval_opinions'],
            "check": data['check'],
            "back": data['back'],
            "score": data['score'],
            "images": data['images'],
            "files": data['files']

        }
        # 批量执行审批操作
        for session_header in approval_session_headers:
            C.get_exception(method, url, msgs, session_header, form_data=form_data)
            time.sleep(2)

