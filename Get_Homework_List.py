import requests


def get_homework_list(stuId, openClassId, courseOpenId):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/getHomeworkList_new'
    data = {
        'openClassId': openClassId,
        'courseOpenId': courseOpenId,
        'pageSize': '100',
        'page': '1',
        'stuId': stuId,
    }
    html = requests.post(url=url, data=data).json()
    if html['code'] == 1:
        index = 1
        for i in html['homeworkList']:
            print(f'【{index}】{i["title"]}\t{i["stuHomeworkState"]}')
            index += 1
        homework_index = int(input("请输入数字序号：")) - 1
        homeworkId = html['homeworkList'][homework_index]['homeworkId']
        homeworkTermTimeId = html['homeworkList'][homework_index]['homeworkTermTimeId']
        return {
            'homeworkId': homeworkId,
            'homeworkTermTimeId': homeworkTermTimeId
        }
    else:
        return 0


if __name__ == '__main__':
    openClassId = ''
    courseOpenId = ''
    stuId = ''
    get_homework_list(stuId, openClassId, courseOpenId)
