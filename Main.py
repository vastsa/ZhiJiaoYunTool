import os

import requests

from Brainstorm import main as brainstorm
from Exam_Answer import main as examans
from Exam_Time import main as exam_time
from Get_Stu_Info import get_info
from Homework_Answer import main as homeanswer
from Homework_Time import main as retime
from Re_Grade import Main as regrade
from Retroactive import main as buqian
from Sign_Auto import main as autosign
from rejectHomework import main as tui

url = 'https://www.lanol.cn/zjypackage.json'
info = requests.get(url).json()
infomation = info['information']
print(infomation['message'])
name = info['name']
new_version = info['version']
now_version = '1.5'
if now_version < new_version:
    print(f"版本有更新！目前版本{now_version}，最新版本{new_version}，请前往www.lanol.cn获取最新版")
    input("回车退出！")
else:
    print(f'随机一句：{requests.get("https://v1.hitokoto.cn/?encode=text&charset=utf8").text}')
    stuId = get_info()
    print(f"【欢迎使用{name}】")
    print(" www.lanol.cn     By:Lan")
    print("【1】职教云签到监控功能")
    print("【2】职教云签到改命功能")
    print("【3】职教云作业改分功能")
    print("【4】职教云作业改时功能")
    print("【5】头脑风暴改评分功能")
    print("【6】职教云作业答案功能")
    print("【7】职教云考试答案功能")
    print("【8】职教云作业退回功能")
    print("【9】职教云考试退回功能")
    print("【10】作业批量获取功能")
    print("【0】 退 出 当 前 账 号")
    tool = input("请输入功能序号：")
    if tool == '1':
        autosign(stuId)
    elif tool == '2':
        buqian(stuId)
    elif tool == '3':
        regrade(stuId)
    elif tool == '4':
        retime(stuId)
    elif tool == '5':
        brainstorm(stuId)
    elif tool == '6':
        homeanswer(stuId)
    elif tool == '7':
        examans(stuId)
    elif tool == '8':
        tui(stuId)
    elif tool == '9':
        exam_time(stuId)
    elif tool == '0':
        if os.path.exists('config.info'):
            os.remove('config.info')
            print("注销成功，回车后退出")
            input()
        else:
            print("您当前没有登录！")
            input()
