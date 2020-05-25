import requests


def get_all_course(stuid):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/student/getCourseList'
    data = {
        'stuId': stuid
    }
    html = requests.post(url=url, data=data).json()
    print(html)
    if html['code'] == 1:
        index = 1
        for i in html['dataList']:
            print(f"【{index}】{i['courseName']}\t{i['mainTeacherName']}")
            index += 1
        course_index = int(input("请输入数字序号：")) - 1
        openClassId = html['dataList'][course_index]['openClassId']
        courseOpenId = html['dataList'][course_index]['courseOpenId']
        return {
            'openClassId': openClassId,
            'courseOpenId': courseOpenId
        }
    else:
        return 0
