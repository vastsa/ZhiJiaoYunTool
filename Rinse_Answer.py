import time
import json
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
    title = PreviewList["title"]
    questions = PreviewList['questions']
    index = 1

    for item in questions:
        Title = item['title']
        dataJson = item['dataJson']
        dataJsons = json.loads(item['dataJson'])
        with open(f"{title}.txt", "a", encoding="utf-8") as file:
            if item['queTypeName'] == "单选题":
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
                #file.write('题目' + str(index) + ':' + Title + '\n\n' + '单选题答案：' + dataJson + '\n\n')
            if item['queTypeName'] == "多选题":
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

                # file.write('题目' + str(index) + ':' + Title + '\n' + '多选题答案：' + dataJson + '\n\n')
                file.write('题目' + str(index) + ':' + Title + '\n' + Contents + '\n\n')
            if item['queTypeName'] == "判断题":
                x = item['answer'].replace('0', '错').replace('1', '对').replace('2', '').replace('3', '')
                file.write('题目' + str(index) + ':' + Title + '\n\n' + "判断题答案：" + x + '\n\n')
            if item['queTypeName'] == "问答题":
                y = item['answer'].replace('&nbsp;', ' ')
                file.write('题目' + str(index) + ':' + Title + '\n\n\n' + '问答题答案：' + y + '\n\n')
            index += 1
    time.sleep(3)
    print("答案已保存软件根目录下！")
    sele = input("【1】返回首页\n【2】返回上级\n请选择：")
    if sele == 2:
        Rinse(PreviewList)
    else:
        from Main import main as menu
        menu()
