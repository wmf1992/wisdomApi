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
            res = requests.get(url,timeout =0.3, headers=session_headers)
            res.raise_for_status()  # 状态不是200会抛异常
        except exceptions.Timeout as e:  # 超时异常
            logging.info(e)
            # self.assertEqual(200, res.status_code)  # 超时不能使用该断言，否则代码会报错，因为超时了，没有得到res
        except exceptions.HTTPError as e:  # 状态500 进入该异常
            logging.info(e)
            self.assertEqual(200, res.status_code)  # 这个断言不能放在上面，如果放在前面断言(try里面)，考虑到返回状态200，也有可能是fail的用例
        else:
            msg = res.json()
            logging.info(msg['msg'])
            self.assertEqual(200, res.status_code)
            self.assertIn('技术交底与方案列表', msg['msg'])
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
                                timeout=0.1,
                                headers=session_headers,
                                data=form_data,

                                )

            res.raise_for_status()  # 状态不是200会抛异常
        except exceptions.Timeout as e:  # 超时异常
            logging.info(e)
            # self.assertEqual(200, res.status_code)  # 超时不能使用该断言，否则会报错，因为没有得到res
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
    def technical_disclosure_scheme_approval(self,data):
        # url = base_url + '/technical_disclosure_scheme_approval/index?approval_type=1&sub_project_id[]=1&sub_project_id[]=2&sub_project_id[]=6'
        url = base_url + '/technical_disclosure_scheme_approval/index'
        # logging.info(url)
        form_data = {
            'approval_type': data['approval_type'],

            'sub_project_id': data['sub_project_id'],
            'plan_code': data['plan_code'],
            'contract_name': data['contract_name'],
            'building_num': data['building_num'],
            'plan_start_time': data['plan_start_time'],
            'plan_end_time': data['plan_end_time'],
            'plan_type': data['plan_type'],
            'edit_username': data['edit_username'],
            'status': data['status'],
            'create_start_time': data['create_start_time'],
            'create_end_time': data['create_end_time'],
            'page': data['page'],
            'page_size': data['page_size'],

        }
        pinUlr = '?'
        for key, value in form_data.items():
            pinUlr = pinUlr + '%s' % key + '=' + '%s' % value + '&'
        url = url + pinUlr
        # print(url)

        try:
            res = requests.get(url,
                                timeout=0.1,
                                headers=session_headers,

                                )

            res.raise_for_status()   #状态不是200会抛异常
            # logging.info(res.json())

        except exceptions.Timeout as e:  # 超时异常
            logging.info(str(e))
            # self.assertEqual(200,res.status_code)    #超时不能用这句话进行断言
        except exceptions.HTTPError as e:    #状态500 进入该异常
            logging.info(e)
            self.assertEqual(200, res.status_code)   #这个断言不能放在上面，如果放在前面断言(try里面)，考虑到返回状态200，也有可能是fail的用例
        else:
            msg=res.json()
            logging.info(msg['msg'])
            self.assertEqual(200, res.status_code)
            self.assertIn('技术交底与方案审批列表',msg['msg'])
            logging.info('技术交底与方案待审核列表查询成功')

    # 技术交底与方案详情页
    def technical_disclosure_scheme_detail(self,detailId):
        url = base_url + '/technical_disclosure_scheme/detail?id=%d'%detailId
        try:
            res = requests.get(url,timeout =0.3,
                               headers=session_headers,
                               )

            res.raise_for_status()  # 状态不是200会抛异常
        except exceptions.Timeout as e:  # 超时异常
            logging.info(e)
            # self.assertEqual(200, res.status_code)  # 超时不能使用该断言，否则会报错，因为没有得到res
        except exceptions.HTTPError as e:  # 状态500 进入该异常
            logging.info(e)
            self.assertEqual(200, res.status_code)  # 这个断言不能放在上面，如果放在前面断言(try里面)，考虑到返回状态200，也有可能是fail的用例
        else:
            msg = res.json()
            logging.info(msg['msg'])
            self.assertEqual(200, res.status_code)
            self.assertIn('技术交底与方案详情', msg['msg'])
            logging.info('技术交底与方案详情查询成功')

    # 技术交底与方案待审批详情页
    def technical_disclosure_scheme_approval_approval_detail(self,detailId):
        url = base_url +'/technical_disclosure_scheme_approval/detail?id=%d'%detailId
        try:
            res = requests.get(url,timeout=0.3,
                               headers=session_headers,
                               )

            res.raise_for_status()  # 状态不是200会抛异常
        except exceptions.Timeout as e:  # 超时异常
            logging.info(e)
            # self.assertEqual(200, res.status_code)  # 超时不能使用该断言，否则会报错，因为没有得到res
        except exceptions.HTTPError as e:  # 状态500 进入该异常
            logging.info(e)
            self.assertEqual(200, res.status_code)  # 这个断言不能放在上面，如果放在前面断言(try里面)，考虑到返回状态200，也有可能是fail的用例
        else:
            msg = res.json()
            logging.info(msg['msg'])
            self.assertEqual(200, res.status_code)
            self.assertIn('技术交底与方案待审批详情', msg['msg'])
            logging.info('技术交底与方案待审批详情查询成功')






if __name__ == '__main__':
    l = technicalDisclosureSchemeView()
    # l.technical_disclosure_scheme()
    form_data = {

        'sub_project_id': 6,
        'contract_id': 4,
        'building_id': 15,
        'plan_time': '2020-03-24',
        # 'contract_id': 4,
        'type': 1,
        'modify_ids': '',
        'description': 'description00',
        'page_num': 1,
        'files': '[{"file_name":"q.doc","file_ext":"doc","width":0,"height":0,"url":"http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/file/b1c1e9d22380c8c74502a3e1d68def4f.doc"}]',
        'labour_contract_id': ''

    }
    l.technical_disclosure_scheme_add(form_data)
    data = {
        'approval_type': '',
        'sub_project_id': '',
        'plan_code': '',
        'contract_name': '软件园公寓',
        'building_num': '',
        'plan_start_time': '',
        'plan_end_time': '',
        'plan_type': '',
        'edit_username': '',
        'status': '',
        'create_start_time': '',
        'create_end_time': '',
        'page': '',
        'page_size': '',
    }
    pinUlr = '?'
    for key,value in data.items():
        pinUlr = pinUlr + '%s' %key + '=' +  '%s' %value + '&'
    url = 'http://wisdom_project.yxsoft.net/front/technical_disclosure_scheme/index' +pinUlr

    # l.technical_disclosure_scheme_approval(data)
