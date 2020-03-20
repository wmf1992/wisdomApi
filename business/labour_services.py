
from base.base import base_url,session_headers
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class LabourServicesView:
    # 劳务公司列表
    def get_labour_services(self):
        url = base_url + '/labour_services/index?page=1&page_size=10&company_name=&legal_person_name=&contacts=&contacts_mobile=&is_black=0'

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('劳务公司列表请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)

    # 劳务公司黑名单列表
    def get_labour_services_black(self):
        url = base_url + '/labour_services/index?page=1&page_size=10&company_name=&legal_person_name=&contacts=&contacts_mobile=&is_black=1'

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('劳务公司黑名单列表请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 添加劳务公司
    def labour_services_add(self):
        url = base_url + '/labour_services/add'

        form_data = {
            'company_name': '劳务公司031702',
            'legal_person_name': '法定代表人01',
            'province_code': 150000,
            'city_code': 150100,
            'area_code': 150123,
            'address': '软件园',
            'contacts': '联系人01',
            'contacts_mobile': '18859663158',
            'original_business_license_id': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/22543476a8a01a20ba789efcb9a1b688.png',
            'copy_business_license_id': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/268290ab1a0e45b6974e19b9b1e421d6.png',
            'opening_permit_id': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/49753df0d37fd44cc210839e52e9fb3c.png',
            'letter_of_attorney_id': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/753837ac685f2206390123ab453f2015.jpg',
            'front_legal_person_idcard_id': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/5875577bb3fb889c3622bbac8df0cdfa.jpg',
            'back_legal_person_idcard_id': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/ab28e193d0621a56fea166a64932a4ed.jpg',
            'sort': 2
        }
        try:
            res = requests.post(url,
                                headers=session_headers,
                                data=form_data
                                )
            logging.info('添加劳务公司成功')
            res.status_code
            res.text
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
if __name__ == '__main__':
    l = LabourServicesView()
    l.get_labour_services()
    l.get_labour_services_black()
    l.labour_services_add()
