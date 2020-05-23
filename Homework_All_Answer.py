import json

import requests

from Get_All_Course import get_all_course


def main(stuid):
    info = get_all_course(stuid)
    url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/getHomeworkList_new'
    data = {
        'openClassId': info['openClassId'],
        'courseOpenId': info['courseOpenId'],
        'pageSize': '100',
        'page': '1',
        'stuId': stuid,
    }
    html = requests.post(url=url, data=data).json()
    for k in html['homeworkList']:
        url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/previewHomework'
        data = {
            'homeWorkId': k['homeworkId']
        }
        html = requests.post(url=url, data=data).json()['data']
        title = html['title']
        with open(f'{title}.txt', 'w', encoding='utf8') as f:
            for i in html['questions']:
                f.write(f'{int(i["sortOrder"]) + 1},{i["title"]}\n')
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
                        f.write(f'{select},{j["Content"]}\n')
                    answer = i["answer"].replace('0', 'A').replace('1', 'B').replace('2', 'C').replace('3',
                                                                                                       'D').replace(
                        '4', 'E').replace('5', 'F').replace('6', 'G').replace('7', 'H').replace('8', 'I')
                    f.write(f'Answer:{answer}\n')
                except:
                    pass
            print(f'{title}已下载')
    input("作业答案已生成在软件目录下。请回车退出")


if __name__ == '__main__':
    main('')
