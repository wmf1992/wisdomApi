'''
工程结算
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
class SubProject:

    def sub_project_index(self):
        url = base_url + '/project_settlement/index'
        msgs = '获取成功'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')
    def sub_project_detail(self,project_settlement_id):
        url = base_url + '/project_settlement/detail?id=%d' %project_settlement_id
        msgs = '合同详情'
        C = Common()
        method = 'get'
        res = C.get_exception(method, url, msgs, session_headers, form_data='')
        return res
    def sub_project_add(self,data):
        url = base_url + '/project_settlement/add'
        msgs = '提交成功'
        C = Common()
        method = 'post'
        form_data = {
            "start_time": data['start_time'],
            "end_time": data['end_time'],
            "contract_id": data['contract_id'],
            "labor_contract_id": data['labor_contract_id'],
            "building_id": data['building_id'],
            "sub_project_ids": data['sub_project_ids'],
            "compliant": data['compliant'],
            "project_side": data['project_side'],
            "pay_rate": data['pay_rate'],
            "labour_contract_id": data['labour_contract_id'],
            "settlement_list[0][construction_content]": data['settlement_list[0][construction_content]'],
            "settlement_list[0][quantities_count]": data['settlement_list[0][quantities_count]'],
            "settlement_list[0][quantities_unit]": data['settlement_list[0][quantities_unit]'],
            "settlement_list[0][unit_price]": data['settlement_list[0][unit_price]'],
            "settlement_list[0][desc]": data['settlement_list[0][desc]'],
        }

        C.get_exception(method, url, msgs, session_headers, form_data=form_data)

    def sub_project_check(self,data,data_info,checkCost_form_data,settingPayRate_form_data):
        url = base_url + '/project_settlement_approval/add'
        msgs = '提交成功'
        C = Common()
        method = 'post'
        form_data = {
            "project_settlement_id": data['project_settlement_id'],
            "approval_opinions": data['approval_opinions'],
            "check": data['check'],
            "back": data['back'],
            "score": data['score']

        }
        form_data_info = {
            "files": data_info['files'],
            "images": data_info['images'],
            "approval_opinions": data_info['approval_opinions'],
            "score": data_info['score'],
            "check": data_info['check'],
            "project_settlement_id": data_info['project_settlement_id']
        }
        # 不需要填写结算信息，批量执行审批操作
        for session_header in approval_session_headers:
            C.get_exception(method, url, msgs, session_header, form_data=form_data)
            time.sleep(3)
        # 需要填写结算信息---设置结算金额、数量
        checkCost_url = base_url + '/project_settlement_approval/checkCost'
        checkCost_form_data = {
            'approval_quantities_count': checkCost_form_data['approval_quantities_count'],
            'approval_unit_price': checkCost_form_data['approval_unit_price'],
            'id': checkCost_form_data['id']
        }
        C.get_exception(method, checkCost_url, '保存成功', score_session_headers, form_data=checkCost_form_data)
        # 需要填写结算信息---设置结算比例
        settingPayRate_url = base_url + '/project_settlement_approval/settingPayRate'
        settingPayRate_form_data= {
            'project_settlement_id': settingPayRate_form_data['project_settlement_id'],
            'approval_pay_rate': settingPayRate_form_data['approval_pay_rate']
        }
        C.get_exception(method, settingPayRate_url, '保存成功', score_session_headers, form_data=settingPayRate_form_data)

        # 需要填写结算信息，执行审批操作
        # C.get_exception(method, url, msgs, score_session_headers, form_data=form_data)
        # 批量执行审批操作
        # for session_header in score_session_headers:
        #     C.get_exception(method, url, msgs, session_header, form_data=form_data_info)
        #     time.sleep(3)

