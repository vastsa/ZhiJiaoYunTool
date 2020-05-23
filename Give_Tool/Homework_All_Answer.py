import requests

from Get_All_Course import get_all_course
from Rinse_Answer import Rinse


def main(stuid):
    info = get_all_course(stuid)
    url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/getHomeworkList_new'
    data = {
        'openClassId': info['openClassId'],
        'courseOpenId': info['courseOpenId'],
        'pageSize': '100',
        'page': '1',
        'stuId': stuid,
    }
    html = requests.post(url=url, data=data).json()
    for k in html['homeworkList']:
        url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/previewHomework'
        data = {
            'homeWorkId': k['homeworkId']
        }
        html = requests.post(url=url, data=data).json()['data']
        Rinse(html)


if __name__ == '__main__':
    main('')
