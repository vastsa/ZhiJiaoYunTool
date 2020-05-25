import threading
import time

import requests

from Get_Class_Activity import get_activity
from Get_Day_Course import get_course


def sign(signId, stuId, openClassId):
    qdurl = 'https://zjyapp.icve.com.cn/newmobileapi/faceteach/saveStuSign'
    qddata = {
        'signId': signId,
        'stuId': stuId,
        'classState': 2,
        'openClassId': openClassId
    }
    html = requests.post(url=qdurl, data=qddata).json()['msg']
    return html


def jiankong(activities, openClassId, stuId):
    # 反复监控，是否需要存在已开启的签到
    signids = []  # 签到过的ID集合
    for i in range(18000):
        js = 0
        for j in range(len(activities)):
            activity = activities[j]
            datatype = activity['DataType']
            if datatype == '签到' and activity['State'] == 2 and activity['Id'] not in signids:
                signId = activity['Id']
                signids.append(signId)
                print(signId)
                js += 1
                print("您当前有一个签到，正在尝试帮你签到，请稍等！")
                print(activity['Title'])

                # 执行签到，为了能够失败重签，所以嵌套了一下

                def panta():

                    msg = sign(signId, stuId, openClassId)
                    if msg == '签到成功！':
                        print(f"{msg}，我要休息半小时")
                        time.sleep(10)
                    else:
                        print(f"{msg}，正在重新签到")
                        time.sleep(2)
                        panta()

                panta()
        if js == 0:
            print(f"系统未检测到需要签到哦！", end="当前时间：")
            print(time.strftime("%H:%M:%S", time.localtime()))
            time.sleep(30)


def main(stuId):
    courses = get_course(stuId)
    if courses == 'no':
        print("你今天没有课，好好休息")
        input("回车退出！")
    else:
        print("Lan职教云助手提示您：\n您今天课表如下：")
        for i in range(len(courses['courseNmae'])):
            print(f'【{i + 1}】：{courses["classSection"][i]}{courses["courseNmae"][i]}')
        for index in range(len(courses['courseId'])):
            activities = get_activity(stuId, courses["courseId"][index], courses["openClassId"][index])
            jiankong(activities, courses['openClassId'], stuId)
            xcname = threading.Thread(target=jiankong, args=(activities, courses["courseId"][index], stuId))
            xcname.start()


if __name__ == '__main__':
    stuid = ''
    main(stuid)
