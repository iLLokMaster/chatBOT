import sqlite3
import os
import random
import webbrowser
import time

debug = 0  # set 1 to turn on debug
DataBaseSQL3inCode = sqlite3.connect("DataBaseInFiles")  # connect Data Base
cursor = DataBaseSQL3inCode.cursor()  # create cursor
try:
    cursor.execute("SELECT * FROM AnsvQest")
except sqlite3.Error:
    cursor.execute("""CREATE TABLE AnsvQest (
            answer city,
            qestion city
        )""")  # create table ###perform only for the first time
    cursor.execute("INSERT INTO AnsvQest VALUES ('привет', "
                   "'Привет, как у тебя дела?')")
db = cursor.execute("SELECT * FROM AnsvQest").fetchall()  # select all from Data Base and insert to db
DataBaseSQL3inCode.commit()  # commit changes and cloce Data Base


# calculation of the percentage of coincidence of the question from the database and the user's question
def per_com(list1, list2):
    common_elements = set(list1) & set(list2)
    percent_match = (len(common_elements) / len(set(list1 + list2))) * 100
    return percent_match


def recp(prompt):
    global result_of_percentage
    persentage_of_match = []
    prompt = prompt.lower()  # pr = re.sub('\W+',' ', pr )
    for k in range(len(db)):
        result_of_percentage = per_com(prompt, db[k][0])  # result = проценты совпадения
        persentage_of_match.append([result_of_percentage, db[k][1]])
    sort_pers = sorted(persentage_of_match)
    if result_of_percentage == 0:
        print('Я вас не понял. Скажите ответ на ваш вопрос.(\n')
        text = input()
        if text != '':
            print(text)
            cursor.execute(f"INSERT INTO AnsvQest VALUES ('{prompt}', '{text}')")
            DataBaseSQL3inCode.commit()
            db.append([prompt, text])
            chat()
    else:
        print('Ответ бота:')
        a = sort_pers[-1][1]
        b = list(a)
        for alphabet in b:
            print(alphabet, end = '')
            time.sleep(0.01)
        print('\n')
        if sort_pers[-1][0] != 100:
            print('вам понравился ответ?[да][нет]')
            text = input()
            if text != '':
                print(text)
                if text.lower() == 'нет':
                    print('ваш вариант ответа')
                    text = input()
                    if text != '':
                        print(text)
                        print('\n')
                        cursor.execute(f"INSERT INTO AnsvQest VALUES ('"
                                        f"{prompt}', "
                                        f"'{text}'")
                        DataBaseSQL3inCode.commit()
                        db.append([prompt, text])
                        chat()
                    # print(db)
                elif text.lower() == 'да':
                    cursor.execute(f"INSERT INTO AnsvQest VALUES ('"
                                   f"{prompt}', "
                                   f"'{sort_pers[-1][1]}')")
                    DataBaseSQL3inCode.commit()
                    db.append([prompt, sort_pers[-1][1]])
                    chat()


def chat():
    compleat = ['готово кмдр!\n', 'готово CMDR!\n', 'рад помочь!\n', 'держи!\n', 'лови!\n', 'compleat!\n',
                'есть, сер!!!\n', 'вот держите, сер!\n', 'включаю\n', 'на\n', 'выполняю\n', 'сер, да, сер\n']
    while True:
        text = input()
        if text == 'exit' or text == 'выход':
            print(text)
            good_by = ['почему ты меня бросаешь? не надо, пожалуйста.(котик с блестящими глазками)', 'пока',
                       'Приходите пожалуйста поскорее. Я по вам уже скучаю:(', 'не оставляйте меня одного на долго',
                       'нееееееее...', 'не оставляй меня на долго, пожалуйста, я очень тебя прошу']
            print(random.choice(good_by))
            exit()
        elif text in ['db', 'data base', 'your data base', 'твоя база данных', 'база данных']:
            print(text)
            for h in range(len(db)):
                print(db[h], end = '\n')
        elif text == 'что ты умеешь':
            print(text)
            print('я умею отвечать на вопросы и постоянно обучаюсь, но не поддерживаю режим диалога. '
                  'Мои программисты под контролем Прядиева Романа, '
                  'очень стараются для продвижения проекта, и постоянно его поддерживают. '
                  'Если вам угодно, вы можете обновить программу(https://github.com/iLLokMaster/chatBOT)')
            print(text)
            os.system('C:/Users/B-ZONE/AppData/Local/Yandex/YandexBrowser/Application/browser.exe')
            print(random.choice(compleat))
        else:
            print(text)
            recp(text)


chat()