
from base.base import base_url,session_headers
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class StafView:
    # 劳务人员列表
    def get_staff(self):
        url = base_url + '/staff/index?page=1&page_size=10&name=&work_type_id=&gender=&province_code=&city_code=&birthday_start=&birthday_end=&mobile=&company_id=&initiation_time_start=&initiation_time_end=&level=&is_black=0'

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('劳务人员列表请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 劳务人员详情页
    def labourForceDetails(self):
        url = base_url + '/staff/detail?id=28'

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('劳务人员列表请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)


    # 劳务人员黑名单列表
    def get_staff_black(self):
        url = base_url + '/staff/index?page=1&page_size=10&name=&work_type_id=&gender=&province_code=&city_code=&birthday_start=&birthday_end=&mobile=&company_id=&initiation_time_start=&initiation_time_end=&level=&is_black=1'

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('劳务人员黑名单列表请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 添加劳务人员
    def staff_add(self):
        url = base_url + '/staff/add'

        form_data = {
            'avatar': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/a3d11afa6a8ae82938f1070ae1c4022c.jpg',
            'name': '劳务人员031702',
            'staff_num': 'LWRY031702',
            'work_type_id': 30,
            'gender': 1,
            'province_code': 150000,
            'city_code': 150100,
            'birthday': '1981-04-03',
            'mobile': '18859663968',
            'company_id': 9,
            'major_years': '5年',
            'initiation_time': '2011-06-01',
            'level': '5级',
            'id_num': '350524199205105568',
            'card_img_front': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/7f9dfa436d0f2d988d95700221e34889.jpg',
            'card_img_back': 'http://wisdom-youxuan-dev.oss-cn-chengdu.aliyuncs.com/images/7f9dfa436d0f2d988d95700221e34889.jpg'
        }
        try:
            res = requests.post(url,
                                headers=session_headers,
                                data=form_data
                                )
            logging.info('添加劳务人员成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
if __name__ == '__main__':
    l = StafView()
    l.get_staff()
    l.get_staff_black()
    l.staff_add()
