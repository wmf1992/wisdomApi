from base.base import base_url,approval_session_headers,session_headers,score_session_headers
from base.commonfun import Common

import requests,json,time
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class QualityCheck:

    def quality_check_add(self,data):

        url = base_url + '/quality_check/add'
        msgs = '提交成功'
        C = Common()
        method = 'post'
        form_data = {
            "sub_project_id": data['sub_project_id'],
            "tender_contract_id": data['tender_contract_id'],
            "building_id": data['building_id'],
            "check_time": data['check_time'],
            "labour_score": data['labour_score'],
            "owner_score": data['owner_score'],
            "lack_num": data['lack_num'],
            "deal_num": data['deal_num'],
            "undeal_num": data['undeal_num'],
            "modify_ids": data['modify_ids'],
            "check_desc": data['check_desc'],
            "check_file": data['check_file'],
            "labour_file": data['labour_file'],
            "owner_file": data['owner_file'],
            "labour_contract_id": data['labour_contract_id'],
            "goodness_score": data['goodness_score']

        }

        C.get_exception(method, url, msgs,session_headers,form_data=form_data)
        # C.get_exception(method, url, msgs, session_headers, form_data=form_data)
    # 质量检查详情
    def quality_check_detail(self,checkId):
        url = base_url + '/quality_check_approval/detail?id=%d' %checkId
        msgs = '质量检查详情'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')


    # 质量检查列表
    def quality_check_index(self,pinUlr):

        url = base_url + '/quality_check/index'+pinUlr
        print(url)
        msgs = '质量检查单列表'
        C = Common()
        method = 'get'
        C.get_exception(method, url, msgs, session_headers, form_data='')
    #质量检查审批
    def quality_check_approval(self,data,data_score):

        url = base_url + '/quality_check_approval/check'
        msgs = '操作成功'
        C = Common()
        method = 'post'
        #（不需要填写评分信息）
        form_data = {
            "quality_check_id": data['quality_check_id'],
            "approval_opinions": data['approval_opinions'],
            "check": data['check'],
            "back": data['back'],
            "score": data['score'],

        }
        #（要填写评分信息）
        form_data_score = {
            "files": data_score['files'],
            "reback_file": data_score['reback_file'],
            "images": data_score['images'],
            "reback_score": data_score['reback_score'],
            "new_lack_num": data_score['new_lack_num'],
            "total_undeal_num": data_score['total_undeal_num'],
            "reback_check_desc": data_score['reback_check_desc'],
            "score": data_score['score'],
            "reback_modify_ids": data_score['reback_modify_ids'],
            "quality_check_reback":  data_score['quality_check_reback'],
            "check":  data_score['check'],
            "goodness_score":  data_score['goodness_score'],
            "quality_check_id":  data_score['quality_check_id']
        }
        # 批量执行审批操作
        for session_headers in approval_session_headers:
            C.get_exception(method, url, msgs, session_headers, form_data=form_data)
            time.sleep(3)

        C.get_exception(method, url, msgs, score_session_headers, form_data=form_data_score)
        time.sleep(3)





























