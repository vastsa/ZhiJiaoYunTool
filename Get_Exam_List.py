import requests


def main(openClassId, courseOpenId, userId):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/onlineExam/getExamList_new'
    data = {
        'openClassId': openClassId,
        'courseOpenId': courseOpenId,
        'pageSize': '100',
        'stuId': userId,
    }
    result = requests.post(url=url, data=data).json()['examList']
    return result
