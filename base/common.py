import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class Common:
    # status_code响应状态码
    def get_exception(self,status_code):
        if status_code == 200:

            logging.info('添加材料成功')
        else:
            logging.info('添加材料失败，status_code：%d' % (status_code))

