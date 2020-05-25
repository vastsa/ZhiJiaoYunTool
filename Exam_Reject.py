import requests

from Get_All_Course import get_all_course
from Get_Exam_List import main as exams


def examlist(stuid):
    courses = get_all_course(stuid)
    openClassId = courses['openClassId']
    courseOpenId = courses['courseOpenId']
    exam_list = exams(openClassId, courseOpenId, stuid)
    index = 1
    for i in exam_list:
        print(f"【{index}】{i['title']}")
    target = int(input("请选择需要退回的考试：")) - 1
    examId = exam_list[target]['examId']
    examTermTimeId = exam_list[target]['examTermTimeId']
    url = 'https://zjyapp.icve.com.cn/newmobileapi/onlineExam/getReadStuList'
    data = {
        'courseOpenId': courseOpenId,
        'openClassId': openClassId,
        'examId': examId,
        'examTermTimeId': examTermTimeId,
    }
    html = requests.post(url=url, data=data).json()
    print(html['msg'])
    num = 0
    for i in html['examStuList']:
        if i['stuId'] == stuid:
            examStuId = i['examStuId']
            num = 1
    if num == 0:
        print("未发现你的试卷，请先提交")
        from Main import main as menu
        menu()
    reurl = 'https://zjyapp.icve.com.cn/newmobileapi/onlineExam/rejectExam'
    data = {
        'examStuId': examStuId
    }
    html = requests.post(url=reurl, data=data).json()
    input(html['msg'])
    from Main import main as menu
    menu()


if __name__ == '__main__':
    examlist('')
