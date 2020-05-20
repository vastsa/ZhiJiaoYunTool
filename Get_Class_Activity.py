import requests


# 获取课堂活动

def get_activity(stuid, courseId, openClassId):
    # 课堂活动获取
    get_activity_url = 'https://zjyapp.icve.com.cn/newmobileapi/faceteach/newGetStuFaceActivityList'
    data = {
        'activityId': courseId,
        'stuId': stuid,
        'classState': '2',
        'openClassId': openClassId
    }
    html = requests.post(url=get_activity_url, data=data).json()['dataList']
    return html


if __name__ == '__main__':
    activityid = ''
    openclassid = ''
    stuid = ''
    get_activity(stuid, activityid, openclassid)
