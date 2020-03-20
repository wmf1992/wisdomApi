from base.base import base_url,session_headers
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class technicalDisclosureSchemeView:
    # 技术交底方案列表
    def technical_disclosure_scheme(self):
        url = base_url + '/technical_disclosure_scheme/index?sub_project_id=&page=1&page_size=10'

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('技术交底方案列表请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 添加技术交底方案
    def technical_disclosure_scheme_add(self):
        url = base_url + '/technical_disclosure_scheme/add'

        form_data = {
            'sub_project_id': 6,
            'contract_id': 4,
            'building_id': 15,
            'plan_time': '2020-03-16',
            'type': 1,
            'modify_ids':'' ,
            'description': 'description00',
            'page_num': 1,
            'files': '[{"file_name":"q.doc","file_ext":"doc","width":0,"height":0,"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/b1c1e9d22380c8c74502a3e1d68def4f.doc"}]',
            'labour_contract_id': ''
        }
        try:
            res = requests.post(url,
                                headers=session_headers,
                                data=form_data
                                )
            logging.info('添加技术交底方案成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
if __name__ == '__main__':
    l = technicalDisclosureSchemeView()
    l.technical_disclosure_scheme()
    l.technical_disclosure_scheme_add()
