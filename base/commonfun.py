#!/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
import logging.config
import requests,json
from requests import exceptions
import unittest

CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

class Common(unittest.TestCase):

    def get_exception(self,method,url,msgs,session_headers,form_data=''):

        try:
            if method == 'get':
                res = requests.get(url,timeout=3, headers=session_headers)
            elif method == 'post':
                res = requests.post(url,timeout=3, headers=session_headers,data=form_data)
            elif method == 'put':
                res = requests.put(url, timeout=3, headers=session_headers, data=form_data)
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
            logging.info(msg)
            self.assertEqual(200, res.status_code)
            self.assertIn(msgs, msg['msg'])
            return msg


