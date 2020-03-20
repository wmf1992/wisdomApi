# coding: utf-8
from base.base import base_url,session_headers
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class baseMebu:
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
            if res.status_code == 200:

                logging.info('左边菜单栏请求成功')
            else:
                logging.info('左边菜单栏请求失败')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)

            # print('post请求出现了异常')
    def behavior(self):
        url = base_url + '/rule/behavior'
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('behavior请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)

            # print('post请求出现了异常')
    def userInfo(self):
        url = base_url + '/user/info'
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('userInfo请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)

    def toDoBusiness(self):
        url = base_url + '/index/toDoBusiness'
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('toDoBusiness请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # print('post请求出现了异常')



    def toDoList(self):
        url = base_url + '/index/toDoList'
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('toDoList请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)


# print('post请求出现了异常')


if __name__ == '__main__':
    l = baseMebu()
    l.leftMenu()
    l.behavior()
    l.userInfo()
    l.toDoBusiness()
    l.toDoList()