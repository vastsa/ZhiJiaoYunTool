import os

from Get_Stu_Info import get_info
from Homework_Time import main as retime
from Re_Grade import Main as regrade
from Retroactive import main as buqian
from Sign_Auto import main as autosign

os.system("mode con cols=46 lines=24")
stuId = get_info()
print("【欢迎使用职教云综合助手】")
print(" www.lanol.cn     By:Lan")
print("【1】职教云签到监控功能")
print("【2】职教云签到改命功能")
print("【3】职教云作业改分功能")
print("【4】职教云作业改时功能")
tool = input("请输入功能序号：")
if tool == '1':
    autosign(stuId)
elif tool == '2':
    buqian(stuId)
elif tool == '3':
    regrade(stuId)
elif tool == '4':
    retime(stuId)
