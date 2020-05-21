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


def main(stuId):
    time = input("请输入结束时间（格式2020-5-21)：")
    teaid = input("请输入教师ID（获取方法：www.lanol.cn)：")
    allcourse = get_all_course(stuId)
    if allcourse == 0:
        print("获取失败")
    else:
        index = 1
        for i in allcourse:
            print(f"【{index}】{i['courseName']}\t{i['mainTeacherName']}")
            index += 1
        course_index = int(input("请输入数字序号：")) - 1
    openClassId = allcourse[course_index]['openClassId']
    courseOpenId = allcourse[course_index]['courseOpenId']
    homeworklist = get_homework_list(stuId, openClassId, courseOpenId)
    if homeworklist == 0:
        print("获取失败")
    else:
        index = 1
        for i in homeworklist:
            print(f'【{index}】{i["title"]}\t{i["stuHomeworkState"]}')
            index += 1
        homework_index = int(input("请输入数字序号：")) - 1
        homeworkId = homeworklist[homework_index]['homeworkId']
        retime(time, teaid, homeworkId, courseOpenId, openClassId)


if __name__ == '__main__':
    retime('2020-4-7', '', '', '',
           '')
    main('')
