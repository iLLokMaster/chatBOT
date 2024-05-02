
import sqlite3
import os
import random
import webbrowser
import json
import pyaudio
from vosk import Model, KaldiRecognizer
import time
import winsound

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

model = Model('model')
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000)
stream.start_stream()
print('говорите')
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
            print(text)
            otvet_polzovatelya = text
            if text == '':
                break
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
                print(text)

            if text == '':
                pass
            elif text.lower() == 'нет':
                for text in listen():
                    print(text)
                    print('ваш ответ')

                    for text in listen():
                        print(text)
                        if text == '':
                            break
                    otvet_polzovatelya = text

                cursor.execute(
                    f"INSERT INTO AnsvQest VALUES ('"
                    f"{prompt}', "
                    f"'{otvet_polzovatelya}')"
                )
                DataBaseSQL3inCode.commit()
                db.append([prompt, otvet_polzovatelya])
                # print(db)
            elif text.lower() == 'да':
                cursor.execute(f"INSERT INTO AnsvQest VALUES ('"
                               f"{prompt}', "
                               f"'{sortPers[-1][1]}')")
                DataBaseSQL3inCode.commit()
                db.append([prompt, sortPers[-1][1]])


chat = 0
while True:
    for text in listen():
        print(text)
        prompt = text

        if prompt == '':
            pass
        elif chat == 1:
            recp(prompt)
        elif prompt in ['режим игры', 'игры']:
            print('выберите игру [elite dangerous]')
            for text in listen():
                print(text)

                if text in ['элитная опастность', 'элитной опасностью', 'элитное опасность', 'опасности', 'элитной опасность']:
                    print('включаю')
                    #buttons
                elif text == 'назад':
                    pass

        elif prompt == 'exit' or prompt == 'выход':
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
        elif prompt == 'db' or prompt == 'ви' or prompt == 'data base' or prompt == 'your data base' or prompt == 'твоя база данных':
            if debug == 1:
                for h in range(len(db)):
                    print(db[h])
        elif prompt == 'что ты умеешь':
            print(
                'я умею отвечать на вопросы и постоянно обучаюсь, но не поддерживаю режим диалога. Мои программисты под контролем Прядиева Романа, очень стараются для продвижения проекта, и постоянно его поддерживают. Если вам угодно, вы можете обновить программу(https://github.com/iLLokMaster/chatBOT)')
        elif prompt == 'открой браузер':
            os.system('C:/Users/B-ZONE/AppData/Local/Yandex/YandexBrowser/Application/browser.exe')
            print('на')
        elif prompt == 'какое дз':
            webbrowser.open('https://dnevnik.ru/marks/school/1000009993521/student/1000012990748/current', new = 2)
            print('держи')
        elif prompt == 'открой сам пикер':
            os.system('C:/Program Files (x86)/Steam/Steam.exe')
            time.sleep(10)
            os.system('C:/Users/B-ZONE/Desktop/игры/SteamAchievementManager-7.0.25/SAM.Picker.exe')
            print('на')
        elif prompt == 'режим чата':
            chat = 1
            for text in listen():
                print(text)
                prompt = text
            recp(prompt)
        else:
            print('я вас не понял')