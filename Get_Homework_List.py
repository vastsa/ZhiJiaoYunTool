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
    openClassId = 'pkcravurd4zfoouox04m5a'
    courseOpenId = '4s4gar6qiank7g3k15kiyw'
    stuId = 'midwaoaqv6xmebkkd0czew'
    get_homework_list(stuId, openClassId, courseOpenId)
