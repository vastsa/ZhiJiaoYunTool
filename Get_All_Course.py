import requests


def get_all_course(stuid):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/student/getCourseList'
    data = {
        'stuId': stuid
    }
    html = requests.post(url=url, data=data).json()
    if html['code'] == 1:
        return html['dataList']
    else:
        return 0
