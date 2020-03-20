from base.base import base_url,session_headers
import requests,json
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

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('合同签订申请列表请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 添加技术交底方案
    def contract_sign_apply_record_add(self):
        url = base_url + '/contract_sign_apply_record/add'

        form_data = {
            'contract_id': 78,
            'building_id':'',
            'apply_code': 'SQ030700001',
            'b_name': '乙方',
            'workload': '50天',
            'cost_price': '600000000',
            'plan_time': '2020-03-17',
            'project_address': '福建省厦门市集美区软件园三期',
            'construction_scope': '软件园所有的绿化带',
            'description': '翻种草坪',
            'case_description': '所有的草坪必须替换最新品种的草',
            'labour_contract_id':''
        }
        try:
            res = requests.post(url,
                                headers=session_headers,
                                data=form_data
                                )
            logging.info('添加合同签订申请成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
if __name__ == '__main__':
    l = ContractSignApplyRecordView()
    l.contract_sign_apply_record_index()
    l.contract_sign_apply_record_add()
