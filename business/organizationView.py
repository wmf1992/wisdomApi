from base.base import base_url,session_headers
import requests,json
from base.commonfun import Common
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class Organization:
    def department(self):
        url = base_url + '/department/index'
        msgs = '部门列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')


    # 获取组织架构的人员列表信息
    def departmentUser(self):
        url = base_url + '/department/user?id=1&page=1&is_page=1&page_size=10'
        msgs = '部门员工'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    # 获取岗位列表
    def station(self):
        url = base_url + '/station/index?page=1&page_size=10'
        msgs = '岗位组列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    # 获取学历信息
    def getBasicInfo(self):
        url = base_url + '/user/getBasicInfo'
        msgs = '基础信息获取'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')

    # 编辑部门
    def editDepartment(self,data):
        url = base_url + '/department/edit'
        form_data = {
            'id': data['id'],
            'name': data['name'],
            'parent_id': data['parent_id']
        }

        msgs = '更新成功'
        C = Common()
        method = 'put'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)


    # 添加部门
    def addDepartment(self,data):
        url = base_url + '/department/add'
        form_data = {
            'name': data['name'],
            'parent_id': data['parent_id']
        }
        msgs = '添加成功'
        C = Common()
        method = 'post'
        C.get_exception(method, url, msgs, session_headers, form_data=form_data)


if __name__ == '__main__':
    l = Organization()
    l.department()
    l.departmentUser()
    l.station()
    l.getBasicInfo()