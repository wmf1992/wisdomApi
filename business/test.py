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
from requests import exceptions
import logging
import logging.config
import unittest,time,logging
from base.base import session_headers
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
#4.编写测试用例和断言
class TestTaobao(unittest.TestCase):
    '''测试淘宝接口'''       # 此注释将展示到测试报告的测试组类
    def test_taobao(self):
        '''查询淘宝首页'''         # 此注释将展示到测试报告的用例标题
        url = "https://www.taobao.com"
        #
        #
        # r = requests.get(url)
        # print(r.status_code)     # 获取返回的结果
        # # result = r.json()['code'] #获取状态码
        # # print(result)
        # # 断言
        # self.assertEqual(200, r.status_code)
        # self.assertIn('msg', r.text)
        # self.assertTrue('淘宝'in r.text)
        try:
            res = requests.get(url,
                               headers=session_headers
                                )
        except Exception as e:
            # logging.info("post请求出现了异525常：{0}".format(e))
            # self.assertFalse(0)

            logging.info('淘宝请求有问题')
            self.assertEqual(200, res.status_code)
        else:
            print(44)
            logging.info('淘宝请求成功')
            self.assertEqual(200, res.status_code)

    def test_baidu(self):
        '''查询百度首页'''  # 此注释将展示到测试报告的用例标题
        url = "https://www.baidu.com"

        try:
            res = requests.get(url,timeout=0.1,
                               headers=session_headers
                                )
        except Exception as e:
            # logging.info("post请求出现了异525常：{0}".format(e))
            # self.assertFalse(0)
            logging.info('百度请求报错')
            self.assertEqual(200, res.status_code)
        else:
            logging.info('百度请求成功')
            self.assertEqual(200, res.status_code)

    def test_baidu_timeout(self):
        try:
            response = requests.get("https://www.baidu.com", timeout=0.0001, auth=('username', 'password'))
        except exceptions.Timeout as e:
            logging.info(32323)
            print(str(e))
        else:
            logging.info(120000000)
            print(response.text)


if __name__ == '__main__':
    t = TestTaobao()
    t.test_baidu_timeout()
