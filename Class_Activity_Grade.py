import requests

from Get_Day_Course import get_course


def discuss(id, stuid, grade):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/faceTeach/getDiscussReplyList'
    data = {
        'discussId': id
    }
    data = requests.post(url=url, data=data).json()['discussInfo']['replyList']
    for i in data:
        if stuid == i['creatorId']:
            url = 'https://zjyapp.icve.com.cn/newmobileapi/faceTeach/saveStuDiscussScore'
            data = {
                'discussId': i['discussId'],
                'discussStuIds': stuid,
                'replyIds': i['Id'],
                'score': grade,
            }
            html = requests.post(url=url, data=data).json()
            input(f'{html["msg"]}')


def BrainStorm(id, stuid, grade):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/faceTeach/getBrainStromStuInfo'
    data = {
        'brainStormId': id
    }
    html = requests.post(url=url, data=data).json()['datalist']
    for i in html:
        if i['StuId'] == stuid:
            brainStormStuIds = i['Id']
            url = 'https://zjyapp.icve.com.cn/newmobileapi/faceTeach/saveStuStormScore'
            data = {
                'brainStormStuIds': brainStormStuIds,
                'score': grade
            }
            html = requests.post(url=url, data=data).json()
            input(f'{html["msg"]}')


def Question(id, stuid, grade, name):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/faceTeach/getStuAskedList'
    data = {
        'askId': id
    }
    html = requests.post(url=url, data=data).json()['dataList']
    for i in html:
        if i['Name'] == name:
            stuIds = i['Id']
            url = 'https://zjyapp.icve.com.cn/newmobileapi/faceTeach/saveStuAskScore'
            data = {
                'score': grade,
                'stuIds': stuIds,
                'askId': id,
            }
            html = requests.post(url=url, data=data).json()
            input(f'{html["msg"]}')


def get_activity(stuid, stuname):
    print("【欢迎使用课堂活动改分功能】")
    print("                  By:Lan")
    date = input("请输入需要改活动的日期如(2020-5-20)：")
    courses = get_course(stuid, date)
    if courses == 'no':
        print("你今天没有课，好好休息")
    else:
        print("Lan职教云助手提示您：\n您今天课表如下：")
        for i in range(len(courses['courseNmae'])):
            print(f'【{i + 1}】：{courses["classSection"][i]}{courses["courseNmae"][i]}')
        index = int(input("请输入你要改签的课程：")) - 1
        activityId = courses["courseId"][index]
        courseOpenId = courses['courseOpenId'][index]
    url = 'https://zjyapp.icve.com.cn/newmobileapi/faceteachbytea/getOpenClassFaceTeachList'
    data = {
        'courseOpenId': courseOpenId,
        'activityId': activityId,
        'type': '2',
    }
    html = requests.post(url=url, data=data).json()
    if html['code'] == 1:
        activity_list = html['list']
        index = 1
        for i in activity_list:
            print(f'【{index}】{i["title"]}')
            index += 1
        target = int(input("请输入你要修改的序号：")) - 1
        grade = input("请输入分数：")
        type = activity_list[target]['activityType']
        if type == '提问':
            Question(activity_list[target]['Id'], stuid, grade, stuname)
        elif type == '头脑风暴':
            BrainStorm(activity_list[target]['Id'], stuid, grade)
        elif type == '讨论':
            discuss(activity_list[target]['Id'], stuid, grade)
        else:
            input("暂不支持改类型！")
        from Main import main as menu
        menu()
    else:
        input("获取失败")


if __name__ == '__main__':
    stuname = ''
    get_activity('', stuname)
