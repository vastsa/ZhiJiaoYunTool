# 获取学生信息
import configparser

import requests

from Login import login

info_url = 'https://zjyapp.icve.com.cn/newmobileapi/mobilelogin/getUserInfo'


def get_info():
    config = configparser.ConfigParser()

    try:
        config.read('config.info')
        stuId = config['information']['userid']
    except:
        login()
        config.read('config.info')
        stuId = config['information']['userid']
    data = {
        'userId': stuId
    }
    html = requests.post(url=info_url, data=data).json()
    if html['code'] == -1:
        print("系统检测到您是第一次登陆或者信息已失效，所以请重新登陆！")

        login()
        config.read('config.info')
        stuId = config['information']['userid']
        get_info(stuId)
    else:
        return print_info(html)


def print_info(html):
    data = html['userInfo']
    name = data['displayName']
    school = data['schoolName']
    QQ = data['QQ']
    print(f"姓名\t\t\t学校\t\t\t\tQQ\n{name}\t{school}\t{QQ}")
    return data['Id']


if __name__ == '__main__':
    print(get_info(''))
