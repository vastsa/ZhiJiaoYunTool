import os

import requests

from Class_Activity_Grade import get_activity as ketang
from Exam_Answer import main as examans
from Exam_Reject import examlist as reexam
from Exam_Time import main as exam_time
from Get_All_Answer import main as tiku
from Get_Stu_Info import get_info
from Homework_Answer import main as homeanswer
from Homework_Time import main as retime
from No_Sign import main as nosign
from Re_Grade import Main as regrade
from Retroactive import main as buqian
from Sign_Auto import main as autosign
from rejectHomework import main as tui


def main():
    url = 'http://app.1314567.xyz/zjypackage.json'
    info = requests.get(url).json()
    infomation = info['information']
    print(infomation['message'])
    name = info['name']
    new_version = info['version']
    now_version = '1.6'
    if now_version < new_version:
        print(f"版本有更新！目前版本{now_version}，最新版本{new_version}，请前往www.lanol.cn获取最新版")
        input("回车退出！")
    else:
        print(f'随机一句：{requests.get("https://v1.hitokoto.cn/?encode=text&charset=utf8").text}')
        print('警告:本软件仅供学习交流使用,下载后请于24小时内删除,严禁用于商业及非法用途!')
        password = get_info()
        stuId = password['stuId']
        schoolid = password['schoolId']
        print(f"【欢迎使用{name}】")
        print(" www.lanol.cn     By:Lan")
        print("【1】自动签到监控功能")
        print("【2】签到补签改分功能")
        print("【3】单个作业改分功能")
        print("【4】单个作业改时功能")
        print("【5】课堂活动改分功能")
        print("【6】获取作业答案功能")
        print("【7】获取考试答案功能")
        print("【8】职教云作业退回功能")
        print("【9】职教云考试改时功能")
        print("【10】科目题库获取功能")
        print("【11】考 试 退 回 功 能")
        print("【12】查询未签到人员")
        print("【0】 退 出 当 前 账 号")
        tool = input("请输入功能序号：")
        if tool == '1':
            autosign(stuId)
        elif tool == '2':
            buqian(stuId, schoolid)
        elif tool == '3':
            regrade(stuId)
        elif tool == '4':
            retime(stuId)
        elif tool == '5':
            ketang(stuId, name)
        elif tool == '6':
            homeanswer(stuId)
        elif tool == '7':
            examans(stuId)
        elif tool == '8':
            tui(stuId)
        elif tool == '9':
            exam_time(stuId)
        elif tool == '10':
            tiku(stuId, schoolid)
        elif tool == '11':
            reexam(stuId)
        elif tool == '12':
            nosign(stuId)
        elif tool == '0':
            if os.path.exists('config.info'):
                os.remove('config.info')
                print("注销成功，回车后退出")
                input()
            else:
                print("您当前没有登录！")
                input()


if __name__ == '__main__':
    main()
