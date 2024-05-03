import sqlite3
import os
import random
import webbrowser
import json
import pyaudio
from vosk import Model, KaldiRecognizer
import time

debug = 0  # set 1 to turn on debug
DataBaseSQL3inCode = sqlite3.connect("DataBaseInFiles")  # connect Data Base
cursor = DataBaseSQL3inCode.cursor()  # create cursor
try:
    cursor.execute("SELECT * FROM AnsvQest")
except sqlite3.Error:
    cursor.execute("""CREATE TABLE AnsvQest (
            answer text,
            qestion text
        )""")  ###create table ###perform only for the first time
    cursor.execute("INSERT INTO AnsvQest VALUES ('привет', "
                   "'Привет, как у тебя дела?')")
db = cursor.execute("SELECT * FROM AnsvQest").fetchall()  ###select all from Data Base and insert to db
DataBaseSQL3inCode.commit()  ###commit changes and cloce Data Base

model = Model('models/model')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000)
stream.start_stream()
def listen():
    while True:
        data = stream.read(4000, exception_on_overflow = False)
        if rec.AcceptWaveform(data) and len(data) > 0:
            result = json.loads(rec.Result())
            if 'text' in result:
                yield result['text']
def per_com(list1,
            list2):  ###calculation of the percentage of coincidence of the question from the database and the user's question
    common_elements = set(list1) & set(list2)
    percent_match = (len(common_elements) / len(set(list1 + list2))) * 100
    return percent_match
def recp(prompt):
    pers = []
    pr = prompt
    pr = pr.lower()  # pr = re.sub('\W+',' ', pr )
    for k in range(len(db)):
        list_a = pr
        list_b = db[k][0]  # list_b = re.sub('\W+',' ', db[k][0] )
        result = per_com(list_a, list_b)  ###result = проценты совпадения
        pers.append([result, db[k][1]])
    sortPers = sorted(pers)
    if result == 0:
        print('Я вас не понял. Скажите ответ на ваш вопрос.(\n')
        for text in listen():
            otvet_polzovatelya = text
            if text != '':
                print(text)
        cursor.execute(f"INSERT INTO AnsvQest VALUES ('{prompt}', '{otvet_polzovatelya}')")
        DataBaseSQL3inCode.commit()
        db.append([prompt, otvet_polzovatelya])
    else:
        print('Ответ бота:')
        a = sortPers[-1][1]
        b = list(a)
        for alphabet in b:
            print(alphabet, end = '')
            time.sleep(0.01)
        print('\n')
        if sortPers[-1][0] != 100:
            print('вам понравился ответ?[да][нет]')

            for text in listen():
                if text != '':
                    print(text)

                    if text.lower() == 'нет':
                        print('ваш вариант ответа')
                        for text in listen():
                            if text != '':
                                print(text)
                                print('\n')
                                cursor.execute(
                                    f"INSERT INTO AnsvQest VALUES ('"
                                    f"{prompt}', "
                                    f"'{text}')"
                                )
                                DataBaseSQL3inCode.commit()
                                db.append([prompt, text])
                                chat()
                        # print(db)
                    elif text.lower() == 'да\n':
                        cursor.execute(f"INSERT INTO AnsvQest VALUES ('"
                                       f"{prompt}', "
                                       f"'{sortPers[-1][1]}')")
                        DataBaseSQL3inCode.commit()
                        db.append([prompt, sortPers[-1][1]])
                        chat()


def chat(chhat = 0):
    while True:
        print('говорите')
        for text in listen():
            prompt = text

            if prompt == '':
                pass
            elif prompt in ['режим игры', 'игры']:
                print(prompt)
                print('выберите игру [elite dangerous]')
                for text in listen():
                    if text in ['элитная опастность', 'элитной опасностью', 'элитное опасность', 'опасности', 'элитной опасность']:
                        print(text)
                        print('включаю')
                        #buttons
                    elif text == 'назад':
                        print(text)
                        pass

            elif prompt == 'exit' or prompt == 'выход':
                print(prompt)
                if debug == 1:
                    print('     сохраняем изменения в базе')
                if debug == 1:
                    try:
                        DataBaseSQL3inCode.close()
                        print('     изменения сохранены')
                    except sqlite3.Error as e:
                        print("     не удалось сохранить изменения")
                        error_code = e.args[0]
                        print(f"     Error code: {error_code}")
                good_by = [
                    'почему ты меня бросаешь? не надо, пожалуйста.(котик с блестящими глазками)', 'пока',
                    'Приходите пожалуйста поскорее. Я по вам уже скучаю:(',
                    'не оставляйте меня одного на долго', 'нееееееее...',
                    'не оставляй меня на долго, пожалуйста, я очень тебя прошу'
                ]
                print(good_by[random.randint(0, len(good_by) - 1)])
                exit()
            #elif prompt in ['заметки', 'идеи']:

            elif prompt in['db', 'ви', 'data base', 'your data base', 'твоя база данных', 'база данных']:
                print(prompt)
                if debug == 1:
                    for h in range(len(db)):
                        print(db[h])
            elif prompt == 'что ты умеешь':
                print(prompt)
                print('я умею отвечать на вопросы и постоянно обучаюсь, но не поддерживаю режим диалога. Мои программисты под контролем Прядиева Романа, очень стараются для продвижения проекта, и постоянно его поддерживают. Если вам угодно, вы можете обновить программу(https://github.com/iLLokMaster/chatBOT)')
            elif prompt in ['открой браузер', 'браузер']:
                print(prompt)
                os.system('C:/Users/B-ZONE/AppData/Local/Yandex/YandexBrowser/Application/browser.exe')
                print('на')
            elif prompt in ['домашняя работа', 'домашнюю работу']:
                print(prompt)
                webbrowser.open('https://dnevnik.ru/marks/school/1000009993521/student/1000012990748/current', new = 2)
                print('держи')
            elif prompt == 'открой игры':
                print(prompt)
                os.system('C:/Program Files (x86)/Steam/Steam.exe')
                print('на')
            elif prompt in ['телеграм', 'телеграмм']:
                print(text)
                print('открываю')
                webbrowser.open('https://web.telegram.org/', new = 2)
            elif prompt in ['чат', 'общение', 'к общению', 'в общении']:
                print('чат активирован')
                chhat = 1
            elif prompt in ['закрой чат', 'хватит общаться']:
                print('выключаю...')
                chhat = 0
            elif prompt in ['видео', 'я хочу посмотреть видео']:
                webbrowser.open('https://www.youtube.com/', new = 2)

            elif chhat == 1:
                print(prompt)
                recp(prompt)
            else:
                print(text)
                print('я вас не понял')
chat()