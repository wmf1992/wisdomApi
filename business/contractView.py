from base.base import base_url,session_headers
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class contractView:
    # 请求合同列表信息
    def contracts(self):
        url = base_url + '/contract/index?page=1&page_size=10'

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('合同列表请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 合同查阅记录请求
    def contract_apply_record(self):
        url = base_url + '/contract_apply_record/index?page=1'

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('合同查阅记录请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 添加劳务合同
    def labourContract_add(self):
        url = base_url + '/contract/add'

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
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
            'contract_type': 2,

            'contract_id': 254,
            'contract_name': '劳务合同0316001',
            'signing_time': '2020-03-16',
            'start_time': '2020-04-01',
            'end_time': '2023-05-06',
            'contract_money': 50000000,
            'bond_money': 20000,
            'labour_services_company': 6,
            'project_side': '项目方01',
            'compliant': '履约委托人01',
            'project_manager': 4,
            'desc': 'description0001'

        }
        try:
            res = requests.post(url,
                                headers = session_headers,
                                data = form_data
                                )
            logging.info('劳务合同添加成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)

    # 添加招标合同
    def contract_add(self):
        url = base_url + '/contract/add'

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
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
        try:
            res = requests.post(url,
                                headers=session_headers,
                                data=form_data
                                )
            logging.info('招标合同添加成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)

if __name__ == '__main__':
    l = contractView()
    l.contracts()
    l.contract_apply_record()
    # l.contract_add()

    l.labourContract_add()
