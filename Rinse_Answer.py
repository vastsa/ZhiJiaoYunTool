import time


def Rinse(PreviewList):
    title = PreviewList["title"]
    questions = PreviewList['questions']
    index = 1
    for item in questions:
        Title = item['title'].replace('&nbsp;', '').replace('<p>', '').replace('</p>', '').replace('<strong>',
                                                                                                   '').replace(
            '</strong>', '').replace('<br/>', '')
        dataJson = item['dataJson'].replace('true', '：对').replace('false', '').replace('[', '').replace(']', '') \
            .replace('"', '').replace('SortOrder', '').replace('0', '').replace('1', '').replace('2', '').replace('3',
                                                                                                                  '') \
            .replace('Content', '').replace(':', '').replace('IsAnswer', '').replace(',', '  ').replace('&nbsp;', '')

        with open(f"D:/{title}.txt", "a", encoding="utf-8") as file:
            if item['queTypeName'] == "单选题":
                file.write('题目' + str(index) + ':' + Title + '\n\n' + '单选题答案：' + dataJson + '\n\n')
            if item['queTypeName'] == "多选题":
                file.write('题目' + str(index) + ':' + Title + '\n\n' + '多选题答案：' + dataJson + '\n\n')
            if item['queTypeName'] == "判断题":
                x = item['answer'].replace('0', '错').replace('1', '对').replace('2', '').replace('3', '')
                file.write('题目' + str(index) + ':' + Title + '\n\n' + "判断题答案：" + x + '\n\n')
            if item['queTypeName'] == "问答题":
                y = item['answer'].replace('&nbsp;', ' ')
                file.write('题目' + str(index) + ':' + Title + '\n\n\n' + '问答题答案：' + y + '\n\n')
            index += 1
    time.sleep(3)
    print("答案已保存软件根目录下！")
    input("请回车退出")
