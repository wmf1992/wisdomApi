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
import urllib3
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
        url = "https://www.taobappo.com"
        try:
            res = requests.get(url,
                               headers=session_headers
                               )
            res.raise_for_status()  # 状态不是200会抛异常
        except exceptions.Timeout as e:  # 超时异常
            logging.info(e)
            # self.assertEqual(200, res.status_code)  # 超时不能使用该断言，否则会报错，因为没有得到res
            self.assertEqual(0, 1)
        except exceptions.HTTPError as e:  # 状态500 进入该异常
            logging.info(e)
            self.assertEqual(200, res.status_code)  # 这个断言不能放在上面，如果放在前面断言(try里面)，考虑到返回状态200，也有可能是fail的用例

        else:
            msg = res.json()
            logging.info('请求状态码：%d ' % res.status_code + url + ' : ' + msg['msg'])
            self.assertEqual(200, res.status_code)
            # self.assertIn(msgs, msg['msg'])
        # try:
        #     res = requests.get(url,
        #                        headers=session_headers
        #                         )
        # except Exception as e:
        #     # logging.info("post请求出现了异525常：{0}".format(e))
        #     # self.assertFalse(0)
        #
        #     logging.info('淘宝请求有问题')
        #     self.assertEqual(200, res.status_code)
        # else:
        #
        #     logging.info('淘宝请求成功')
        #     self.assertEqual(200, res.status_code)
        #     return 99

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
    # t = TestTaobao()
    # dat=t.test_taobao()
    t = time.time()
    print(int(t))
    # t.test_baidu_timeout()
