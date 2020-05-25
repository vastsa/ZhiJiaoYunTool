import requests

from Get_All_Course import get_all_course
from Get_Exam_List import main as exam_list
from Get_Tea_Id import getteaid

def main(stuId):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/onlineExam/saveExamTimeInfo?data='
    allcourse = get_all_course(stuId)
    openClassId = allcourse['openClassId']
    courseOpenId = allcourse['courseOpenId']
    exams = exam_list(openClassId, courseOpenId, stuId)
    index = 1
    for i in exams:
        print(f'【{index}】{i["title"]}\t{i["startDate"]}')
        index += 1
    target = exams[int(input("请输入序号：")) - 1]
    examId = target['examId']
    examTermTimeId = target['examTermTimeId']
    print("时间注意切换到英文输入！")
    starttime = input("请输入开始时间（2020-03-20 00:00:00）：")
    endtime = input("请输入结束时间（2020-03-20 00:00:00）：")
    teaid = getteaid(openClassId, courseOpenId)
    xdata = f'{{"Id":"{examTermTimeId}","CreatorId":"{teaid}","OpenClassId":"{openClassId}","ExamId":"{examId}","StuStartDate":"{starttime}","StuEndDate":"{endtime}"}}'
    result_url = url + xdata
    result = requests.post(url=result_url).json()
    print(result['msg'])
    input("回车后返回首页！")
    from Main import main as menu
    menu()


if __name__ == '__main__':
    main('')
