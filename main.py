import sqlite3
import os
import random
import webbrowser
import json
import keyboard
import pyaudio
from vosk import Model, KaldiRecognizer
import time
import pyautogui as pag
import requests
import pyttsx3



#os.system('form.exe')

# Создание объекта для синтеза речи
SayPhrasesEngine = pyttsx3.init()
# Установка параметров речи (необязательно)
SayPhrasesEngine.setProperty('rate', 150)    # Скорость речи
SayPhrasesEngine.setProperty('volume', 0.9)  # Громкость речи
voices = SayPhrasesEngine.getProperty('voices')
SayPhrasesEngine.setProperty('voice', voices[0].id)

SayPhrasesEngine.say('привет, это ваш ассистент, я загружаюсь, ожидайте!')
SayPhrasesEngine.runAndWait()
def weather(city_name, text):
    api_key = "4d3976c583aeef24ef9481dc24dc48c5"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    print(x['weather'])
    text = text.replace(' ', '+')
    webbrowser.open(f"https://yandex.ru/search/?text={text}&clid=2270455&banerid=6301000000%3A65808155b2635984727c6729&win=606&lr=193")
chatMode = 0
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
def recp(prompt, chhat):
    persentageOfMatch = []
    prompt = prompt.lower()  # pr = re.sub('\W+',' ', pr )
    for k in range(len(db)):
        resultOfPercentage = per_com(prompt, db[k][0])  ###result = проценты совпадения
        persentageOfMatch.append([resultOfPercentage, db[k][1]])
    sortPers = sorted(persentageOfMatch)
    if resultOfPercentage == 0:
        print('Я вас не понял. Скажите ответ на ваш вопрос.(\n')
        SayPhrasesEngine.say('Я вас не понял. Скажите ответ на ваш вопрос.')
        SayPhrasesEngine.runAndWait()
        for text in listen():
            otvet_polzovatelya = text
            if text != '':
                print(text)
                cursor.execute(f"INSERT INTO AnsvQest VALUES ('{prompt}', '{otvet_polzovatelya}')")
                DataBaseSQL3inCode.commit()
                db.append([prompt, otvet_polzovatelya])
                chat(chhat)
    else:
        print('Ответ бота:')
        a = sortPers[-1][1]
        b = list(a)
        for alphabet in b:
            print(alphabet, end = '')
            time.sleep(0.01)

        SayPhrasesEngine.say(a)
        SayPhrasesEngine.runAndWait()
        print('\n')
        if sortPers[-1][0] != 100:
            print('вам понравился ответ?[да][нет]')
            SayPhrasesEngine.say('вам понравился ответ?')
            SayPhrasesEngine.runAndWait()

            for text in listen():
                if text != '':
                    print(text)

                    if text.lower() == 'нет':
                        print('ваш вариант ответа')
                        SayPhrasesEngine.say('ваш вариант ответа')
                        SayPhrasesEngine.runAndWait()
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
                                chat(chhat)
                        # print(db)
                    elif text.lower() == 'да':
                        cursor.execute(f"INSERT INTO AnsvQest VALUES ('"
                                       f"{prompt}', "
                                       f"'{sortPers[-1][1]}')")
                        DataBaseSQL3inCode.commit()
                        db.append([prompt, sortPers[-1][1]])
                        chat(chhat)
print('говорите\n')


# Синтез речи
SayPhrasesEngine.say('говорите')
SayPhrasesEngine.runAndWait()

def chat(chhat = 0):
    compleat = ['готово кмдр!\n', 'готово CMDR!\n', 'рад помочь!\n', 'держи!\n', 'лови!\n', 'compleat!\n', 'есть, сер!!!\n', 'вот держите, сер!\n', 'включаю\n', 'на\n', 'выполняю\n', 'сер, да, сер\n']
    while True:
        for text in listen():
            if text == '':
                chat(chhat)
            elif 'какая погода в' in text:
                print(text)
                city_name = 'воронеж'
                weather(city_name, text)

            elif text in ['режим игры', 'игры']:
                print(text)
                print('выберите игру [elite dangerous]')
                SayPhrasesEngine.say('выберите игру')
                SayPhrasesEngine.runAndWait()

                for text in listen():
                    if text in ['элитная опастность', 'элитной опасностью', 'элитное опасность', 'опасности', 'элитной опасность', 'элита']:
                        print(text)
                        print('включаю')
                        SayPhrasesEngine.say('включаю')
                        SayPhrasesEngine.runAndWait()
                        while True:
                            print('\n')
                            #buttonsa
                            for text in listen():
                                if text == 'назад':
                                    print(text)
                                    chat(chhat)
                                elif text == '':
                                    pass
                                elif text in ['фиксация', 'захват']:
                                    keyboard.press('7')
                                elif text in ['соло', 'одиночная', 'одиночную']:
                                    pag.moveTo(500, 500, 0.5)
                                    pag.leftClick()
                                    pag.moveTo(1300, 800, 0.5)
                                    time.sleep(1)
                                    keyboard.press('enter')
                                    time.sleep(0.1)
                                    keyboard.release('enter')
                                    print(text)
                                    print(random.choice(compleat))
                                    SayPhrasesEngine.say(random.choice(compleat))
                                    SayPhrasesEngine.runAndWait()
                                elif text in ['на главный экран', 'меню', 'на базу']:
                                    print(random.choice(compleat))
                                    keyboard.press('esc')
                                    keyboard.release('esc')
                                    pag.moveTo(250, 830, 1)
                                    time.sleep(0.1)
                                    keyboard.press('Enter')
                                    time.sleep(0.1)
                                    keyboard.release('enter')
                                    time.sleep(0.1)
                                    keyboard.press('Enter')
                                    time.sleep(0.1)
                                    keyboard.release('enter')
                                    SayPhrasesEngine.say(random.choice(compleat))
                                    SayPhrasesEngine.runAndWait()
                                elif text == 'полная тяга':
                                    keyboard.press('w')
                                    time.sleep(4)
                                    keyboard.release('w')
                                    print(text)
                                    print(random.choice(compleat))
                                    SayPhrasesEngine.say(random.choice(compleat))
                                    SayPhrasesEngine.runAndWait()
                                elif text == 'стоп':
                                    keyboard.press('x')
                                    time.sleep(0.1)
                                    keyboard.release('x')
                                    print(text)
                                    print(random.choice(compleat))
                                    SayPhrasesEngine.say(random.choice(compleat))
                                    SayPhrasesEngine.runAndWait()
                                elif text in ['прыжок']:
                                    keyboard.press('j')
                                    time.sleep(0.5)
                                    keyboard.release('j')
                                    print(text)
                                    print(random.choice(compleat))
                                    SayPhrasesEngine.say(random.choice(compleat))
                                    SayPhrasesEngine.runAndWait()
                                elif text in ['карта галактики']:
                                    keyboard.press('5')
                                    time.sleep(0.1)
                                    keyboard.release('5')
                                    print(text)
                                    print(random.choice(compleat))
                                    SayPhrasesEngine.say(random.choice(compleat))
                                    SayPhrasesEngine.runAndWait()
                                elif text in ['картер система', 'карты системах', 'карта системы', 'карты системы','карты системы', 'карту систему', 'карту системы']:
                                    keyboard.press('6')
                                    time.sleep(0.1)
                                    keyboard.release('6')
                                    print(text)
                                    print(random.choice(compleat))
                                    SayPhrasesEngine.say(random.choice(compleat))
                                    SayPhrasesEngine.runAndWait()
                                elif text in ['в игру', 'к игре', 'продолжить', 'продолжим']:
                                    keyboard.press('backspace')
                                    time.sleep(0.1)
                                    keyboard.release('backspace')
                                    print(text)
                                    print(random.choice(compleat))
                                    SayPhrasesEngine.say(random.choice(compleat))
                                    SayPhrasesEngine.runAndWait()
                                elif text in ['сканер системы', 'сканера систем', 'сканер систем', 'сканер система']:
                                    keyboard.press("'")
                                    time.sleep(0.1)
                                    keyboard.release("'")
                                    print(text)
                                    print(random.choice(compleat))
                                    SayPhrasesEngine.say(random.choice(compleat))
                                    SayPhrasesEngine.runAndWait()
                                elif text in ['гнезда']:
                                    keyboard.press('u')
                                    time.sleep(0.1)
                                    keyboard.release('u')
                                    SayPhrasesEngine.say(random.choice(compleat))
                                    SayPhrasesEngine.runAndWait()
                                elif text in ['шасси']:
                                    keyboard.press('l')
                                    time.sleep(0.1)
                                    keyboard.release('l')
                                    SayPhrasesEngine.say(random.choice(compleat))
                                    SayPhrasesEngine.runAndWait()
                                else:
                                    print(text)
                                    print('я вас не понял')
                    elif text in ['выживалка', 'выживание', 'выживал']:
                        while True:
                            print('\n')
                            # buttonsa
                            for text in listen():
                                if text == 'назад':
                                    print(text)
                                    chat(chhat)
                                elif text == '':
                                    pass


                    elif text == 'назад':
                        print(text)
                        SayPhrasesEngine.say(random.choice(compleat))
                        SayPhrasesEngine.runAndWait()
                        chat(chhat)
            elif text == 'exit' or text == 'выход':
                print(text)
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
                good_by = ['почему ты меня бросаешь? не надо, пожалуйста.(котик с блестящими глазками)', 'пока', 'Приходите пожалуйста поскорее. Я по вам уже скучаю:(', 'не оставляйте меня одного на долго', 'нееееееее...', 'не оставляй меня на долго, пожалуйста, я очень тебя прошу']
                print(random.choice(good_by))
                SayPhrasesEngine.say(random.choice(good_by))
                SayPhrasesEngine.runAndWait()
                exit()
            elif text in['db', 'ви', 'data base', 'your data base', 'твоя база данных', 'база данных']:
                print(text)
                if debug == 1:
                    for h in range(len(db)):
                        print(db[h])
            elif text == 'что ты умеешь':
                print(text)
                print('я умею отвечать на вопросы и постоянно обучаюсь, но не поддерживаю режим диалога. Мои программисты под контролем Прядиева Романа, очень стараются для продвижения проекта, и постоянно его поддерживают. Если вам угодно, вы можете обновить программу(https://github.com/iLLokMaster/chatBOT)\n')
                SayPhrasesEngine.say('я умею отвечать на вопросы и постоянно обучаюсь, но не поддерживаю режим диалога. Мои программисты под контролем Прядиева Романа, очень стараются для продвижения проекта, и постоянно его поддерживают. Если вам угодно, вы можете обновить программу')
                SayPhrasesEngine.runAndWait()
            elif text in ['открой браузер', 'браузер']:
                print(text)
                os.system('C:/Users/B-ZONE/AppData/Local/Yandex/YandexBrowser/Application/browser.exe')
                print(random.choice(compleat))
                SayPhrasesEngine.say(random.choice(compleat))
                SayPhrasesEngine.runAndWait()
            elif text in ['домашняя работа', 'домашнюю работу']:
                print(text)
                webbrowser.open('https://dnevnik.ru/marks/school/1000009993521/student/1000012990748/current', new = 2)
                print(random.choice(compleat))
                SayPhrasesEngine.say(random.choice(compleat))
                SayPhrasesEngine.runAndWait()
            elif text in ['открой игры', 'стил', 'стим', 'тим', 'стин']:
                print(text)
                print(random.choice(compleat))
                SayPhrasesEngine.say(random.choice(compleat))
                SayPhrasesEngine.runAndWait()
                os.system('C:/steeeem/steam.exe.lnk')
                chat(chhat)
            elif text in ['телеграм', 'телеграмм']:
                print(text)
                print(random.choice(compleat))
                SayPhrasesEngine.say(random.choice(compleat))
                SayPhrasesEngine.runAndWait()
                os.system('C:/steeeem/Telegram.exe.lnk')
                recp(text, chhat)
            elif text in ['чат', 'общение', 'к общению', 'в общении', 'режим чата', 'режим общения']:
                print('чат активирован\n')
                SayPhrasesEngine.say(random.choice('чат активирован'))
                SayPhrasesEngine.runAndWait()
                chhat = 1
            elif text in ['закрой чат', 'хватит общаться']:
                print('выключаю...\n')
                chhat = 0
                print(random.choice(compleat))
                SayPhrasesEngine.say(random.choice(compleat))
                SayPhrasesEngine.runAndWait()
            elif text in ['видео', 'я хочу посмотреть видео']:
                webbrowser.open('https://www.youtube.com/', new = 2)
                print(random.choice(compleat))
                SayPhrasesEngine.say(random.choice(compleat))
                SayPhrasesEngine.runAndWait()
            elif text in ['эскорт', 'дискомфорт', 'дискурс', 'дискурса']:
                os.system('C:/steeeem/disc.exe.lnk')
                print(random.choice(compleat))
                SayPhrasesEngine.say(random.choice(compleat))
                SayPhrasesEngine.runAndWait()
            elif chhat == 1:
                print(text)
                recp(text, chhat)
            else:
                print(text)
                print('я вас не понял\n')


chat(chatMode)
