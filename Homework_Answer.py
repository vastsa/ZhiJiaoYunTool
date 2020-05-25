import requests
import re
import json

from Get_All_Course import get_all_course
from Get_Homework_List import get_homework_list
from Rinse_Answer import Rinse


def main(stuid):
    info = get_all_course(stuid)
    homrwork_list = get_homework_list(stuid, info['openClassId'], info['courseOpenId'])
    homeworkId = homrwork_list['homeworkId']
    url = 'https://zjyapp.icve.com.cn/newmobileapi/homework/previewHomework'
    data = {
        'homeWorkId': homeworkId
    }
    html = requests.post(url=url, data=data).text
    html = html.replace('&nbsp;', '').replace('</span>', '').replace('</p>', '').replace('</font>', '').replace('<strong>', '').replace('</strong>', '').replace('<b>', '').replace('</b>', '').replace('<div>','').replace('</div>','').replace('<br>','').replace('<br/>','')
    html = re.sub('<p.*?>', "", html)
    html = re.sub('<span.*?>', "", html)
    html = re.sub('<font.*?>', "", html)
    Rinse(json.loads(html)['data'])


if __name__ == '__main__':
    main('')
