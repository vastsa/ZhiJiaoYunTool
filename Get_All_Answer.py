import json
import re
import time

import requests

from Get_All_Course import get_all_course


def main(stuid, schoolid):
    allcourse = get_all_course(stuid)
    print(allcourse)
    courseOpenId = allcourse['courseOpenId']
    url = 'https://zjyapp.icve.com.cn/newmobileapi/coursequestion/getCourseQuestionList'
    data = {
        'schoolId': schoolid,
        'courseOpenId': courseOpenId,
        'limit': '1000',
    }
    tihuana = {
        '0': 'A',
        '1': 'B',
        '2': 'C',
        '3': 'D',
        '4': 'E',
        '5': 'F',
        '6': 'G',
        '7': 'H',
        '8': 'I',
    }
    # PreviewList = requests.post(url=url, data=data).json()
    # 先转为文本删除无效内容再转回去json处理
    PreviewListReq = requests.post(url=url, data=data).text
    PreviewListReq = PreviewListReq.replace('&nbsp;', '').replace('</span>', '').replace('</p>', '').replace('</font>',
                                                                                                             '').replace(
        '<strong>', '').replace('</strong>', '').replace('<b>', '').replace('</b>', '').replace('<div>', '').replace(
        '</div>', '').replace('<br>', '').replace('<br/>', '')
    PreviewListReq = re.sub('<p.*?>', "", PreviewListReq)
    PreviewListReq = re.sub('<span.*?>', "", PreviewListReq)
    PreviewListReq = re.sub('<font.*?>', "", PreviewListReq)
    PreviewList = json.loads(PreviewListReq)
    if PreviewListReq.find('<img') > 0:
        hhf = '<br />'
        kzm = '.html'
    else:
        hhf = '\n'
        kzm = '.txt'

    if PreviewList['code'] == 1:
        questions = PreviewList['questionList']
        index = 1
        filename = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
        for item in questions:
            Title = item['title']
            try:
                with open(f"{filename}" + kzm, "a", encoding="utf-8") as file:
                    if item['queTypeName'] == "单选题":
                        dataJsons = json.loads(item['dataJson'])
                        Contents = ''
                        for SortOrder_i in range(len(dataJsons)):
                            tihao = tihuana[str(dataJsons[SortOrder_i]['SortOrder'])]
                            Content = dataJsons[SortOrder_i]['Content']
                            if dataJsons[SortOrder_i]['IsAnswer'] == True:
                                key = '单选题答案:' + tihao + '.' + Content
                            Contents = Contents + tihao + '.' + Content + hhf
                        Contents = Contents + key
                        file.write('题目' + str(index) + ':' + Title + hhf + Contents + hhf + hhf)
                    if item['queTypeName'] == "多选题":
                        dataJsons = json.loads(item['dataJson'])
                        Contents = ''
                        key = '多选题答案:'
                        for SortOrder_i in range(len(dataJsons)):
                            tihao = tihuana[str(dataJsons[SortOrder_i]['SortOrder'])]
                            Content = dataJsons[SortOrder_i]['Content']
                            if dataJsons[SortOrder_i]['IsAnswer'] == True:
                                key = key + tihao + '.' + Content + ','
                            Contents = Contents + tihao + '.' + Content + hhf
                        if key[-1] == ',':
                            key = key[0:-1]
                        Contents = Contents + key
                        file.write('题目' + str(index) + ':' + Title + hhf + Contents + '\n\n')
                    if item['queTypeName'] == "判断题":
                        x = item['answer'].replace('0', '错').replace('1', '对').replace('2', '').replace('3',
                                                                                                        '').replace(
                            '4', '')
                        file.write('题目' + str(index) + ':' + Title + hhf + hhf + "判断题答案：" + x + hhf + hhf)
                    if item['queTypeName'] == "问答题":
                        y = item['answer']
                        file.write('题目' + str(index) + ':' + Title + hhf + hhf + '问答题答案：' + y + hhf + hhf)
                    if item['queTypeName'] == "填空题(客观)":
                        y = item['answer']
                        file.write('题目' + str(index) + ':' + Title + hhf + hhf + '填空题(客观)答案：' + y + hhf + hhf)
                    if item['queTypeName'] == '填空题(主观)':
                        y = item['answer']
                        file.write('题目' + str(index) + ':' + Title + '\n\n' + '填空题(主观)答案：' + y + '\n\n')
                    index += 1
            except json.JSONDecodeError as e:
                print(PreviewList)
                pass
        print(f"{filename}已下载")
        print("答案已保存软件根目录下！")
        input("回车后返回首页！")
        from Main import main as menu
        menu()


if __name__ == '__main__':
    schoolid = ''
    stuid = ''
    main(stuid, schoolid)
