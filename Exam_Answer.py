import requests
from Get_All_Course import get_all_course
from Rinse_Answer import Rinse


def exam_list(stuId):
    allcourse = get_all_course(stuId)
    url = 'https://zjyapp.icve.com.cn/newmobileapi/onlineExam/getExamList_new'
    data = {
        'openClassId': allcourse['openClassId'],
        'courseOpenId': allcourse['courseOpenId'],
        'pageSize': '100',
        'stuId': stuId,
    }
    html = requests.post(url=url, data=data).json()
    if html['code'] == 1:
        return html['examList']
    else:
        print(html['msg'])
        exam_list(stuId)


def answer(examid):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/onlineExam/previewOnlineExam'
    data = {
        'examId': examid
    }
    html = requests.post(url=url, data=data).json()['data']
    Rinse(html)


def main(stuid):
    exams = exam_list(stuid)
    index = 1
    for i in exams:
        print(f'【{index}】{i["title"]}\t{i["startDate"]}')
        index += 1
    target = exams[int(input("请输入序号：")) - 1]
    answer(target['examId'])


if __name__ == '__main__':
    main('')
