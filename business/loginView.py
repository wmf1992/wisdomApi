from base.base import base_url,session_headers
import requests,json
import logging
import logging.config
CON_LOG='../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
class organization:
    def login(self):
        url = base_url+'/index/login'
        form_data = {
            'username': '13063054221',
            'password': '888888',
            'verify_code': '5641'

        }

        r = requests.post(
            url,
            headers=session_headers,
            data=form_data

        )
        print(url)
        print(r.json())
if __name__ == '__main__':
    l = organization()
    l.login()