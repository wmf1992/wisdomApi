from base.base import base_url,session_headers
import requests,json
import logging
import logging.config
from base.commonfun import Common
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class LabourServicesView:
    # 劳务公司列表
    def get_labour_services(self):
        url = base_url + '/labour_services/index?page=1&page_size=10&company_name=&legal_person_name=&contacts=&contacts_mobile=&is_black=0'

        msgs = '劳务公司列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    # 劳务公司黑名单列表
    def get_labour_services_black(self):
        url = base_url + '/labour_services/index?page=1&page_size=10&company_name=&legal_person_name=&contacts=&contacts_mobile=&is_black=1'

        msgs = '劳务公司列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    # 添加劳务公司
    def labour_services_add(self,data):
        url = base_url + '/labour_services/add'

        form_data = {
            'company_name': data['company_name'],
            'legal_person_name': data['legal_person_name'],
            'province_code': data['province_code'],
            'city_code': data['city_code'],
            'area_code': data['area_code'],
            'address': data['address'],
            'contacts': data['contacts'],
            'contacts_mobile': data['contacts_mobile'],
            'original_business_license_id': data['original_business_license_id'],
            'copy_business_license_id': data['copy_business_license_id'],
            'opening_permit_id': data['opening_permit_id'],
            'letter_of_attorney_id': data['letter_of_attorney_id'],
            'front_legal_person_idcard_id': data['front_legal_person_idcard_id'],
            'back_legal_person_idcard_id': data['back_legal_person_idcard_id'],
            'sort': data['sort']
        }

        msgs = '添加成功'
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)

if __name__ == '__main__':
    l = LabourServicesView()
    l.get_labour_services()
    l.get_labour_services_black()
    l.labour_services_add()
