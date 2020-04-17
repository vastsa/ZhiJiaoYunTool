from configparser import ConfigParser

import requests

config = ConfigParser()
config.read('config.info')
try:
    stuid = config['information']['userid']
except:
    import get_cookie


def get_kecheng(time):
    data = {
        'stuId': stuid,
        'faceDate': time
    }
    url = 'https://zjyapp.icve.com.cn/newmobileapi/faceteach/getStuFaceTeachList'
    html = requests.post(url=url, data=data).json()
    datalist = html['dataList']
    courses = len(datalist)
    courseId = []
    courseNmae = []
    classSection = []
    openClassId = []
    for i in range(courses):
        courseNmae.append(datalist[i]['courseName'])
        courseId.append(datalist[i]['Id'])
        classSection.append(datalist[i]['classSection'])
        openClassId.append(datalist[i]['openClassId'])
    if courses != 0:
        print(f'课表如下：')
        js = 0
        for i in range(courses):
            print(f'【{js}】第{classSection[i]}课：{courseNmae[i]}')
            js += 1
        js = input("请输入你要补签的课堂：")
        return {
            'courseId': courseId[int(js)],
            'openClassId': openClassId[int(js)],
            'courses': courses
        }
    else:
        print("同学，你今天无课，好好休息！")


def buqian(course):
    url = 'https://zjyapp.icve.com.cn/newmobileapi/faceteach/newGetStuFaceActivityList'
    data = {
        'activityId': course['courseId'],
        'stuId': stuid,
        'classState': '2',
        'openClassId': course['openClassId']
    }
    html = requests.post(url=url, data=data).json()['dataList']
    buqianname = []
    buqianid = []
    for j in range(len(html)):
        datatype = html[j]['DataType']
        if datatype == "签到":
            buqianname.append(html[j]['Title'])
            buqianid.append(html[j]['Id'])
    for i in range(len(buqianid)):
        print(f'【{i}】{buqianname[i]}')
        # print(f'【{i}】{buqianid[i]}')
    target = int(input("请输入要逆天改命的序号："))
    datas = f'{{"OpenClassId":"{course["openClassId"]}","Id":"{stuid}","SignId":"{buqianid[target]}","StuId":"{stuid}","SignResultType":1,"SourceType":2,"schoolId":"3-3sabgooohfboflpnx6bq"}}'
    xdata = {
        'data': f'{datas}'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'zjyapp.icve.com.cn',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.10.0',
    }
    bqurl = 'https://zjyapp.icve.com.cn/newmobileapi/faceteach/changeSignType'
    html = requests.post(url=bqurl, headers=headers, data=xdata).json()
    if html['code'] == 1:
        print(html['msg'])
        print("逆天改命成功，返回菜单")
        menu()
    else:
        print(html['msg'])
        print("逆天改命失败，请联系Lan")


def menu():
    print("【欢迎使用职教云补签助手】")
    print("                  By:Lan")
    date = input("请输入需要补签的日期如(2020-4-17)：")
    course = get_kecheng(date)
    buqian(course)

if __name__ == '__main__':
    menu()

