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
approval_session_headers = [
    {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': 'dfc7vFXsi5Q/s5RuF1aqVwoqX/nBx162i2izEMwebGv2pi6xz0EMaygIbv6Xc2TI4nWBeVM'
    },
    # {
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'access-token': '824705R+n8tFLOnsQ5/UfQT1CqPTGQwva58y0VZq5bi98h2+3JnNEuGdkiBF5dNDVk5kyPw'
    # },
    {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': '9aa3XwD6DSteYR6g1Xvv35VVqJN20fIDCEbJG4IEzR5gZAOmPtwLfrjmMTto6Sp9lTCh6a6C'
    },
    # {
    # 'Content-Type': 'application/x-www-form-urlencoded',
    # 'access-token': 'd2bdlZDUPv5NUoD3ec4xuHe1Cpogl/4TezlDuQuiZUT0odG1OFM2pec4N+rU+AdutPx0jyUB'
    # }
]


# 总库管田七
inventory_manager_session_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'access-token': 'b612OkeMT2B3g4JMeL4ODnC6DfHxp2D7u+nhyoJDU30be3mLrN97gpApBMLXHB1+OHO0vbQ',
}

# 数据库配置信息
connection = pymysql.connect(host='10.0.100.88',
                             user='yxsoft',
                             password='yxsoft',
                             db='yxsoft',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)


