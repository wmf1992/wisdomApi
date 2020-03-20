# coding=utf-8
#1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

#2.注释：包括记录创建时间，创建人，项目名称。
'''
 6 Created on 2019-4-26
 7 @author: 北京-宏哥
 8 Project:学习和使用unittest框架编写断言-中篇
 9
'''
#3.导入requests和unittest模块
import requests
import unittest,time,logging
from BSTestRunner import BSTestRunner
#4.编写测试用例和断言
class TestTaobao(unittest.TestCase):
    '''测试淘宝接口'''       # 此注释将展示到测试报告的测试组类
    def test_taobao(self):
        '''查询淘宝首页'''         # 此注释将展示到测试报告的用例标题
        url = "https://www.taobao.com"


        r = requests.get(url)
        print(r.status_code)     # 获取返回的结果
        # result = r.json()['code'] #获取状态码
        # print(result)
        # 断言
        self.assertEqual(200, r.status_code)
        self.assertIn('msg', r.text)
        self.assertTrue('33淘宝'in r.text)


if __name__ == "__main__":
    report_dir = '../reports'

    # 未按顺序执行测试用例
    # discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

    # 测试套件，定义测试用例执行顺序
    suite = unittest.TestSuite()
    suite.addTest(TestTaobao("test_taobao"))
    runner = unittest.TextTestRunner()

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_name = report_dir + '/' + now + ' test_report.html'

    with open(report_name, 'wb') as f:
        runner = BSTestRunner(stream=f, title='ShortVideo Test Report',
                              description='ShortVideo Android app test report')
        logging.info('start run test case...')
        # runner.run(discover)

        runner.run(suite)