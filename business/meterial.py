import json
from base.base import base_url,session_headers,inventory_manager_session_headers
import requests,json
from base.commonfun import Common
import logging
import logging.config
from requests import exceptions
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class MeterialView:
    # 材料列表
    def get_meterial(self):
        url = base_url + '/meterial/index?page=1&page_size=10&type_id='
        msgs = '材料管理'
        C = Common()
        method = 'get'
        resdata = C.get_exception(method, url, msgs, session_headers, form_data='')
        return resdata
    # 添加材料
    def meterial_add(self,data):
        url = base_url + '/meterial/add'

        form_data = {
            'image': data['image'],
            'meterial_code':data['meterial_code'],
            'meterial_name': data['meterial_name'],
            'type_name':data['type_name'],
            'type_id': data['type_id'],
            'meterial_spec': data['meterial_spec'],
            'meterial_unit': data['meterial_unit'],
            'warning_num':data['warning_num'],
            'parent_type_id': data['parent_type_id'],
            'second_type_id': data['second_type_id']
        }
        msgs = '提交成功'
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)

    # 新增材料审批详情页
    def get_meterial_approval(self,meterial_id):
        url = base_url + '/meterial_approval/detail?id=%d'%(meterial_id)
        msgs = '材料审批详'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')


    # 添加材料审批通过
    def meterial_approval_check(self,data):
        url = base_url + '/meterial_approval/check'
        form_data = {
            'id': data['id'],
            'meterial_code': data['meterial_code'],
            'meterial_name': data['meterial_name'],
            'parent_type_id': data['parent_type_id'],
            'second_type_id': data['second_type_id'],
            'type_id': data['type_id'],
            'meterial_spec': data['meterial_spec'],
            'meterial_unit': data['meterial_unit'],
            'image': data['image'],
            'warning_num': data['warning_num'],
            'is_need_approval': data['is_need_approval'],
            'edit_user': data['edit_user'],
            'create_time': data['create_time'],
            'status': data['status'],
            'type_text': data['type_text'],
            'status_text': data['status_text'],
            'edit_username': data['edit_username'],
            'is_approval_right': data['is_approval_right'],
            'files': data['files'],
            'images': data['images'],
            'approval_opinions': data['approval_opinions'],
            'check': data['check'],
            'meterial_id': data['meterial_id']
        }
        msgs = '操作成功'
        C = Common()
        method = 'post'
        # C.get_exception(method, url, msgs, session_headers, form_data=form_data)
        C.get_exception(method, url, msgs, inventory_manager_session_headers, form_data=form_data)


