from base.base import base_url,session_headers
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class worktypeView:
    # 工种列表
    def work_type(self):
        url = base_url + '/work_type/index?page=1&page_size=10&work_num=&work_name='

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('工种列表请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 添加工种成功
    def work_type_add(self):
        url = base_url + '/work_type/add'

        form_data = {
            'work_num': 'ZZ0317',
            'work_name': '装潢工'
        }
        try:
            res = requests.post(url,
                                headers=session_headers,
                                data=form_data
                                )
            logging.info('添加工种成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
if __name__ == '__main__':
    l = worktypeView()
    l.work_type()
    l.work_type_add()
