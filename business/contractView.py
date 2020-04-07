from base.base import base_url,session_headers
import requests,json
from base.commonfun import Common
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class ContractView:
    # 请求合同列表信息
    def contracts(self):
        url = base_url + '/contract/index?page=1&page_size=10'
        msgs = '合同列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    # 合同查阅记录请求
    def contract_apply_record(self):
        url = base_url + '/contract_apply_record/index?page=1'
        msgs = '获取成功'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')


    # 添加劳务合同
    def labourContract_add(self,data):
        url = base_url + '/contract/add'

        form_data = {
                'files[0][url]': data['files[0][url]'],
                'files[0][file_name]': data['files[0][file_name]'],
                'files[0][file_ext]': data['files[0][file_ext]'],
                'files[0][width]': data['files[0][width]'],
                'files[0][height]': data['files[0][height]'],
                'files[1][url]': data['files[1][url]'],
                'files[1][file_name]': data['files[1][file_name]'],
                'files[1][file_ext]': data['files[1][file_ext]'],
                'files[1][width]': data['files[1][width]'],
                'files[1][height]': data['files[1][height]'],

            'apply[0][id]': data['apply[0][id]'],
                'apply[1][id]': data['apply[1][id]'],
                'apply[2][id]': data['apply[2][id]'],
                'apply[3][id]': data['apply[3][id]'],
                'apply[4][id]': data['apply[4][id]'],
                'contract_type': data['contract_type'],

                'contract_id': data['contract_id'],
                'contract_name': data['contract_name'],
                'signing_time': data['signing_time'],
                'start_time': data['start_time'],
                'end_time': data['end_time'],
                'contract_money': data['contract_money'],
                'bond_money': data['bond_money'],
                'labour_services_company': data['labour_services_company'],
                'project_side': data['project_side'],
                'compliant': data['compliant'],
                'project_manager': data['project_manager'],
                'desc': data['desc']

            }
        msgs = '添加成功'
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)


    # 添加招标合同
    def contract_add(self,data):
        url = base_url + '/contract/add'

        form_data = {
            'files[0][url]': data['files[0][url]'],
            'files[0][file_name]': data['files[0][file_name]'],
            'files[0][file_ext]': data['files[0][file_ext]'],
            'files[0][width]': data['files[0][width]'],
            'files[0][height]': data['files[0][height]'],
            'apply[0][id]': data['apply[0][id]'],
            'apply[1][id]': data['apply[1][id]'],
            'apply[2][id]': data['apply[2][id]'],
            'apply[3][id]': data['apply[3][id]'],
            'apply[4][id]': data['apply[4][id]'],
            'contract_type': data['contract_type'],
            'contract_name': data['contract_name'],
            'signing_time': data['signing_time'],
            'start_time': data['start_time'],
            'end_time': data['end_time'],
            'contract_money': data['contract_money'],
            'bond_money': data['bond_money'],
            'project_side': data['project_side'],
            'compliant': data['compliant'],
            'project_manager': data['project_manager'],
            'desc': data['desc']

        }
        msgs = '添加成功'
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)

if __name__ == '__main__':
    l = ContractView()
    # l.contracts()
    # l.contract_apply_record()
    # l.contract_add()
    form_data = {
        'files[0][url]': 'http: // wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com / file / b1c1e9d22380c8c74502a3e1d68def4f.doc',
        'files[0][file_name]': 'q.doc',
        'files[0][file_ext]': 'doc',
        'files[0][width]': 0,
        'files[0][height]': 0,
        'apply[0][id]': 3,
        'apply[1][id]': 4,
        'apply[2][id]': 5,
        'apply[3][id]': 69,
        'apply[4][id]': 73,
        'contract_type': 1,
        'contract_name': '招标合同0316002',
        'signing_time': '2020-03-16',
        'start_time': '2020-04-01',
        'end_time': '2023-05-06',
        'contract_money': 50000000,
        'bond_money': 20000,
        'project_side': '项目方01',
        'compliant': '履约委托人01',
        'project_manager': 4,
        'desc': 'description0001'

    }
    l.contract_add(form_data)
