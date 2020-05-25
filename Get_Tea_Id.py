import requests


def getteaid(openClassId, courseOpenId):
    url = 'https://zjy2.icve.com.cn/api/study/courseIndex/courseIndex'
    data = {
        "courseOpenId": courseOpenId,
        "openClassId": openClassId
    }
    teaid = requests.post(url=url, data=data).json()["openClassInfo"]["CreatorId"]
    return teaid
