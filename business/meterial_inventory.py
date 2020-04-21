'''
盘点
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
class MeterialInventory:
    def meterial_inventory_index(self):
        url = base_url + '/inventory/index?page=1&page_size=10'
        msgs = '盘点单'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')
    def meterial_inventory_detail(self,access_id):
        url = base_url + '/inventory/detail?id=%d' %access_id
        msgs = '盘点单详情'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')
    def meterial_inventory_add(self,data):
        url = base_url + '/inventory/add'
        msgs = '提交成功'
        C = Common()
        method = 'post'
        form_data = {
            "access_code": data['access_code'],
            "access_time": data['access_time'],
            "warehouse_id": data['warehouse_id'],
            "meterial_list[0][id]": data['meterial_list[0][id]'],
            "meterial_list[0][meterial_code]": data['meterial_list[0][meterial_code]'],
            "meterial_list[0][meterial_name]": data['meterial_list[0][meterial_name]'],
            "meterial_list[0][parent_type_id]": data['meterial_list[0][parent_type_id]'],
            "meterial_list[0][second_type_id]": data['meterial_list[0][second_type_id]'],
            "meterial_list[0][type_id]": data['meterial_list[0][type_id]'],
            "meterial_list[0][meterial_spec]": data['meterial_list[0][meterial_spec]'],
            "meterial_list[0][meterial_unit]": data['meterial_list[0][meterial_unit]'],
            "meterial_list[0][image]": data['meterial_list[0][image]'],
            "meterial_list[0][is_need_approval]": data['meterial_list[0][is_need_approval]'],
            "meterial_list[0][type_text]": data['meterial_list[0][type_text]'],
            "meterial_list[0][meterial_id]": data['meterial_list[0][meterial_id]'],
            "meterial_list[0][meterial_total_stock]": data['meterial_list[0][meterial_total_stock]'],
            "meterial_list[0][stock_num]": data['meterial_list[0][stock_num]'],
            "meterial_list[0][diff_num]": data['meterial_list[0][diff_num]'],
            "meterial_list[0][desc]": data['meterial_list[0][desc]'],
            "meterial_list[0][num]": data['meterial_list[0][num]'],
            "meterial_list[0][product_time]": data['meterial_list[0][product_time]'],
            "meterial_list[0][expire_time]": data['meterial_list[0][expire_time]'],
            "meterial_list[0][unit_price]": data['meterial_list[0][unit_price]']
        }

        C.get_exception(method, url, msgs, session_headers, form_data=form_data)

    def inventory_approval_check(self,data):
        url = base_url + '/inventory_approval/check'
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

