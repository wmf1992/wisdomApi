from base.commonfun import Common
from base.base import base_url,session_headers
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class MeterialtypeView:
    # 材料分类列表
    def get_meterial_type(self):
        url = base_url + '/meterial_type/index?type_name='
        msgs = '材料类型列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    # 添加材料分类
    def meterial_type_add(self):
        url = base_url + '/meterial_type/add'

        form_data = {
            'type_name': '一级分类031802'
        }
        msgs = '添加成功'
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)


if __name__ == '__main__':
    l = MeterialtypeView()
    l.get_meterial_type()
    l.meterial_type_add()
