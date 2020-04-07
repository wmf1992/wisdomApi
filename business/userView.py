from base.base import base_url,session_headers
import requests,json
from base.commonfun import Common
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class UserView:
    # 请求员工列表信息
    def users(self):
        url = base_url + '/user/index?city_code=&education=&page=1&page_size=10'
        msgs = '成员列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')
    # 请求某一个员工信息
    def userinfo(self):
        url = base_url + '/user/info?id=125'
        msgs = '用户信息'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

if __name__ == '__main__':
    l = UserView()
    l.users()
    l.userinfo()
