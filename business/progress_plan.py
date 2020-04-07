from base.base import base_url,session_headers
from base.commonfun import Common
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class ProgressPlan:
    def progress_plan_index(self):
        url = base_url + '/progress_plan/index?page=1&page_size=10&building_id=&labour_contract_id='
        msgs = '进度计划列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')
    def progress_plan_detail(self):
        url = base_url + '/progress_plan/detail?id=196'
        msgs = '进度计划详情'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')