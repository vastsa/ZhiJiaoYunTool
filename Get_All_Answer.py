import time
import re
import json
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
    #PreviewList = requests.post(url=url, data=data).json()
    #先转为文本删除无效内容再转回去json处理
    PreviewListReq = requests.post(url=url, data=data).text
    PreviewListReq = PreviewListReq.replace('&nbsp;', '')
    PreviewListReq = re.sub('<.*?>', "", PreviewListReq)
    PreviewList = json.loads(PreviewListReq)

    if PreviewList['code'] == 1:
        questions = PreviewList['questionList']
        index = 1
        filename = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
        for item in questions:
            #Title = item['title'].replace('&nbsp;', '').replace('<p>', '').replace('</p>', '').replace('<strong>',
                                                                                                       #'').replace(
             #   '</strong>', '').replace('<br/>', '')
            Title = item['title']
            #Title = re.sub('<.*?>', "", Title)
            #dataJson = item['dataJson'].replace('true', '：对').replace('false', '').replace('[', '').replace(']', '') \
                #.replace('"', '').replace('SortOrder', '').replace('0', '').replace('1', '').replace('2', '').replace(
                #'4', '').replace(
                #'3', '') \
                #.replace('Content', '').replace(':', '').replace('IsAnswer', '').replace(',', '  ').replace('&nbsp;',
                                                                                                            #'')
            #dataJson = re.sub('<.*?>', "", dataJson)
            dataJson = item['dataJson']
            try:
                with open(f"{filename}.txt", "a", encoding="utf-8") as file:
                    if item['queTypeName'] == "单选题":
                        dataJsons = json.loads(item['dataJson'])
                        Contents = ''
                        for SortOrder_i in range(len(dataJsons)):
                            tihao = tihuana[str(dataJsons[SortOrder_i]['SortOrder'])]
                            Content = dataJsons[SortOrder_i]['Content']
                            if dataJsons[SortOrder_i]['IsAnswer'] == True:
                                key = '单选题答案:' + tihao + '.' + Content
                            Contents = Contents + tihao + '.' + Content + '\n'
                        Contents = Contents + key
                    #file.write('题目' + str(index) + ':' + Title + '\n' + '单选题答案：' + dataJson + '\n\n')
                        file.write('题目' + str(index) + ':' + Title + '\n' + Contents + '\n\n')
                    if item['queTypeName'] == "多选题":
                        dataJsons = json.loads(item['dataJson'])
                        Contents = ''
                        key = '多选题答案:'
                        for SortOrder_i in range(len(dataJsons)):
                            tihao = tihuana[str(dataJsons[SortOrder_i]['SortOrder'])]
                            Content = dataJsons[SortOrder_i]['Content']
                            if dataJsons[SortOrder_i]['IsAnswer'] == True:
                                key = key + tihao + '.' + Content + ','
                            Contents = Contents + tihao + '.' + Content + '\n'
                        if key[-1] == ',':
                            key = key[0:-1]
                        Contents = Contents + key
                        #file.write('题目' + str(index) + ':' + Title + '\n' + '多选题答案：' + dataJson + '\n\n')
                        file.write('题目' + str(index) + ':' + Title + '\n' + Contents + '\n\n')
                    if item['queTypeName'] == "判断题":
                        x = item['answer'].replace('0', '错').replace('1', '对').replace('2', '').replace('3', '').replace(
                            '4', '')
                        file.write('题目' + str(index) + ':' + Title + '\n' + "判断题答案：" + x + '\n\n')
                    if item['queTypeName'] == "问答题":
                        y = item['answer']
                        file.write('题目' + str(index) + ':' + Title + '\n\n' + '问答题答案：' + y + '\n\n')
                    if item['queTypeName'] == "填空题(客观)":
                        y = item['answer']
                        file.write('题目' + str(index) + ':' + Title + '\n\n' + '填空题(客观)答案：' + y + '\n\n')
                    index += 1
            except json.JSONDecodeError as e:
                print(PreviewList)
                pass
        #time.sleep(3)
        print(f"{filename}已下载")
        print("答案已保存软件根目录下！")
        main(stuid, schoolid)
        # questionlist = html['questionList']
        # filename = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
        # with open(f'{filename}.txt', 'w', encoding='utf8') as f:
        #     for i in questionlist:
        #         Qusetion_title = i["title"]
        #         Qusetion_title = Qusetion_title.replace('<p>', '').replace('</p>', '').replace('</span>', '').replace(
        #             '<br/>', '').replace('&nbsp;', '')
        #         Qusetion_title = re.sub('<.*?>', "", Qusetion_title)
        #         f.write(f'{Qusetion_title}\n')
        #         try:
        #             selects = json.loads(i['dataJson'])
        #             for j in selects:
        #                 tihuan = {
        #                     '0': 'A',
        #                     '1': 'B',
        #                     '2': 'C',
        #                     '3': 'D',
        #                     '4': 'E',
        #                     '5': 'F',
        #                 }
        #                 select = tihuan[str(j['SortOrder'])]
        #                 content = j["Content"]
        #                 content = content.replace('&nbsp;', '')
        #                 f.write(f'{select},{content}\n')
        #             answer = i["answer"].replace('0', 'A').replace('1', 'B').replace('2', 'C').replace('3',
        #                                                                                                'D').replace(
        #                 '4', 'E').replace('5', 'F').replace('6', 'G').replace('7', 'H').replace('8', 'I')
        #             f.write(f'Answer:{answer}\n')
        #         except:
        #             pass
        #     print(f"{filename}已下载")


if __name__ == '__main__':
    schoolid = ''
    stuid = ''
    main(stuid, schoolid)
