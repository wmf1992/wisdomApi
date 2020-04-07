from base.commonfun import Common
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
        msgs = '仓库列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    # 添加仓库
    def warehouse_add(self,data):
        url = base_url + '/warehouse/add'

        form_data = {
            'warehouse_name': data['warehouse_name'],
            'warehouse_address': data['warehouse_address'],
            'manager_user': data['manager_user'],
            'approval_user': data['approval_user'],
            'contract_id': data['contract_id'],
            'is_build': data['is_build']
        }
        msgs = '添加成功'
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)


if __name__ == '__main__':
    l = WarehouseView()
    l.get_warehouse()
    l.warehouse_add()
