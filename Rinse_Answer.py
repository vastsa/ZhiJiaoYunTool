import json
import time


def Rinse(PreviewList):
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
    if str(PreviewList).find('<img') > 0:
        hhf = '<br />'
        kzm = '.html'
    else:
        hhf = '\n'
        kzm = '.txt'
    title = PreviewList["title"]
    questions = PreviewList['questions']
    index = 1

    for item in questions:
        Title = item['title']
        dataJson = item['dataJson']
        try:
            with open(f"{title}" + kzm, "a", encoding="utf-8") as file:
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
                    # file.write('题目' + str(index) + ':' + Title + '\n' + '单选题答案：' + dataJson + '\n\n')
                    file.write('题目' + str(index) + ':' + Title + hhf + Contents + hhf + hhf)
                    # file.write('题目' + str(index) + ':' + Title + '\n\n' + '单选题答案：' + dataJson + '\n\n')
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

                    # file.write('题目' + str(index) + ':' + Title + '\n' + '多选题答案：' + dataJson + '\n\n')
                    file.write('题目' + str(index) + ':' + Title + hhf + Contents + hhf + hhf)
                if item['queTypeName'] == "判断题":
                    x = item['answer'].replace('0', '错').replace('1', '对').replace('2', '').replace('3', '')
                    file.write('题目' + str(index) + ':' + Title + hhf + hhf + "判断题答案：" + x + '\n\n')
                if item['queTypeName'] == "问答题":
                    y = item['answer'].replace('&nbsp;', ' ')
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
    time.sleep(3)
    print("答案已保存软件根目录下！")
    input('返回首页中。。。。。')
    from Main import main as menu
    menu()
