'''
调拨
'''
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from base.base import base_url,session_headers,approval_session_headers,score_session_headers,inventory_manager_session_headers
from base.commonfun import Common
import threading
import requests,json,time
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class MeterialAllocated:
    def meterial_allocated_index(self):
        url = base_url + 'allocated/index?access_code=&warehouse_name=&to_warehouse_name=&access_start_time=&access_end_time=&create_start_time=&create_end_time=&initiator_username=&page=1&page_size=10'
        msgs = '调拨单'
        C = Common()
        method = 'get'
        resdata = C.get_exception(method, url, msgs, session_headers, form_data='')
        return resdata
    def meterial_getWarehouseMeterialInfo(self):
        # 固定取材料：法国牛排，id=13
        url = base_url + '/Meterial/getWarehouseMeterialInfo?warehouse_id=6&meterial_id=13'
        msgs = '仓库材料详情'
        C = Common()
        method = 'get'
        resdata = C.get_exception(method, url, msgs, session_headers, form_data='')
        return resdata


    def meterial_allocated_detail(self,access_id):
        url = base_url + '/allocated/detail?id=%d' %access_id
        msgs = '调拨单详情'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')
    def meterial_allocated_add(self,data):
        url = base_url + '/allocated/add'
        meterial_info = self.meterial_getWarehouseMeterialInfo()
        if meterial_info['data']['meterial_stock'] > 0:
            msgs = '提交成功'
        else:
            msgs = meterial_info['data']['meterial_name'] + '材料不足'
        C = Common()
        method = 'post'
        form_data = {
            'access_code': data[''],
            'access_time': data[''],
            'warehouse_id': data[''],
            'to_warehouse_id': data[''],
            'meterial_list': data['']
        }

        C.get_exception(method, url, msgs, inventory_manager_session_headers, form_data=form_data)
if __name__ == '__main__':
    M = MeterialAllocated()
    M.meterial_getWarehouseMeterialInfo()
    M.meterial_allocated_add()
    M.meterial_allocated_detail()

