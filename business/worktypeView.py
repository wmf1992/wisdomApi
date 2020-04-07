from base.base import base_url,session_headers
from base.commonfun import Common
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class WorktypeView:
    # 工种列表
    def work_type(self):
        url = base_url + '/work_type/index?page=1&page_size=10&work_num=&work_name='
        msgs = '部门列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    # 添加工种成功
    def work_type_add(self,data):
        url = base_url + '/work_type/add'

        form_data = {
            'work_num': data['work_num'],
            'work_name':  data['work_name']
        }
        msgs = '添加成功'
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)


if __name__ == '__main__':
    l = WorktypeView()
    l.work_type()
    l.work_type_add()
