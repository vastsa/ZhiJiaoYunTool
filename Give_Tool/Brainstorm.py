import requests

from Get_Class_Activity import get_activity
from Get_Day_Course import get_course


def get_stormid(activity, stuid):
    ids = []
    index = 1
    for i in activity:
        if i['DataType'] == '头脑风暴':
            print(f'【{index}】{i["Title"]}')
            index += 1
            ids.append(i['Id'])
    target = ids[int(input("请选择序号：")) - 1]
    last_url = 'https://zjyapp.icve.com.cn/newmobileapi/faceTeach/getBrainStromStuInfo'
    data = {
        'brainStormId': target
    }
    data = requests.post(url=last_url, data=data).json()
    if data['code'] == 1:
        for i in data['datalist']:
            if i['StuId'] == stuid:
                return i['Id']
    else:
        print(data['msg'])
        input("回车退出")


def main(stuid):
    date = input("请输入需要改分的日期如(2020-5-20)：")
    courses = get_course(stuid, date)
    if courses == 'no':
        print("你今天没有课，好好休息")
    else:
        print("Lan职教云助手提示您：\n您今天课表如下：")
        for i in range(len(courses['courseNmae'])):
            print(f'【{i + 1}】：{courses["classSection"][i]}{courses["courseNmae"][i]}')
        index = int(input("请输入你要改分的课程：")) - 1
        activities = get_activity(stuid, courses["courseId"][index], courses["openClassId"][index])
        stormid = get_stormid(activities, stuid)
        grade = int(input("请输入分数："))
        url = 'https://zjyapp.icve.com.cn/newmobileapi/faceTeach/saveStuStormScore'
        data = {
            'brainStormStuIds': stormid,
            'score': grade,
        }
        html = requests.post(url=url, data=data).json()
        print(html['msg'])
        main(stuid)


if __name__ == '__main__':
    activityid = ''
    openclassid = ''
    stuid = ''
    main(stuid)
