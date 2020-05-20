# 补签模块
import requests
from Get_Class_Activity import get_activity
from Get_Day_Course import get_course


def main(stuid):
    print("【欢迎使用职教云补签助手】")
    print("                  By:Lan")
    date = input("请输入需要补签的日期如(2020-5-20)：")
    courses = get_course(stuid, date)
    if courses == 'no':
        print("你今天没有课，好好休息")
    else:
        print("Lan职教云助手提示您：\n您今天课表如下：")
        for i in range(len(courses['courseNmae'])):
            print(f'【{i + 1}】：{courses["classSection"][i]}{courses["courseNmae"][i]}')
        index = int(input("请输入你要改签的课程：")) - 1
        activities = get_activity(stuid, courses["courseId"][index], courses["openClassId"][index])
        buqianname = []
        buqianid = []
        for j in range(len(activities)):
            datatype = activities[j]['DataType']
            if datatype == "签到":
                buqianname.append(activities[j]['Title'])
                buqianid.append(activities[j]['Id'])
        for i in range(len(buqianid)):
            print(f'【{i}】{buqianname[i]}')
        target = int(input("请输入要逆天改命的序号："))
        datas = f'{{"OpenClassId":"{courses["openClassId"]}","Id":"{stuid}","SignId":"{buqianid[target]}","StuId":"{stuid}","SignResultType":1,"SourceType":2,"schoolId":"3-3sabgooohfboflpnx6bq"}}'
        xdata = {
            'data': f'{datas}'
        }
        bqurl = 'https://zjyapp.icve.com.cn/newmobileapi/faceteach/changeSignType'
        html = requests.post(url=bqurl,data=xdata).json()
        if html['code'] == 1:
            print(html['msg'])
            print("逆天改命成功，Lan's Blog：https://www.lanol.cn")
        else:
            print(html['msg'])
            print("逆天改命失败，请联系Lan")


if __name__ == '__main__':
    stuid = ''
    main(stuid)
