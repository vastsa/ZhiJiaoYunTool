import pickle
import time
from configparser import ConfigParser

import requests

config = ConfigParser()
config.read('config.info')
time = time.strftime("%Y-%m-%d", time.localtime())
print(time)
data = {
    'stuId': config['information']['userid'],
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
