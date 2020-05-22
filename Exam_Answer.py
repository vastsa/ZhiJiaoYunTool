import json

import requests

from Get_All_Course import get_all_course


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
        input("回车退出！")


def answer(examid, title):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/onlineExam/previewOnlineExam'
    data = {
        'examId': examid
    }
    html = requests.post(url=url, data=data).json()['data']
    with open(f'{title}.txt', 'w', encoding='utf8') as f:
        for i in html['questions']:
            f.write(f'{int(i["sortOrder"]) + 1},{i["title"]}\n')
            try:
                for j in json.loads(i['dataJson']):
                    f.write(f'{j["SortOrder"]},{j["Content"]}\n')
                f.write(f'Answer:{i["answer"]}\n')
            except:
                pass
    input("答案已生成在软件目录下。请回车退出")


def main(stuid):
    exams = exam_list(stuid)
    index = 1
    for i in exams:
        print(f'【{index}】{i["title"]}\t{i["startDate"]}')
        index += 1
    target = exams[int(input("请输入序号：")) - 1]
    answer(target['examId'], target['title'])


if __name__ == '__main__':
    main('')
