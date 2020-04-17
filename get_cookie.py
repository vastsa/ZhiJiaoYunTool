import pickle

import requests
import configparser

userName = input("请输入你的学号：")
userPwd = input("请输入你的密码：")
url = 'https://zjyapp.icve.com.cn/newmobileapi/mobilelogin/newlogin'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'zjyapp.icve.com.cn',
    'Connection': 'close',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'okhttp/3.10.0',
}
data = {
    'clientId': 'd3a22c66c8154964af6c8f3d0046f82b',
    'sourceType': '2',
    'userPwd': userPwd,
    'userName': userName,
    'appVersion': '3',
}
html = requests.post(url=url, headers=headers, data=data)
html_json = html.json()
# 将配置信息写入配置文件
config_writer = configparser.ConfigParser()  # 实例化配置写入
config_writer.add_section('information')  # 创建information选择器
config_writer.set("information", 'userId', html_json['userId'])  # 将userId写入information
config_writer.write(open('config.info', 'w'))  # 将配置文件输出到文件
