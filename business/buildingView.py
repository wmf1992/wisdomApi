from base.base import base_url,session_headers
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class buildingView:
    # 请求员工列表信息
    def builds(self):
        url = base_url + '/building/index?page=1&page_size=10'

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('楼栋列表请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 请求某一个员工信息
    def building_add(self):
        url = base_url + '/building/add'

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
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
        try:
            res = requests.post(url,
                               headers=session_headers,
                               data=form_data
                               )
            logging.info('添加楼栋成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
if __name__ == '__main__':
    l = buildingView()
    l.builds()
    l.building_add()
