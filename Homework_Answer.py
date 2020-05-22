import json

import requests

from Get_All_Course import get_all_course
from Get_Homework_List import get_homework_list


def main(stuid):
    info = get_all_course(stuid)
    homrwork_list = get_homework_list(stuid, info['openClassId'], info['courseOpenId'])
    homeworkId = homrwork_list['homeworkId']
    url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/previewHomework'
    data = {
        'homeWorkId': homeworkId
    }
    html = requests.post(url=url, data=data).json()['data']
    title = html['title']
    with open(f'{title}.txt', 'w', encoding='utf8') as f:
        for i in html['questions']:
            f.write(f'{int(i["sortOrder"]) + 1},{i["title"]}\n')
            try:
                for j in json.loads(i['dataJson']):
                    select = j["SortOrder"]
                    if select == 0:
                        select = 'A'
                    elif select == 1:
                        select = 'B'
                    elif select == 2:
                        select = 'C'
                    elif select == 3:
                        select = 'D'
                    f.write(f'{select},{j["Content"]}\n')
                answer = i["answer"].replace('0', 'A').replace('1', 'B').replace('2', 'C').replace('3', 'D')
                f.write(f'Answer:{answer}\n')
            except:
                pass
        input("作业答案已生成在软件目录下。请回车退出")


if __name__ == '__main__':
    main('')
