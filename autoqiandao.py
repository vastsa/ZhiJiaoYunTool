import pickle
import time
import requests
import configparser
try :
    from get_datakecheng import courses, courseId, courseNmae, classSection, openClassId
except:
    import get_cookie

url = 'https://zjyapp.icve.com.cn/newmobileapi/faceteach/newGetStuFaceActivityList'
qdurl = 'https://zjyapp.icve.com.cn/newmobileapi/faceteach/saveStuSign'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '107',
    'Host': 'zjyapp.icve.com.cn',
    'Connection': 'close',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'okhttp/3.10.0',
}
# 读取配置文件
config = configparser.ConfigParser()
config.read('config.info')
stuId = config['information']['userid']  # 读取用户ID


# 获取今日课程
def get_datakecheng():
    print("【欢迎使用职教云自助签到助手】")
    print("                      By:Lan")
    print(f"同学你好，你今天共有{courses}节课")
    if courses != 0:
        print(f'课表如下：')
        js = 0
        for i in range(courses):
            print(f'【{js}】第{classSection[i]}课：{courseNmae[i]}')
            js += 1
        js = input("请输入你要监控的课堂：")
        return courseId[int(js)], openClassId[int(js)], courses
    else:
        print("同学，你今天无课，好好休息！")


def qiandao(signId, openClassId):
    qddata = {
        'signId': signId,
        'stuId': stuId,
        'classState': 2,
        'openClassId': openClassId
    }
    requests.post(url=qdurl, headers=headers, cookies=cookie, data=qddata)


# 获取课中活动
def get_kecheng():
    courseinformation = get_datakecheng()
    openClassId = courseinformation[1]
    courseId = courseinformation[0]
    data = {
        'activityId': courseId,
        'stuId': stuId,
        'classState': '2',
        'openClassId': openClassId
    }
    for i in range(180):
        html = requests.post(url=url, headers=headers, data=data, cookies=cookie).json()['dataList']
        js = 0
        for i in range(len(html)):
            datatype = html[i]['DataType']
            if datatype == "签到":
                state = html[i]['State']
                if state == 2:
                    signId = html[i]['Id']
                    js += 1
                    print("您当前有一个签到，正在尝试帮你签到，请稍等！")
                    try:
                        qiandao(signId, openClassId)
                        print("签到成功！，我要休息半小时")
                        time.sleep(1800)
                    except:
                        print("签到失败，正在重新签到")
                        qiandao(signId, openClassId)
        if js == 0:
            print(f"你好你当前不需要签到哦！", end="当前时间：")
            print(time.strftime("%H:%M:%S", time.localtime()))
            time.sleep(30)


# 先读取本地cookie，如果失败则在线登陆
if courses != 0:
    try:
        with open('cookies', 'rb') as f:
            cookie = pickle.load(f)
        get_kecheng()
    except:
        print("首次请登陆：")
        from get_cookie import cookies

        cookie = cookies
        get_kecheng()
else:
    print("今天放假，好好休息")
