# coding: utf-8
from base.base import base_url,session_headers
import requests,json,unittest
import logging
from requests import exceptions
from base.commonfun import Common
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class BaseMenu(unittest.TestCase):
    def leftMenu(self):
        url = base_url + '/rule/leftMenu'
        msgs = '角色列表'

        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    def behavior(self):
        url = base_url + '/rule/behavior'
        msgs = '操作列表'

        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    def userInfo(self):
        url = base_url + '/user/info'
        msgs = '用户信息'

        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')


    def toDoBusiness(self):
        url = base_url + '/index/toDoBusiness'
        msgs = '获取数据成功'

        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')




    def toDoList(self):
        url = base_url + '/index/toDoList'
        msgs = '获取数据成功'

        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')



# print('post请求出现了异常')


if __name__ == '__main__':
    l = BaseMenu()
    l.leftMenu()
    l.behavior()
    l.userInfo()
    l.toDoBusiness()
    l.toDoList()