import requests

from helpers import get_lan_ip, str_to_base64
from local_settings import HZNU_STU_NUM, HZNU_STU_PWD

api = 'http://172.31.1.30/include/auth_action.php'

IP = get_lan_ip()[:-1] + '1'


def init_data(username, password):
    return {
        'action': 'login',
        'username': username,
        'password': '{B}' + str_to_base64(password),
        'ac_id': '9',
        'user_ip': IP,
        'nas_ip': '',
        'user_mac': '',
        'url': '',
        'ajax': 1,
    }


data = init_data(HZNU_STU_NUM, HZNU_STU_PWD)
resp = requests.post(api, data=data)
if 'login_ok' in resp.content.decode():
    print('Login success')
else:
    print(resp.content.decode())
