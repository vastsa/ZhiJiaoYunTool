import requests

from Get_All_Course import get_all_course
from Get_Homework_Grade import get_homework_grade
from Get_Homework_List import get_homework_list


def re_grade(stuid, getScore):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/readFileHomework'
    data = {
        'homeworkStuId': stuid,
        'getScore': getScore,
        'sourceType': '2',
    }
    html = requests.post(url=url, data=data).json()
    return html['msg']


def Main(stuId):
    print("注意：改分只可以改非题库作业，需要老师批阅的")
    allcourse = get_all_course(stuId)
    openClassId = allcourse['openClassId']
    courseOpenId = allcourse['courseOpenId']
    homeworklist = get_homework_list(stuId, openClassId, courseOpenId)
    if homeworklist == 0:
        print("获取失败")
    else:
        homeworkTermTimeId = homeworklist['homeworkTermTimeId']
        homeworkId = homeworklist['homeworkId']
        grades = get_homework_grade(openClassId, homeworkId, stuId, homeworkTermTimeId)
        if grades != 0:
            index = 1
            for i in grades:
                print(f"【{index}】时间：{i['dateCreated']}\t分数{i['getScore']}")
                index += 1
            target = int(input("请输入要修改的序号：")) - 1
            if target > len(grades):
                print("请输入正确的序号")
                target = int(input("请输入要修改的序号：")) - 1
            homeworkStuId = grades[target]['homeworkStuId']
            getScore = int(input("请输入目标分数（整数）："))
            result = re_grade(homeworkStuId, getScore)
            print(result)
            input("回车后返回首页！")
            from Main import main as menu
            menu()
        else:
            Main(stuId)
            input("回车后返回首页！")
            from Main import main as menu
            menu()


if __name__ == '__main__':
    Main('')
