import requests


def get_homework_grade(openClassId, homeworkId, stuId, homeworkTermTimeId):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/getHomeworkStuRecord'
    data = {
        'openClassId': openClassId,
        'homeworkId': homeworkId,
        'stuId': stuId,
        'homeworkTermTimeId': homeworkTermTimeId,
    }
    html = requests.post(url=url, data=data).json()
    if html['code'] == 1:
        return html['stuHomeworkList']
    else:
        print(html['msg'])
        return 0


if __name__ == '__main__':
    openClassId = ''
    homeworkId = ''
    stuId = ''
    homeworkTermTimeId = ''
    a = get_homework_grade(openClassId, homeworkId, stuId, homeworkTermTimeId)
    print(a)