#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import pymysql.cursors
import json
# pc 前端接口
base_url = 'http://wisdom_project.yxsoft.net/front'
# 创建人
session_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': '1cbepl/AYdwsf1HxiXwbUhJRupAtnYzNdr02bMrVEay7OxGOnrXqLdjlpecyRD15NhTMAVs',
}
# 审批人
approval_session_headers =[
    {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': 'eda6vgPNtHrWv7qRidnm9ehYtNNT6K8VANMQhxCL8uA7rHCcfQgytZ0ikh+pKRaGHXo+LQI'
    },
    # {
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'access-token': '824705R+n8tFLOnsQ5/UfQT1CqPTGQwva58y0VZq5bi98h2+3JnNEuGdkiBF5dNDVk5kyPw'
    # },
    {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': 'c5632XwHyFZs7X/1P2jG+Vh4fmhwUaSnmW+TpxAnAOwDI67+esR1ITJzggQDmnhUH6vgSaS9'
    },
    # {
    #  'Content-Type': 'application/x-www-form-urlencoded',
    #  'access-token':'2a15RHv88ArWFfuXbFQtt+qB66zGTDuEFg+b6UoNNLHrQyTDucELdeqZZQk9ac2veqqeH8zg'
]
# 总库管田七
inventory_manager_session_headers =[ {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': 'b612OkeMT2B3g4JMeL4ODnC6DfHxp2D7u+nhyoJDU30be3mLrN97gpApBMLXHB1+OHO0vbQ',
}]
# 需要填写评分信息
score_session_headers ={
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': 'e9f5fnATqe7drgcuLAXD5kqqifKyoWdFP5VmLlBJQWugFji4UB5yFgLDH7ECrji1NRrhHuQ',
    }


# 数据库配置信息
connection = pymysql.connect(host='10.0.100.88',
                             user='yxsoft',
                             password='yxsoft',
                             db='yxsoft',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


