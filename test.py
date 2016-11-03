import requests

api = 'http://ids2.hznu.edu.cn/amserver/UI/Login'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'IDToken0': '',
    'IDToken1': '2014211440',
    'IDToken2': '227685',
    'IDButton': '登陆',
    'goto': '',
    'encoded': 'false',
    'gx_charset': 'UTF-8',
}

resp = requests.post(api, data=data, headers=headers, allow_redirects=False)
print(resp.is_redirect)
print(resp.status_code)
