import requests


def get_homework_list(stuId, openClassId, courseOpenId):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/getHomeworkList_new'
    data = {
        'openClassId': openClassId,
        'courseOpenId': courseOpenId,
        'pageSize': '100',
        'page': '1',
        'stuId': stuId,
    }
    html = requests.post(url=url, data=data).json()
    if html['code'] == 1:
        return html['homeworkList']
    else:
        return 0


if __name__ == '__main__':
    openClassId = ''
    courseOpenId = ''
    stuId = ''
    get_homework_list(stuId, openClassId, courseOpenId)
