import os

from Brainstorm import main as brainstorm
from Exam_Answer import main as examans
from Get_Stu_Info import get_info
from Homework_Answer import main as homeanswer
from Homework_Time import main as retime
from Re_Grade import Main as regrade
from Retroactive import main as buqian
from Sign_Auto import main as autosign

stuId = get_info()
print("【欢迎使用职教云综合助手】")
print(" www.lanol.cn     By:Lan")
print("【1】职教云签到监控功能")
print("【2】职教云签到改命功能")
print("【3】职教云作业改分功能")
print("【4】职教云作业改时功能")
print("【5】头脑风暴改评分功能")
print("【6】作业 答案 查询功能")
print("【7】考试 答案 查询功能")
print("【8】 退 出 当 前 账 号")
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
    if os.path.exists('config.info'):
        os.remove('config.info')
        print("注销成功，回车后退出")
        input()
    else:
        print("您当前没有登录！")
        input()
