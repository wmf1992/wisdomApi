
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

        # r = requests.get(
        #     url,
        #     headers=session_headers
        # )
        # print(url)
        # print(r.json())
        try:
            res = requests.get(url, headers=session_headers)
            logging.info('材料分类列表请求成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
    # 添加材料分类
    def meterial_type_add(self):
        url = base_url + '/meterial_type/add'

        form_data = {
            'type_name': '一级分类031802'
        }
        try:
            res = requests.post(url,
                                headers=session_headers,
                                data=form_data
                                )
            logging.info('添加一级材料分类成功')
            # print(res.json())
        except Exception as e:
            print("post请求出现了异常：{0}".format(e))
            logging.info(res.status_code)
if __name__ == '__main__':
    l = MeterialtypeView()
    l.get_meterial_type()
    l.meterial_type_add()
