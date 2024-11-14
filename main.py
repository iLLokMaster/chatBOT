import io
import sqlite3
import os
import random
import sys
import threading
import webbrowser
import json
import keyboard
import pyaudio
from PyQt5 import uic
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic.properties import QtCore, QtGui, QtWidgets
from vosk import Model, KaldiRecognizer
import time
import pyautogui as pag
import pyttsx3
from threading import *


class ChatBot(QMainWindow):
    def __init__(self, form_maker = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if form_maker:
            uic.loadUi('chatForm.ui', self)  # Load the .ui file1
            self.initUI()
        else:
            self.text = ''
            self.voice = True
            self.chat()

    def initUI(self):
        self.checkBoxVoice.clicked.connect(self.voice_const_changer)

    def voice_const_changer(self):
        self.voice = not self.voice
        if not self.voice:
            self.say_and_print(user_text = '', phrase = 'Понял, больше вас не слушаю, CoMaNDeR!')
        else:
            self.say_and_print(user_text = '', phrase = 'Понял, слушаю вас!')

    def say_and_print(self, user_text, phrase = '', phrase_that_not_saied = ''):
        print('Вы: ', user_text)
        print('собеседник: ', phrase + ' ' + phrase_that_not_saied)
        say_phrases_engine.say(phrase)
        say_phrases_engine.runAndWait()

    def chat(self, chhat = 0):
        # список слов или фраз, необходимых для их воспроизведения, после выполнения команды
        compleat = ['готово кмдр!', 'готово CMDR!', 'рад помочь!', 'держи!', 'лови!', 'compleat!',
                    'есть, сер!!!', 'вот держите, сер!', 'включаю', 'на', 'выполняю',
                    'сер, да, сер']
        while True:
            for self.text in self.listen():
                if self.text == '':
                    self.chat(self)
                elif 'какая погода в' in self.text:
                    print(self.text)
                    city_name = 'воронеж'
                    self.get_weather(self)
                elif self.text in ['режим игры', 'игры']:
                    self.say_and_print(user_text = self.text, phrase = 'Выберите игру',
                                       phrase_that_not_saied = '[elite dangerous]')
                    for self.text in self.listen():
                        if self.text in ['элитная опастность', 'элитной опасностью', 'элитное опасность', 'опасности',
                                         'элитной опасность', 'элита']:
                            self.say_and_print(user_text = self.text, phrase = 'включаю')
                            while True:  # 7wxj56'ul
                                print('\n')
                                for self.text in self.listen():
                                    if self.text == 'назад':
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                        self.chat(self)
                                    elif self.text == '':
                                        pass
                                    elif self.text in ['фиксация', 'захват']:
                                        keyboard.press('7')
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                    elif self.text in ['соло', 'одиночная', 'одиночную']:
                                        pag.moveTo(500, 500, 0.5)
                                        pag.leftClick()
                                        pag.moveTo(1300, 800, 0.5)
                                        time.sleep(1)
                                        keyboard.press('enter')
                                        time.sleep(0.1)
                                        keyboard.release('enter')
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                    elif self.text in ['на главный экран', 'меню', 'на базу']:
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
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                    elif self.text == 'полная тяга':
                                        keyboard.press('w')
                                        time.sleep(4)
                                        keyboard.release('w')
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                    elif self.text == 'стоп':
                                        keyboard.press('x')
                                        time.sleep(0.1)
                                        keyboard.release('x')
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                    elif self.text in ['прыжок']:
                                        keyboard.press('j')
                                        time.sleep(0.5)
                                        keyboard.release('j')
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                    elif self.text in ['карты галактики', 'карта галактики']:
                                        keyboard.press('5')
                                        time.sleep(0.1)
                                        keyboard.release('5')
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                    elif self.text in ['картер система', 'карты системах', 'карта системы',
                                                       'карты системы', 'карты системы', 'карту систему',
                                                       'карту системы']:
                                        keyboard.press('6')
                                        time.sleep(0.1)
                                        keyboard.release('6')
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                    elif self.text in ['в игру', 'к игре', 'продолжить', 'продолжим']:
                                        keyboard.press('backspace')
                                        time.sleep(0.1)
                                        keyboard.release('backspace')
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                    elif self.text in ['сканер системы', 'сканера систем', 'сканер систем',
                                                       'сканер система']:
                                        keyboard.press("'")
                                        time.sleep(0.1)
                                        keyboard.release("'")
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                    elif self.text in ['гнезда']:
                                        keyboard.press('u')
                                        time.sleep(0.1)
                                        keyboard.release('u')
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                    elif self.text in ['шасси']:
                                        keyboard.press('l')
                                        time.sleep(0.1)
                                        keyboard.release('l')
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                    else:
                                        self.say_and_print(user_text = self.text, phrase = 'Я вас не понял')
                        elif self.text in ['выживалка', 'выживание', 'выживал']:
                            while True:
                                print('\n')
                                for self.text in self.listen():
                                    if self.text == 'назад':
                                        print(self.text)
                                        self.chat(self)
                                    elif self.text == '':
                                        pass
                        elif self.text == 'назад':
                            self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                            self.chat(self)
                elif self.text == 'exit' or self.text == 'выход':
                    if debug == 1:
                        print('     сохраняем изменения в базе')
                    if debug == 1:
                        try:
                            data_base_sql3in_code.close()
                            print('     изменения сохранены')
                        except sqlite3.Error as e:
                            print("     не удалось сохранить изменения")
                            error_code = e.args[0]
                            print(f"     Error code: {error_code}")
                    good_by = ['почему ты меня бросаешь? не надо, пожалуйста.(котик с блестящими глазками)', 'пока',
                               'Приходите пожалуйста поскорее. Я по вам уже скучаю:(',
                               'не оставляйте меня одного на долго',
                               'нееееееее...', 'не оставляй меня на долго, пожалуйста, я очень тебя прошу']
                    self.say_and_print(user_text = self.text, phrase = random.choice(good_by))
                    exit()
                elif self.text in ['db', 'ви', 'data base', 'your data base', 'твоя база данных', 'база данных']:
                    print(self.text)
                    if debug == 1:
                        for h in range(len(db)):
                            print(db[h])
                elif self.text == 'что ты умеешь':
                    what_can_i_do = ('Я умею отвечать на вопросы и постоянно обучаюсь, '
                                     'но не поддерживаю режим диалога. '
                                     'Мои программисты под контролем @CMDRillok, '
                                     'очень стараются для продвижения проекта,'
                                     ' и постоянно его поддерживают. Если вам угодно, вы можете обновить программу\n')
                    # threading.Thread(target = self.say_and_print, args = (self.text, what_can_i_do, '(https://github.com/iLLokMaster/chatBOT)'))
                    self.say_and_print(user_text = self.text, phrase = what_can_i_do,
                                       phrase_that_not_saied = ' (https://github.com/iLLokMaster/chatBOT)')
                elif self.text in ['открой браузер', 'браузер']:
                    os.system('C:/Users/B-ZONE/AppData/Local/Yandex/YandexBrowser/Application/browser.exe')
                    self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                elif self.text in ['домашняя работа', 'домашнюю работу']:
                    webbrowser.open('https://dnevnik.ru/marks/school/1000009993521/student/1000012990748/current',
                                    new = 2)
                    self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                elif self.text in ['открой игры', 'стил', 'стим', 'тим', 'стин']:
                    self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                    os.system('C:/steeeem/steam.exe.lnk')
                    self.chat(self)
                elif self.text in ['телеграм', 'телеграмм']:
                    self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                    os.system('C:/steeeem/Telegram.exe.lnk')
                elif self.text in ['видео', 'я хочу посмотреть видео']:
                    webbrowser.open('https://www.youtube.com/', new = 2)
                    self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                elif self.text in ['дискорд', 'эскорт', 'дискомфорт', 'дискурс', 'дискурса']:
                    os.system('C:/steeeem/disc.exe.lnk')
                    self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                else:
                    pass
                    # self.recp()

    def per_common(self, list2):  # расчёт схожести эллемента из БД и запроса юзера
        list1 = self.text
        common_elements = set(list1) & set(list2)
        percent_match = (len(common_elements) / len(set(list1 + list2))) * 100
        return percent_match

    def recp(self):
        if self.text == "None_pole":
            self.chat(self)
        else:
            persentage_of_match = []
            self.text = self.text.lower()  # pr = re.sub('\W+',' ', pr )
            for k in range(len(db)):
                result_of_percentage = self.per_common(db[k][0])  # result = проценты совпадения
                persentage_of_match.append([result_of_percentage, db[k][1]])
            sort_pers = sorted(persentage_of_match)
            if result_of_percentage == 0:
                self.say_and_print(user_text = self.text, phrase = 'Я вас не понял. Скажите ответ на ваш вопрос.(',
                                   phrase_that_not_saied = '')
                for self.text in self.listen():
                    otvet_polzovatelya = self.text
                    if self.text != '':
                        print(self.text)
                        cursor.execute(f"INSERT INTO AnsvQest VALUES ('{self.text}', '{otvet_polzovatelya}')")
                        data_base_sql3in_code.commit()
                        db.append([self.text, otvet_polzovatelya])
                        self.chat(self)
            else:
                a = sort_pers[-1][1]
                self.say_and_print(user_text = self.text, phrase = a)
                if sort_pers[-1][0] != 100:
                    self.say_and_print(user_text = self.text, phrase = 'вам понравился ответ?',
                                       phrase_that_not_saied = '[да][нет]')
                    for self.text in self.listen():
                        if self.text != '':
                            if self.text.lower() == 'нет':
                                self.say_and_print(user_text = self.text, phrase = 'ваш вариант ответа')
                                for self.text in self.listen():
                                    if self.text != '':
                                        self.say_and_print(user_text = self.text)
                                        cursor.execute(
                                            f"INSERT INTO AnsvQest VALUES ('"
                                            f"{self.text}', "
                                            f"'{self.text}')"
                                        )
                                        data_base_sql3in_code.commit()
                                        db.append([self.text, self.text])
                                        self.chat(self)
                            elif self.text.lower() == 'да':
                                self.say_and_print(user_text = 'да')
                                cursor.execute(f"INSERT INTO AnsvQest VALUES ('"
                                               f"{self.text}', "
                                               f"'{sort_pers[-1][1]}')")
                                data_base_sql3in_code.commit()
                                db.append([self.text, sort_pers[-1][1]])
                                self.chat(self)

    def get_weather(self, sity = "Воронеж"):  # открытие сайта с прогнозом погоды
        try:
            webbrowser.open(f"https://yandex.ru/search/?text={sity}"
                            f"&clid=2270455&banerid=6301000000%3A65808155b2635984727c6729&win=606&lr=193")
        except Exception as e:
            if debug == 1:
                print(f'Exception {e}')
            self.get_weather(self)

    def listen(self):
        while True:
            if self.voice:
                data = stream.read(4000, exception_on_overflow = False)
                if rec.AcceptWaveform(data) and len(data) > 0:
                    result = json.loads(rec.Result())
                    if 'text' in result:
                        yield result['text']


def settings4say():  # установка параметров синтеза речи
    say_phrases_engine = pyttsx3.init()
    say_phrases_engine.setProperty('rate', 150)
    say_phrases_engine.setProperty('volume', 0.9)
    voices = say_phrases_engine.getProperty('voices')
    return say_phrases_engine, voices

def settings4recognition():  # функция необходимая для задания параметров распознования речи, подключения модели
    model = Model('models/vosk-model-ru-0.42')
    rec = KaldiRecognizer(model, 16000)
    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000)
    stream.start_stream()
    return stream, rec


say_phrases_engine, voices = settings4say()
say_phrases_engine.setProperty('voice', voices[0].id)
say_phrases_engine.say('привет, это ваш ассистент, я загружаюсь, ожидайте!')
say_phrases_engine.runAndWait()
# константы
debug = 0
'''Проверка на наличие базы данных, при обнаружении которой(про удачном реквесте), происходит подключение к ней.
А если такой базы не существует, то она создаётся, и туда добавляется одна пара(ключ: ззначение), 
что необходимо для правильной работы программы(def per_com())'''
data_base_sql3in_code = sqlite3.connect("DataBaseInFiles")
cursor = data_base_sql3in_code.cursor()
try:
    cursor.execute("SELECT * FROM AnsvQest")
except sqlite3.Error:
    cursor.execute("""CREATE TABLE AnsvQest (
            answer sity,
            qestion sity
        )""")
    cursor.execute("INSERT INTO AnsvQest VALUES ('привет', "
                   "'Привет, как у тебя дела?')")
db = cursor.execute("SELECT * FROM AnsvQest").fetchall()
data_base_sql3in_code.commit()

stream, rec = settings4recognition()
print('говорите\n')
# Синтез речи
say_phrases_engine.say('говорите')
say_phrases_engine.runAndWait()

# запуск приложения
app = QApplication([])
window = ChatBot(form_maker = True)
window.show()
ChatBot()
app.exit(app.exec())
