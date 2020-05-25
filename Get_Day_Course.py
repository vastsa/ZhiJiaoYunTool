import time

import requests


# 获取当日课程

def get_course(stuid, today=time.strftime("%Y-%m-%d", time.localtime())):
    get_activity_url = 'https://zjyapp.icve.com.cn/newmobileapi/faceteach/getStuFaceTeachList'
    data = {
        'stuId': stuid,
        'faceDate': today  # 查询当天的课程的日期
    }
    html = requests.post(url=get_activity_url, data=data).json()
    html = html['dataList']
    courses = len(html)  # 获取课程数量
    if courses == 0:  # 如果无课，返回no，否则返回课程信息
        return 'no'
    else:
        courseId = []  # 课程ID
        courseNmae = []  # 课程名字
        classSection = []  # 第几节
        openClassId = []  # 开设班级
        courseOpenId = []
        for i in range(courses):
            courseNmae.append(html[i]['courseName'])
            courseId.append(html[i]['Id'])
            classSection.append(html[i]['classSection'])
            openClassId.append(html[i]['openClassId'])
            courseOpenId.append(html[i]['courseOpenId'])
        return {
            'courseId': courseId,
            'courseNmae': courseNmae,
            'classSection': classSection,
            'openClassId': openClassId,
            'courseOpenId': courseOpenId
        }


if __name__ == '__main__':
    stuid = ''
    print(get_course(stuid))
