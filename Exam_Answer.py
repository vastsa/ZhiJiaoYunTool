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
            Qusetion_title = i["title"]
            Qusetion_title = Qusetion_title.replace('<p>', '').replace('</p>', '').replace('</span>', '').replace(
                '<br/>', '').replace('&nbsp;', '')
            Qusetion_title = re.sub('<.*?>', "", Qusetion_title)
            f.write(f'{int(i["sortOrder"]) + 1},{Qusetion_title}\n')
            try:
                selects = json.loads(i['dataJson'])
                for j in selects:
                    tihuan = {
                        '0': 'A',
                        '1': 'B',
                        '2': 'C',
                        '3': 'D',
                        '4': 'E',
                        '5': 'F',
                    }
                    select = tihuan[str(j['SortOrder'])]
                    content = j["Content"]
                    content = content.replace('&nbsp;', '')
                    f.write(f'{select},{content}\n')
                answer = i["answer"].replace('0', 'A').replace('1', 'B').replace('2', 'C').replace('3',
                                                                                                   'D').replace(
                    '4', 'E').replace('5', 'F').replace('6', 'G').replace('7', 'H').replace('8', 'I')
                f.write(f'Answer:{answer}\n')
            except:
                answer = i["answer"].replace('0', 'A').replace('1', 'B').replace('2', 'C').replace('3',
                                                                                                   'D').replace(
                    '4', 'E').replace('5', 'F').replace('6', 'G').replace('7', 'H').replace('8', 'I')
                f.write(f'Answer:{answer}\n')
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
