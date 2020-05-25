import configparser
import time

import requests


def login():
    userName = input("小伙纸，请输入您的学号：")
    userPwd = input("小伙纸，请输入您的密码：")
    login_url = 'https://zjyapp.icve.com.cn/newmobileapi/mobilelogin/newlogin'
    login_data = {
        'clientId': 'd3a22c66c8154964af6c8f3d0046f82b',
        'sourceType': '2',
        'userPwd': userPwd,
        'userName': userName,
        'appVersion': '3',
    }
    # 发送登陆请求
    html = requests.post(url=login_url, data=login_data).json()
    print(html)
    if html['code'] == -1:
        print(html['msg'])
        input("登陆失败！如果密码有英文请切换到英文输入。请重新登陆")
        login()
    else:
        try:
            config = configparser.ConfigParser()  # 实例化一个配置写入
            config.add_section('information')  # 创建一个选择器
            config.set('information', 'userId', html['userId'])  # 保存学生ID
            config.set('information', 'schoolId', html['schoolId'])  # 保存学生ID
            config.write(open('config.info', 'w'))  # 写入文件
        except:
            input("登陆失败！如果密码有英文请切换到英文输入。请重新登陆")
            login()


if __name__ == '__main__':
    login()