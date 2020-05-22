import requests

from Get_All_Course import get_all_course
from Get_Homework_List import get_homework_list


def retime(time, teaid, HomeWorkId, CourseOpenId, OpenClassId):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/coursehomework/saveHkTimeByOpenClass'
    data = {
        'data': f'{{"CreatorId":"{teaid}","CourseOpenId":"{CourseOpenId}","HomeWorkId":"{HomeWorkId}","StuEndDate":"{time}","OpenClassId":"{OpenClassId}"}}'
    }
    html = requests.post(url=url, data=data).json()
    print(f"{html['msg']}")
    input("回车后退出！")


def main(stuId):
    allcourse = get_all_course(stuId)
    openClassId = allcourse['openClassId']
    courseOpenId = allcourse['courseOpenId']
    time = input("请输入结束时间（格式2020-5-21)：")
    teaid = input("请输入教师ID（获取方法：www.lanol.cn)：")
    homeworklist = get_homework_list(stuId, openClassId, courseOpenId)
    homeworkId = homeworklist['homeworkId']
    retime(time, teaid, homeworkId, courseOpenId, openClassId)


if __name__ == '__main__':
    retime('2020-4-7', '', '', '',
           '')
    main('')
