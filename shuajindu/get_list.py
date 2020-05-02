import random
import time
import requests


def get_all():
    url = 'https://zjyapp.icve.com.cn/newmobileapi/assistTeacher/getModuleListByClassId'
    data = {
        'courseOpenId': '4s4gar6qiank7g3k15kiyw',
        'openClassId': 'pkcravurd4zfoouox04m5a',
        'stuId': 'midwaoaqv6xmebkkd0czew',
    }
    html = requests.post(url=url, data=data).json()
    data = html['moduleList']
    moduleIds = []
    for i in data:
        print(i['moduleName'] + '已加载')
        moduleIds.append(i['moduleId'])
    return moduleIds


def get_list(moduleId):
    url = 'https://zjy2.icve.com.cn/newmobileapi/assistTeacher/getTopicListByModuleId'
    moduleIds = []
    for i in moduleId:
        data = {
            'openClassId': 'pkcravurd4zfoouox04m5a',
            'courseOpenId': '4s4gar6qiank7g3k15kiyw',
            'moduleId': f'{i}'
        }
        html = requests.post(url=url, data=data).json()
        data = html['topicList']
        for j in data:
            moduleIds.append(j['topicId'])
    return moduleIds


def get_cell(topicIds):
    url = 'https://zjy2.icve.com.cn/newmobileapi/assistTeacher/getCellListByTopicId'
    cellids = []

    for k in topicIds:
        data = {
            'openClassId': 'pkcravurd4zfoouox04m5a',
            'courseOpenId': '4s4gar6qiank7g3k15kiyw',
            'topicId': k,
            'stuId': 'midwaoaqv6xmebkkd0czew'
        }
        html = requests.post(url=url, data=data).json()
        data = html['cellList']
        for i in data:
            if i['categoryName'] == '子节点':
                for j in i['cellChildNodeList']:
                    cellids.append(j['cellId'])
            else:
                cellids.append(i['cellId'])
    return cellids


def panta(cellids):
    url = 'https://zjy2.icve.com.cn/api/common/Directory/stuProcessCellLog'
    headers = {
        'Cookie': 'Hm_lvt_a3821194625da04fcd588112be734f5b=1587975517; '
                  'Hm_lpvt_a3821194625da04fcd588112be734f5b=1587975517; '
                  'acw_tc=2f624a4b15879755165498696e7b089c18b79ff17c8104a23d59a207444551; '
                  'verifycode=610A50DA6E3B739EA8256AB8E7615A6E@637236014613487854; '
                  'auth'
                  '=0102511C7A6684EAD708FE512C2638D8EAD7080115740071003300770061006F00610071006F007A0070006A007200700033006D006A00760075007600770000012F00FF950843DF1F22D35EB1920F74B53CE306163BB96C; token=zgmoaaqrx6pduyjnythrq',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.122 Safari/537.36',
    }
    for i in cellids:
        data = {
            'courseOpenId': '4s4gar6qiank7g3k15kiyw',
            'openClassId': 'pkcravurd4zfoouox04m5a',
            'cellId': i,
            'cellLogId': '',
            'picNum': '0',
            'studyNewlyTime': random.randint(1000, 2000),
            'studyNewlyPicNum': random.randint(30, 40),
            'token': 'zgmoaaqrx6pduyjnythrq',
        }
        html = requests.post(url=url, headers=headers, data=data).json()
        time.sleep(random.randint(1, 5))
        print(html)


if __name__ == '__main__':
    moduleId_list = get_all()
    topid = get_list(moduleId_list)
    cellids = get_cell(topid)
    panta(cellids)
