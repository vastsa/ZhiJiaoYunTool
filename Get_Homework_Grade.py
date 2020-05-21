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
        print(html)
        return 0


if __name__ == '__main__':
    openClassId = 'o2x1avmro55dslykhbzpsa'
    homeworkId = 'du9caasrboleoc1phbw8mg'
    stuId = 'midwaoaqv6xmebkkd0czew'
    homeworkTermTimeId = 'lv5baaerc6teul62kbz47q'
    get_homework_grade(openClassId, homeworkId, stuId, homeworkTermTimeId)
