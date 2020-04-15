import pickle
import time
import requests
from configparser import ConfigParser

config = ConfigParser()
config.read('config.info')
time = time.strftime("%Y-%m-%d", time.localtime())
print(time)
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '107',
    'Host': 'zjyapp.icve.com.cn',
    'Connection': 'close',
    'Accept-Encoding': 'gzip, deflate',
    'User-Agent': 'okhttp/3.10.0',
}
data = {
    'stuId': config['information']['userid'],
    'faceDate': time
}
with open('cookies', 'rb') as f:
    cookie = pickle.load(f)
url = 'https://zjyapp.icve.com.cn/newmobileapi/faceteach/getStuFaceTeachList'
html = requests.post(url=url, headers=headers, data=data).json()
datalist = html['dataList']
courses = len(datalist)
courseId = []
courseNmae = []
classSection = []
openClassId =[]
for i in range(courses):
    courseNmae.append(datalist[i]['courseName'])
    courseId.append(datalist[i]['Id'])
    classSection.append(datalist[i]['classSection'])
    openClassId.append(datalist[i]['openClassId'])
