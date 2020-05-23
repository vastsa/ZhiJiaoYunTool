import time

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
    PreviewList = requests.post(url=url, data=data).json()
    if PreviewList['code'] == 1:
        questions = PreviewList['questionList']
        index = 1
        filename = time.strftime("%Y-%m-%d-%H-%M", time.localtime())
        for item in questions:
            Title = item['title'].replace('&nbsp;', '').replace('<p>', '').replace('</p>', '').replace('<strong>',
                                                                                                       '').replace(
                '</strong>', '').replace('<br/>', '')
            dataJson = item['dataJson'].replace('true', '：对').replace('false', '').replace('[', '').replace(']', '') \
                .replace('"', '').replace('SortOrder', '').replace('0', '').replace('1', '').replace('2', '').replace(
                '4', '').replace(
                '3', '') \
                .replace('Content', '').replace(':', '').replace('IsAnswer', '').replace(',', '  ').replace('&nbsp;',
                                                                                                            '')
            with open(f"{filename}.txt", "a", encoding="utf-8") as file:
                if item['queTypeName'] == "单选题":
                    file.write('题目' + str(index) + ':' + Title + '\n' + '单选题答案：' + dataJson + '\n\n')
                if item['queTypeName'] == "多选题":
                    file.write('题目' + str(index) + ':' + Title + '\n' + '多选题答案：' + dataJson + '\n\n')
                if item['queTypeName'] == "判断题":
                    x = item['answer'].replace('0', '错').replace('1', '对').replace('2', '').replace('3', '').replace(
                        '4', '')
                    file.write('题目' + str(index) + ':' + Title + '\n' + "判断题答案：" + x + '\n\n')
                if item['queTypeName'] == "问答题":
                    y = item['answer'].replace('&nbsp;', ' ')
                    file.write('题目' + str(index) + ':' + Title + '\n\n' + '问答题答案：' + y + '\n\n')
                index += 1
        time.sleep(3)
        print(f"{filename}已下载")
        input("请回车退出")
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
