from base.base import base_url,session_headers
import requests,json
import  unittest
import logging
from requests import exceptions
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
            res.raise_for_status()  # 状态不是200会抛异常
        except exceptions.Timeout as e:  # 超时异常
            logging.info(e)
            self.assertEqual(200, res.status_code)  # 这个断言不能放在上面，如果放在前面断言(try里面)，考虑到返回状态200，也有可能是fail的用例
        except exceptions.HTTPError as e:  # 状态500 进入该异常
            logging.info(e)
            self.assertEqual(200, res.status_code)  # 这个断言不能放在上面，如果放在前面断言(try里面)，考虑到返回状态200，也有可能是fail的用例
        else:
            msg = res.json()
            logging.info(msg['msg'])
            self.assertEqual(200, res.status_code)
            self.assertIn('提交成功', msg['msg'])
            logging.info('技术交底方案列表请求成功')
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

            res.raise_for_status()  # 状态不是200会抛异常
        except exceptions.Timeout as e:  # 超时异常
            logging.info(e)
            self.assertEqual(200, res.status_code)  # 这个断言不能放在上面，如果放在前面断言(try里面)，考虑到返回状态200，也有可能是fail的用例
        except exceptions.HTTPError as e:  # 状态500 进入该异常
            logging.info(e)
            self.assertEqual(200, res.status_code)  # 这个断言不能放在上面，如果放在前面断言(try里面)，考虑到返回状态200，也有可能是fail的用例
            logging.info('添加技术交底与方案失败')
        else:

            msg=res.json()
            logging.info(msg['msg'])
            self.assertEqual(200, res.status_code)
            self.assertIn('提交成功',msg['msg'])
            logging.info('添加技术交底方案成功')
    #技术交底与方案待审核搜索列表
    def technical_disclosure_scheme_approval(self):
        url = base_url + '/technical_disclosure_scheme_approval/index?approval_type=1&sub_project_id[]=1&sub_project_id[]=2&sub_project_id[]=6'

        form_data = {
            'approval_type': 1,
            'sub_project_id[]': 1,
            'sub_project_id[]': 2,
            'sub_project_id[]': 6,
            'plan_code': 'RJYGY-JSJDFA-15-00015',
            'contract_name': '软件园公寓',
            'building_num': '软三b区',
            'plan_start_time': '2020-03-06',
            'plan_end_time': '2020-03-28',
            'plan_type':'',
            'edit_username': '总经理张三0',
            'status':'',
            'create_start_time': '2020-02-24',
            'create_end_time': '2020-04-04',
            'page': 1,
            'page_size': 10,

        }

        try:
            res = requests.get(url,
                                headers=session_headers,
                                # data=form_data
                                )

            res.raise_for_status()   #状态不是200会抛异常
        except exceptions.Timeout as e:  # 超时异常
            logging.info(e)
            self.assertEqual(200,res.status_code)    #这个断言不能放在上面，如果放在前面断言(try里面)，考虑到返回状态200，也有可能是fail的用例
        except exceptions.HTTPError as e:    #状态500 进入该异常
            logging.info(e)
            self.assertEqual(200, res.status_code)   #这个断言不能放在上面，如果放在前面断言(try里面)，考虑到返回状态200，也有可能是fail的用例
        else:
            msg=res.json()
            logging.info(msg['msg'])
            self.assertEqual(200, res.status_code)
            self.assertIn('技术交底与方案审批列表',msg['msg'])
            logging.info('技术交底与方案待审核列表查询成功')








if __name__ == '__main__':
    l = technicalDisclosureSchemeView()
    # l.technical_disclosure_scheme()
    # l.technical_disclosure_scheme_add()
    l.technical_disclosure_scheme_approval()
