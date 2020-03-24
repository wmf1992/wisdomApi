from base.base import base_url,session_headers
import requests,json
import  unittest
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class technicalDisclosureSchemeView(unittest.TestCase):
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
    def technical_disclosure_scheme_add(self,data):
        url = base_url + '/technical_disclosure_scheme/add'

        form_data = {
            'sub_project_id': data['sub_project_id'],
            'contract_id': data['contract_id'],
            'building_id': data['building_id'],
            'plan_time': data['plan_time'],
            'type': data['type'],
            'modify_ids':data['modify_ids'] ,
            'description': data['description'],
            'page_num': data['page_num'],
            'files': data['files'],
            'labour_contract_id': data['labour_contract_id']
        }
        try:
            res = requests.post(url,
                                headers=session_headers,
                                data=form_data
                                )

            # print(res.json())
        except :

            logging.info('添加技术交底与方案失败')
        else:

            msg=res.json()
            logging.info(msg['msg'])
            self.assertEqual(200, res.status_code)
            self.assertIn('提交成功',msg['msg'])
            logging.info('添加技术交底方案成功33')

if __name__ == '__main__':
    l = technicalDisclosureSchemeView()
    l.technical_disclosure_scheme()
    l.technical_disclosure_scheme_add()
