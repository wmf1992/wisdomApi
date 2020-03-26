# coding: utf-8
from base.base import base_url,session_headers
import requests,json,unittest
import logging
from requests import exceptions
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class BaseMenu(unittest.TestCase):
    def leftMenu(self):
        url = base_url + '/rule/leftMenu'

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
            self.assertIn('角色列表', msg['msg'])
            logging.info('leftMenu请求成功')
            # print('post请求出现了异常')
    def behavior(self):
        url = base_url + '/rule/behavior'
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
            self.assertIn('操作列表', msg['msg'])
            logging.info('behavior请求成功')

            # print('post请求出现了异常')
    def userInfo(self):
        url = base_url + '/user/info'
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
            self.assertIn('用户信息', msg['msg'])
            logging.info('/user/info请求成功')

    def toDoBusiness(self):
        url = base_url + '/index/toDoBusiness'
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
            self.assertIn('获取数据成功', msg['msg'])
            logging.info('/index/toDoBusiness请求成功')
    # print('post请求出现了异常')



    def toDoList(self):
        url = base_url + '/index/toDoList'
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
            self.assertIn('获取数据成功', msg['msg'])
            logging.info('/index/toDoList请求成功')


# print('post请求出现了异常')


if __name__ == '__main__':
    l = BaseMenu()
    l.leftMenu()
    l.behavior()
    l.userInfo()
    l.toDoBusiness()
    l.toDoList()