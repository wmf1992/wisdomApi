
from base.base import base_url,session_headers
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class WarehouseView:
    # 仓库列表
    def get_warehouse(self):
        url = base_url + '/warehouse/index?page=1&page_size=10&warehouse_num=&warehouse_name=&manager_username=&contract_name=&is_build='

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('仓库列表请求成功')
            # res.status_code 是数字类型
            # status = res.status_code
            # if  status==200:
            #     print('成功')
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 添加仓库
    def warehouse_add(self):
        url = base_url + '/warehouse/add'

        form_data = {
            'warehouse_name': '仓库031802',
            'warehouse_address': '福建省厦门市集美区',
            'manager_user': 76,
            'approval_user': 17,
            'contract_id': 41,
            'is_build': 1
        }
        try:
            res = requests.post(url,
                                headers=session_headers,
                                data=form_data
                                )
            logging.info('添加仓库成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
if __name__ == '__main__':
    l = WarehouseView()
    l.get_warehouse()
    l.warehouse_add()
