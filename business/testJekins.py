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
import pymysql
import unittest,time,logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
#4.编写测试用例和断言
class TestGit(unittest.TestCase):
    '''测试git接口'''       # 此注释将展示到测试报告的测试组类
    def test_git(self):
        '''查询git首页'''         # 此注释将展示到测试报告的用例标题
        url = "https://github.com/"


        r = requests.get(url)
        print(r.status_code)     # 获取返回的结果
        # result = r.json()['code'] #获取状态码
        # print(result)
        # 断言
        self.assertEqual(200, r.status_code)
        self.assertIn('msg', r.text)
        self.assertTrue('淘宝'in r.text)

    def test_baidu(self):
        '''查询百度首页'''  # 此注释将展示到测试报告的用例标题
        url = "https://www.baidu.com"

        r = requests.get(url)
        print(r.status_code)  # 获取返回的结果
        # result = r.json()['code'] #获取状态码
        # print(result)
        # 断言
        self.assertEqual(200, r.status_code)
        self.assertIn('msg', r.text)
        self.assertTrue('淘宝' in r.text)


