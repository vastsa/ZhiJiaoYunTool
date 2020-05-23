import json
import re
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
                pass
        input("作业答案已生成在软件目录下。请回车退出")


if __name__ == '__main__':
    main('')
