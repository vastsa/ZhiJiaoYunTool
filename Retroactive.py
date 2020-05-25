# 补签模块
import requests

from Get_Class_Activity import get_activity
from Get_Day_Course import get_course


def main(stuid, schoolid):
    print("【欢迎使用职教云补签助手】")
    print("注意事项：修改之后课堂表现可看到结果，老师那边会显示已参与")
    print("                  By:Lan")
    date = input("请输入需要补签的日期如(2020-5-20)：")
    courses = get_course(stuid, date)
    if courses == 'no':
        print("你今天没有课，好好休息")
    else:
        print("Lan职教云助手提示您：\n您今天课表如下：")
        for i in range(len(courses['courseNmae'])):
            print(f'【{i + 1}】：{courses["classSection"][i]}{courses["courseNmae"][i]}')
        index = int(input("请输入你要改签的课程：")) - 1
        activities = get_activity(stuid, courses["courseId"][index], courses["openClassId"][index])
        buqianname = []
        buqianid = []
        for j in range(len(activities)):
            datatype = activities[j]['DataType']
            if datatype == "签到":
                buqianname.append(activities[j]['Title'])
                buqianid.append(activities[j]['Id'])
        for i in range(len(buqianid)):
            print(f'【{i}】{buqianname[i]}')
        target = int(input("请输入要逆天改命的序号："))
        datas = f'{{"OpenClassId":"{courses["openClassId"]}","Id":"{stuid}","SignId":"{buqianid[target]}","StuId":"{stuid}","SignResultType":1,"SourceType":2,"schoolId":"{schoolid}"}}'
        xdata = {
            'data': f'{datas}'
        }
        bqurl = 'https://zjyapp.icve.com.cn/newmobileapi/faceteach/changeSignType'
        html = requests.post(url=bqurl, data=xdata).json()
        if html['code'] == 1:
            print(html['msg'])
            print("逆天改命成功，Lan's Blog：https://www.lanol.cn")
            re_grade = input("是否需要修改签到分数：是 或 否")
            if re_grade == "是":
                SignId = buqianid[target]
                activityid = activities[target]['Id']
                url = 'https://zjyapp.icve.com.cn/newmobileapi/faceTeach/getCheckStuInfo'
                data = {
                    'signId': SignId,
                    'activityId': activityid,
                }
                html = requests.post(url=url, data=data).json()
                for i in html['signedList']:
                    if i['StuId'] == stuid:
                        SignStuId = i['SignStuId']
                get_grade = input("请输入要改的分数（1-5）：")
                if int(get_grade) < 6:
                    grade_url = 'https://zjyapp.icve.com.cn/newmobileapi/faceTeach/saveSignStuScore'
                    data = {
                        'signId': SignId,
                        'signStuIds': SignStuId,
                        'score': get_grade
                    }
                    result = requests.post(url=grade_url, data=data).json()['msg']
                    print(result)
                    print("返回首页菜单")
                    from Main import main as menu
                    menu()
                else:
                    print("再见")
                    from Main import main as menu
                    menu()
        else:
            print(html['msg'])
            print("逆天改命失败，请联系Lan")
            from Main import main as menu
            menu()


if __name__ == '__main__':
    stuid = ''
    main(stuid)
