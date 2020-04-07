import json
from base.base import base_url,session_headers,inventory_manager_session_headers
import requests,json
from base.commonfun import Common
import logging
import logging.config
import unittest,time
from BSTestRunner import BSTestRunner
from requests import exceptions
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class MeterialView(unittest.TestCase):
    # 材料列表
    def get_meterial(self):
        url = base_url + '/meterial/index?page=1&page_size=10&type_id='
        meterial_id = 0

        try:
            res = requests.get(url, headers=session_headers)
            res.raise_for_status()  # 状态不是200会抛异常
        except exceptions.Timeout as e:  # 超时异常
            logging.info(e)
        # self.assertEqual(200, res.status_code)  # 超时不能使用该断言，否则会报错，因为没有得到res
            self.assertEqual(0,1)
        except exceptions.HTTPError as e:  # 状态500 进入该异常
            logging.info(e)
            self.assertEqual(200, res.status_code)  # 这个断言不能放在上面，如果放在前面断言(try里面)，考虑到返回状态200，也有可能是fail的用例

        else:
            msg = res.json()
            logging.info('请求状态码：%d ' % res.status_code + url + ' : ' + msg['msg'])
            self.assertEqual(200, res.status_code)
            self.assertIn('材料管理', msg['msg'])
            resdata = res.json()
            # print(resdata['data']['item'][0]['meterial_name'])
            # 返回最新一条的材料id
            meterial_id = resdata['data']['item'][0]['id']
        return meterial_id
        '''
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('材料列表请求成功')
            resdata = res.json()
            # print(resdata['data']['item'][0]['meterial_name'])
            # 返回最新一条的材料id
            meterial_id = resdata['data']['item'][0]['id']
            return meterial_id
            # 下面的方法也可以
            # data = json.loads(res.content)
            # print(data['data']['item'][0]['id'])

        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            return meterial_id
        '''
    # 添加材料
    def meterial_add(self,data):
        url = base_url + '/meterial/add'

        form_data = {
            'image': data['image'],
            'meterial_code':data['meterial_code'],
            'meterial_name': data['meterial_name'],
            'type_name':data['type_name'],
            'type_id': data['type_id'],
            'meterial_spec': data['meterial_spec'],
            'meterial_unit': data['meterial_unit'],
            'warning_num':data['warning_num'],
            'parent_type_id': data['parent_type_id'],
            'second_type_id': data['second_type_id']
        }
        msgs = '提交成功'
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)

    # 新增材料审批详情页
    def get_meterial_approval(self):
        meterial_id = self.get_meterial()
        print(meterial_id)
        if meterial_id > 0:
            url = base_url + '/meterial_approval/detail?id=%d'%(meterial_id)
            msgs = '材料审批详'
            C = Common()
            method = 'get'
            C.get_exception(method, url, msgs, session_headers, form_data='')

        else:
            pass

    # 添加材料审批通过
    def meterial_approval_check(self,data):
        meterial_id = self.get_meterial()
        if meterial_id > 0:
            url = base_url + '/meterial_approval/check'
            form_data = {
                id: meterial_id,
                'meterial_code': data['meterial_code'],
                'meterial_name': data['meterial_name'],
                'parent_type_id': data['parent_type_id'],
                'second_type_id': data['second_type_id'],
                'type_id': data['type_id'],
                'meterial_spec': data['meterial_spec'],
                'meterial_unit': data['meterial_unit'],
                'image': data['image'],
                'warning_num': data['warning_num'],
                'is_need_approval': data['is_need_approval'],
                'edit_user': data['edit_user'],
                'create_time': data['create_time'],
                'status': data['status'],
                'type_text': data['type_text'],
                'status_text': data['status_text'],
                'edit_username': data['edit_username'],
                'is_approval_right': data['is_approval_right'],
                'files': data['files'],
                'images': data['images'],
                'approval_opinions': data['approval_opinions'],
                'check': data['check'],
                'meterial_id': meterial_id
            }
            msgs = '操作成功'
            C = Common()
            method = 'post'
            C.get_exception(method, url, msgs, inventory_manager_session_headers, form_data=form_data)
        else:
            pass
if __name__ == '__main__':
    report_dir = '../reports'
    # 未按顺序执行测试用例
    # discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')
    # 测试套件，定义测试用例执行顺序
    suite = unittest.TestSuite()
    suite.addTest(MeterialView("test_meterial_add"))
    runner = unittest.TextTestRunner()

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_name = report_dir + '/' + now + ' test_report.html'

    with open(report_name, 'wb') as f:
        runner = BSTestRunner(stream=f, title='ShortVideo Test Report',
                              description='ShortVideo Android app test report')
        logging.info('start run test case...')
        # runner.run(discover)

        runner.run(suite)