import json
import time
import re
import requests

from Get_All_Course import get_all_course


def main(stuid, schoolid):
    allcourse = get_all_course(stuid)
    courseOpenId = allcourse['courseOpenId']
    url = 'https://zjyapp.icve.com.cn/newmobileapi/coursequestion/getCourseQuestionList'
    data = {
        'schoolId': schoolid,
        'courseOpenId': courseOpenId,
        'limit': '1000',
    }
    html = requests.post(url=url, data=data).json()
    if html['code'] == 1:
        questionlist = html['questionList']
        filename = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
        with open(f'{filename}.txt', 'w', encoding='utf8') as f:
            for i in questionlist:
                Qusetion_title = i["title"]
                Qusetion_title = Qusetion_title.replace('<p>', '').replace('</p>', '').replace('</span>', '').replace(
                    '<br/>', '').replace('&nbsp;', '')
                Qusetion_title = re.sub('<.*?>', "", Qusetion_title)
                f.write(f'{Qusetion_title}\n')
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
            print(f"{filename}已下载")


if __name__ == '__main__':
    schoolid = ''
    stuid = ''
    main(stuid, schoolid)
