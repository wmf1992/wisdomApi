from base.base import base_url,session_headers
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class organization:
    def department(self):
        url = base_url + '/department/index'
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('组织架构--部门信息请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)

    # 获取组织架构的人员列表信息
    def departmentUser(self):
        url = base_url + '/department/user?id=1&page=1&is_page=1&page_size=10'
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('组织架构---人员信息请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 获取岗位列表
    def station(self):
        url = base_url + '/station/index?page=1&page_size=10'
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('组织架构---岗位列表请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 获取学历信息
    def getBasicInfo(self):
        url = base_url + '/user/getBasicInfo'
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('组织架构---学历信息请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 编辑部门
    def editDepartment(self,id,name,parent_id):
        url = base_url + '/department/edit'
        form_data = {
            id: id,
            name: name,
            parent_id: parent_id
        }
        try:
            res = requests.put(
                url,
                data=form_data,
                headers=session_headers
            )
            logging.info('组织架构---编辑岗位成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)

        # 添加部门
        def addDepartment(self, id, name, parent_id):
            url = base_url + '/department/add'
            form_data = {
                id: id,
                name: name,
                parent_id: parent_id
            }
            try:
                res = requests.put(
                    url,
                    data=form_data,
                    headers=session_headers
                )
                logging.info('组织架构---添加岗位成功')
                # print(res.json())
            except Exception as e:
                print("post请求出现了异常：{0}".format(e))
                logging.info(res.status_code)

if __name__ == '__main__':
    l = organization()
    l.department()
    l.departmentUser()
    l.station()
    l.getBasicInfo()