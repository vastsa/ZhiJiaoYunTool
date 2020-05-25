import requests

from Get_Class_Activity import get_activity
from Get_Day_Course import get_course


def Sign_Students(stuid):
    print("【欢迎使用职教云补签助手】")
    print("                  By:Lan")
    date = input("请输入需要补签的日期如(2020-5-20)：")
    courses = get_course(stuid, date)
    if courses == 'no':
        print("你今天没有课，好好休息")
    else:
        print("Lan职教云助手提示您：\n您今天课表如下：")
        for i in range(len(courses['courseNmae'])):
            print(f'【{i + 1}】：{courses["classSection"][i]}{courses["courseNmae"][i]}')
        index = int(input("请输入你要改签到分数的课程：")) - 1
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
        target = int(input("请输入要改分的序号："))
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
        grade_url = 'https://zjyapp.icve.com.cn/newmobileapi/faceTeach/saveSignStuScore'
        data = {
            'signId': SignId,
            'signStuIds': SignStuId,
            'score': get_grade
        }
        result = requests.post(url=grade_url, data=data).json()['msg']
        print(result)
        print("返回首页菜单")
        from Main import main
        main()


if __name__ == '__main__':
    Sign_Students('')
