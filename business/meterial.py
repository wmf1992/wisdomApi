import json
from base.base import base_url,session_headers,inventory_manager_session_headers
import requests,json
import logging
import logging.config
import unittest,time
from BSTestRunner import BSTestRunner
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class MeterialView(unittest.TestCase):
    # 材料列表
    def get_meterial(self):
        url = base_url + '/meterial/index?page=1&page_size=10&type_id='
        meterial_id = 0
        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
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

    # 添加材料
    def test_meterial_add(self):
        url = base_url + '/meterial/add'

        form_data = {
            'image': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/a9f15e98bff56309f3bb31739420e1df.jpg',
            'meterial_code':'',
            'meterial_name': 'huanghua菜',
            'type_name':'',
            'type_id': 127,
            'meterial_spec': 500,
            'meterial_unit': 'g',
            'warning_num':'',
            'parent_type_id': 6,
            'second_type_id': 8
        }
        try:
            res = requests.post(url,
                                headers=session_headers,
                                data=form_data
                                )

            # if res.status_code == 200:
            #     # self.assertEqual(1)
            #     logging.info('添加材料成功')
            #     return True
            #     # self.assertTrue(res.status_code,200)
            # else:
            #
            #     # self.assertTrue(res.status_code,200)
            #     # raise Exception("Invalid level!")
            #     logging.info('添加材料失败，status_code：%d'%(res.status_code))
            #     return False
        except Exception as e:
            # logging.info("post请求出现了异525常：{0}".format(e))
            # self.assertFalse(0)
            logging.info(res.status_code)
        else:
            logging.info(res.status_code)
            self.assertEqual(200, res.status_code)

    # 新增材料审批详情页
    def get_meterial_approval(self):
        meterial_id = self.get_meterial()
        print(meterial_id)
        if meterial_id > 0:
            url = base_url + '/meterial_approval/detail?id=%d'%(meterial_id)
            try:
                res = requests.get(url, headers=session_headers)
                logging.info('新增材料审批详情页请求成功')

            except Exception as e:
                logging.info("post请求出现了异常：{0}".format(e))
        else:
            pass

    # 添加材料审批通过
    def meterial_approval_check(self):
        meterial_id = self.get_meterial()
        if meterial_id > 0:
            url = base_url + '/meterial_approval/check'
            form_data = {
                id: meterial_id,
                'meterial_code': 'CL031803',
                'meterial_name': '白菜',
                'parent_type_id': 6,
                'second_type_id': 8,
                'type_id': 127,
                'meterial_spec': 500,
                'meterial_unit': 'g',
                'image': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/a9f15e98bff56309f3bb31739420e1df.jpg',
                'warning_num': 20,
                'is_need_approval': 1,
                'edit_user': 3,
                'create_time': '2020-03-18',
                'status': 0,
                'type_text': '三级金属',
                'status_text': '审批中',
                'edit_username': '总经理张三01',
                'is_approval_right': 1,
                'files': '',
                'images': '',
                'approval_opinions': '无意见',
                'check': 1,
                'meterial_id': meterial_id
            }
            try:
                res = requests.post(url,
                                    headers=inventory_manager_session_headers,
                                    data=form_data
                                    )
                logging.info('添加材料审批通过')
                # print(res.json())
            except Exception as e:
                print("post请求出现了异常：{0}".format(e))
                logging.info(res.status_code)
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