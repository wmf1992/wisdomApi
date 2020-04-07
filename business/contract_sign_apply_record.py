from base.base import base_url,session_headers
import requests,json
from base.commonfun import Common
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
# 合同签订申请
class ContractSignApplyRecordView:
    # 合同签订申请列表
    def contract_sign_apply_record_index(self):
        url = base_url + '/contract_sign_apply_record/index?page=1&page_size=10'
        msgs = '合同签订申请列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    # 添加合同签订申请
    def contract_sign_apply_record_add(self,data):
        url = base_url + '/contract_sign_apply_record/add'

        form_data = {
            'contract_id': data['contract_id'],
            'building_id':data['building_id'],
            'apply_code': data['apply_code'],
            'b_name': data['b_name'],
            'workload': data['workload'],
            'cost_price': data['cost_price'],
            'plan_time': data['plan_time'],
            'project_address': data['project_address'],
            'construction_scope': data['construction_scope'],
            'description': data['description'],
            'case_description': data['case_description'],
            'labour_contract_id':data['labour_contract_id']
        }
        msgs = '提交成功'
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)

if __name__ == '__main__':
    l = ContractSignApplyRecordView()
    l.contract_sign_apply_record_index()
    l.contract_sign_apply_record_add()
