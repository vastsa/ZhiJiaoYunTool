from Get_Stu_Info import get_info
from Retroactive import main as buqian
from Sign_Auto import main as autosign

stuid = get_info()
print("【欢迎使用职教云综合助手】")
print("                  By:Lan")
print("【0】职教云签到监控功能")
print("【1】职教云签到改命功能")
tool = input("请输入功能序号：")
if tool == '0':
    autosign(stuid)
else:
    buqian(stuid)
