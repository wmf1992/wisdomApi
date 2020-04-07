from base.base import base_url,session_headers
import requests,json
import logging
from base.commonfun import Common
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()


class BuildingView:
    # 请求员工列表信息
    def builds(self):
        url = base_url + '/building/index?page=1&page_size=10'
        msgs = '楼栋列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    # 请求某一个员工信息
    def building_add(self,data):
        url = base_url + '/building/add'
        form_data = {
            'contract_id': data['contract_id'],
            'building_num': data['building_num'],
            'building_area': data['building_area'],
            'floor_up': data['floor_up'],
            'floor_down': data['floor_down'],
            'height': data['height'],
            'building_structure': data['building_structure'],
            'building_basic': data['building_basic'],
            'tech_user': data['tech_user'],
            'civil_user': data['civil_user'],
            'water_user': data['water_user'],
            'elec_user': data['elec_user'],
            'deco_user': data['deco_user'],
            'tester': data['tester'],
            'safer': data['safer'],
            'quality_user': data['quality_user'],
            'data_user': data['data_user'],
            'budget_user': data['budget_user'],
            'logistics_user': data['logistics_user']

        }
        msgs = '添加成功'
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)

if __name__ == '__main__':
    l = BuildingView()
    # l.builds()
    form_data = {
        'contract_id': 253,
        'building_num': '楼栋031601',
        'building_area': 2000000,
        'floor_up': 10,
        'floor_down': 2,
        'height': 10,
        'building_structure': '钢筋水泥',
        'building_basic': '钢筋',
        'tech_user': 19,
        'civil_user': 39,
        'water_user': 33,
        'elec_user': 124,
        'deco_user': 124,
        'tester': 87,
        'safer': 83,
        'quality_user': 25,
        'data_user': 27,
        'budget_user': 63,
        'logistics_user': 105

    }
    l.building_add(form_data)
