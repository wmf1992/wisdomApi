
from base.base import base_url,session_headers
import requests,json
import logging
from base.commonfun import Common
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class StafView:
    # 劳务人员列表
    def get_staff(self):
        url = base_url + '/staff/index?page=1&page_size=10&name=&work_type_id=&gender=&province_code=&city_code=&birthday_start=&birthday_end=&mobile=&company_id=&initiation_time_start=&initiation_time_end=&level=&is_black=0'
        msgs = '劳务人员列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    # 劳务人员详情页
    def labourForceDetails(self):
        url = base_url + '/staff/detail?id=28'
        msgs = '劳务人员详情'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    # 劳务人员黑名单列表
    def get_staff_black(self):
        url = base_url + '/staff/index?page=1&page_size=10&name=&work_type_id=&gender=&province_code=&city_code=&birthday_start=&birthday_end=&mobile=&company_id=&initiation_time_start=&initiation_time_end=&level=&is_black=1'
        msgs = '劳务人员列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')
    # 添加劳务人员
    def staff_add(self,data):
        url = base_url + '/staff/add'

        form_data = {
            'avatar': data['avatar'],
            'name': data['name'],
            'staff_num': data['staff_num'],
            'work_type_id': data['work_type_id'],
            'gender': data['gender'],
            'province_code': data['province_code'],
            'city_code': data['city_code'],
            'birthday': data['birthday'],
            'mobile': data['mobile'],
            'company_id': data['company_id'],
            'major_years': data['major_years'],
            'initiation_time': data['initiation_time'],
            'level': data['level'],
            'id_num': data['id_num'],
            'card_img_front': data['card_img_front'],
            'card_img_back': data['card_img_back']
        }
        msgs = '添加成功'
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)

if __name__ == '__main__':
    l = StafView()
    l.get_staff()
    l.get_staff_black()
    l.staff_add()
