import requests

from Get_All_Course import get_all_course
from Get_Homework_Grade import get_homework_grade
from Get_Homework_List import get_homework_list


def re_grade(teaId, stuid, getScore):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/readFileHomework'
    data = {
        'teaId': teaId,
        'homeworkStuId': stuid,
        'getScore': getScore,
        'sourceType': '2',
    }
    html = requests.post(url=url, data=data).json()
    return html['msg']


def Main(stuId):
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
        homeworkTermTimeId = homeworklist[homework_index]['homeworkTermTimeId']
        grades = get_homework_grade(openClassId, homeworkId, stuId, homeworkTermTimeId)
        if grades != 0:
            index = 1
            for i in grades:
                print(f"【{index}】时间：{i['dateCreated']}\t分数{i['getScore']}")
                index += 1
            target = int(input("请输入要修改的序号：")) - 1
            homeworkStuId = grades[target]['homeworkStuId']
            getScore = int(input("请输入目标分数（整数）："))
            result = re_grade(homeworkStuId, getScore)
            print(result)
            input("回车键后退出")
        else:
            input("回车键后退出")


if __name__ == '__main__':
    Main('')
