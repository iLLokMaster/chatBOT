import sqlite3
import os
import random
import webbrowser
import json
import keyboard
import pyaudio
import requests
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from vosk import Model, KaldiRecognizer
import time
import pyautogui as pag
import pyttsx3


class ChatBot(QMainWindow):
    def __init__(self, form_maker = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if form_maker:
            uic.loadUi('chatForm.ui', self)  # Load the .ui file
            self.initUI()
        else:
            self.text = ''
            self.voice = True
            self.debug = False
            self.make_answer = True
            self.do_commands = True
            self.study = False
            self.chat()

    def initUI(self):  # создание формы
        self.checkBoxVoice.clicked.connect(self.voice_const_changer)
        self.ButtonSent.clicked.connect(self.send_button)
        self.pushButtonAply_2.clicked.connect(self.apply_properties)
        self.checkBox_debug.clicked.connect(self.debug_const_changer)
        self.checkBox_make_answer.clicked.connect(self.make_answer_const_changer)
        self.checkBox_do_comands.clicked.connect(self.do_commands_const_changer)
        self.checkBox_study.clicked.connect(self.study_const_changer)
        self.pushButton_github.clicked.connect(lambda: webbrowser.open('https://github.com/iLLokMaster/chatBOT'))

    def study_const_changer(self):
        self.do_commands = not self.do_commands
        if self.checkBox_do_comands.isChecked():
            self.say_and_print(user_text = '', phrase = 'Спасибо за ваш вклал в проект!')
        else:
            self.say_and_print(user_text = '', phrase = 'Понял. Спасибо, что попробовали!')

    def do_commands_const_changer(self):
        # смена параметра {self.do_commands}
        self.do_commands = not self.do_commands
        if self.checkBox_do_comands.isChecked():
            self.say_and_print(user_text = '', phrase = 'Понял, буду реагировать, CoMaNDeR!')
        else:
            self.say_and_print(user_text = '', phrase = 'Понял. больше не реагирую на команды! Кэ Мэ Дэ эР')

    def make_answer_const_changer(self):
        # смена параметра {self.make_answer}
        self.make_answer = not self.make_answer
        if self.checkBox_make_answer.isChecked():
            self.say_and_print(user_text = '', phrase = 'Понял, буду отвечать на ваши вопросы, CoMaNDeR!')
        else:
            self.say_and_print(user_text = '', phrase = 'Понял, больше вы не увидите ответов на сообщения, '
                                                        'кроме команд!')

    def debug_const_changer(self):
        # смена параметра {self.debug}
        self.debug = not self.debug
        if self.checkBox_debug.isChecked():
            self.say_and_print(user_text = '', phrase = 'Понял, активирую режим разработчика, CoMaNDeR!')
        else:
            self.say_and_print(user_text = '', phrase = 'Понял, больше вы не видите системные сообщения!')

    def voice_const_changer(self):
        # смена параметра {voice}
        self.voice = not self.voice
        if not self.checkBoxVoice.isChecked():
            self.say_and_print(user_text = '', phrase = 'Понял, больше вас не слушаю, CoMaNDeR!')
        else:
            self.say_and_print(user_text = '', phrase = 'Понял, слушаю вас!')

    def apply_properties(self):
        file_model = open('way_to_model_S2T.txt', 'w')
        file_model.write(self.lineEdit_wayS2T.text())
        file_model.close()
        file_city = open('user_city.txt', 'w')
        city_text = self.lineEdit_sity.text()

        dic = {'Ь': '', 'ь': '', 'Ъ': '', 'ъ': '', 'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v',
               'Г': 'G', 'г': 'g', 'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'E', 'ё': 'e', 'Ж': 'Zh', 'ж': 'zh',
               'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'Й': 'I', 'й': 'i', 'К': 'K', 'к': 'k', 'Л': 'L', 'л': 'l',
               'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'О': 'O', 'о': 'o', 'П': 'P', 'п': 'p', 'Р': 'R', 'р': 'r',
               'С': 'S', 'с': 's', 'Т': 'T', 'т': 't', 'У': 'U', 'у': 'u', 'Ф': 'F', 'ф': 'f', 'Х': 'Kh', 'х': 'kh',
               'Ц': 'Tc', 'ц': 'tc', 'Ч': 'Ch', 'ч': 'ch', 'Ш': 'Sh', 'ш': 'sh', 'Щ': 'Shch', 'щ': 'shch', 'Ы': 'Y',
               'ы': 'y', 'Э': 'E', 'э': 'e', 'Ю': 'Iu', 'ю': 'iu', 'Я': 'Ia', 'я': 'ia'}

        alphabet = ['Ь', 'ь', 'Ъ', 'ъ', 'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё',
                    'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о',
                    'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч',
                    'Ш', 'ш', 'Щ', 'щ', 'Ы', 'ы', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']

        st = city_text.lover().capitalize()
        result = str()

        len_st = len(st)
        for i in range(0, len_st):
            if st[i] in alphabet:
                simb = dic[st[i]]
            else:
                simb = st[i]
            result = result + simb

        file_city.write(result)
        file_city.close()

    def send_button(self):  # обработчик кнопки отправки сообщения
        self.text = self.lineEdit.text()
        self.chat()

    def say_and_print(self, user_text, phrase = '', phrase_that_not_sayed = ''):
        f"""в этой функции производится процесс печати сообщения пользователя({user_text}), ответа чат бота({phrase})
         и печать фразы, которая не говорится({phrase_that_not_sayed}).
        функция запоминает текущий текст, что уже напечатан и добавляя к нему параметры функции, печатает
        и преобразовывает в звук."""

        """форма не отвечает, из-за долгой проверки, долгого распознования голоса и долгого ответа на вопрос =>
        => не получаеться записать ответ в сама форму. для теста программы используется print(), но ниже
        я оставлю, то, как это должно работать, используя try...except..."""
        try:
            now_on_text_edit = self.textEdit.toPlainText()
            if user_text:
                self.textEdit.setPlainText(f'{now_on_text_edit}\n Вы: {user_text}\n ')
                now_on_text_edit = self.textEdit.toPlainText()
            if phrase:
                self.textEdit.setPlainText(f'{now_on_text_edit}\n Собеседник: {phrase} {phrase_that_not_sayed}')
        except Exception as E:
            print(E)
            if user_text:
                print('Вы: ', user_text)
            if phrase:
                print('собеседник: ', phrase + ' ' + phrase_that_not_sayed)
                say_phrases_engine.say(phrase)
                say_phrases_engine.runAndWait()

    def chat(self, chat_mode = 0):
        f"""В этой фцнкции происходит первичная обработка ввода пользователя, путём простых условий.
        при не нахождении в этом списке команд ввода({self.text}), запускаются функции вторичной обработки"""
        # список слов или фраз, необходимых для их воспроизведения, после выполнения команды
        compleat = ['готово кмдр!', 'готово CMDR!', 'рад помочь!', 'держи!', 'лови!', 'compleat!',
                    'есть, сер!!!', 'вот держите, сер!', 'включаю', 'на', 'выполняю',
                    'сер, да, сер']
        if self.voice:
            while True:
                for self.text in self.listen():
                    self.if_req_in_func(compleat)
        else:
            self.if_req_in_func(compleat)

    def if_req_in_func(self, compleat):
        """сами первичные обработчики запроса"""
        """если вы хотите, что бы у вас открывался стим, дискорд, браузер и тд,
         то по этому пути('C:/steeeem/steam.exe.lnk') разместите ярлыки на программы."""
        if keyboard.is_pressed('Enter'):
            self.send_button()
        if self.text == '':
            self.chat(self)
        elif 'какая погода в' in self.text:
            if self.do_commands:
                self.say_and_print(user_text = self.text)
                city_name = 'воронеж'
                self.get_weather(self)
                self.chat(self)
        elif self.text in ['режим игры', 'игры']:
            if self.do_commands:
                self.say_and_print(user_text = self.text, phrase = 'Выберите игру',
                                   phrase_that_not_sayed = '[elite dangerous]')
                for self.text in self.listen():
                    if self.text in ['элитная опастность', 'элитной опасностью', 'элитное опасность', 'опасности',
                                     'элитной опасность', 'элита']:
                        self.say_and_print(user_text = self.text, phrase = 'включаю')
                        while True:  # 7wxj56'ul
                            if self.do_commands:
                                for self.text in self.listen():
                                    if self.text == 'назад':
                                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                        self.chat(self)
                                    elif self.text == '':
                                        pass
                                    elif self.text in ['инара', 'енара']:
                                        if self.do_commands:
                                            webbrowser.open('https://inara.cz/elite/news/')
                                            self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                            self.chat(self)
                                    elif self.text in ['едсм', 'edsm']:
                                        if self.do_commands:
                                            webbrowser.open('https://lichess.org/')
                                            self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                            self.chat(self)
                                    elif self.text in ['поиск тесла', 'быстрые маршруты']:
                                        if self.do_commands:
                                            webbrowser.open('https://spansh.co.uk/bodies')
                                            self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                                            self.chat(self)
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
                            for self.text in self.listen():
                                if self.text == 'назад':
                                    self.say_and_print(user_text = '', phrase_that_not_sayed = self.text)
                                    self.chat(self)
                                elif self.text == '':
                                    pass
                    elif self.text == 'назад':
                        self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                        self.chat(self)
        elif self.text in 'пиши под диктовку':
            while True:
                for self.text in self.listen():
                    if self.text == '':
                        pass
                    elif self.text == 'назад' or self.text == 'хватит':
                        self.chat()
                    elif self.text == 'ентер' or self.text == 'энтер':
                        keyboard.press('Enter')
                    elif self.text == 'запятая':
                        keyboard.press(',')
                    elif self.text == 'точка':
                        keyboard.press('.')
                    elif self.text == 'открытая скобка':
                        keyboard.press('(')
                    elif self.text == 'закрытая скобка':
                        keyboard.press(')')
                    elif self.text == 'двоеточие':
                        keyboard.press(':')
                    elif self.text == 'троеточие':
                        keyboard.press('...')
                    elif self.text == 'восклецательный знак':
                        keyboard.press('!')
                    elif self.text == 'вопросительный знак':
                        keyboard.press('?')
                    else:
                        keyboard.write(self.text)

        elif self.text == 'exit' or self.text == 'выход':
            if self.do_commands:
                if self.debug:
                    self.say_and_print(user_text = '', phrase_that_not_sayed = '     сохраняем изменения в базе')
                if self.debug:
                    try:
                        data_base_sql3in_code.close()
                        self.say_and_print(user_text = '', phrase_that_not_sayed = '     изменения сохранены')
                    except sqlite3.Error as e:
                        self.say_and_print(user_text = '',
                                           phrase_that_not_sayed = '     не удалось сохранить изменения')
                        error_code = e.args[0]
                        self.say_and_print(user_text = '', phrase_that_not_sayed = f"     Error code: {error_code}")
                good_by = ['почему ты меня бросаешь? не надо, пожалуйста.(котик с блестящими глазками)', 'пока',
                           'Приходите пожалуйста поскорее. Я по вам уже скучаю:(',
                           'не оставляйте меня одного на долго',
                           'нееееееее...', 'не оставляй меня на долго, пожалуйста, я очень тебя прошу']
                self.say_and_print(user_text = self.text, phrase = random.choice(good_by))
                exit()
        elif self.text in ['db', 'ви', 'data base', 'your data base', 'твоя база данных', 'база данных']:
            if self.do_commands:
                self.say_and_print(user_text = self.text)
                if self.debug:
                    for h in range(len(db)):
                        self.say_and_print(user_text = '', phrase_that_not_sayed = db[h])
                        self.chat(self)
        elif self.text == 'что ты умеешь':
            if self.do_commands:
                what_can_i_do = ('Я умею отвечать на вопросы и постоянно обучаюсь, '
                                 'но не поддерживаю режим диалога. '
                                 'Мои программисты под контролем @CMDRillok, '
                                 'очень стараются для продвижения проекта,'
                                 ' и постоянно его поддерживают. Если вам угодно, вы можете обновить программу\n')
                self.say_and_print(user_text = self.text, phrase = what_can_i_do,
                                   phrase_that_not_sayed = ' (https://github.com/iLLokMaster/chatBOT)')
                self.chat(self)
        elif self.text in ['открой браузер', 'браузер']:
            if self.do_commands:
                os.system('C:/Users/B-ZONE/AppData/Local/Yandex/YandexBrowser/Application/browser.exe')
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                self.chat(self)
        elif self.text in ['домашняя работа', 'домашнюю работу']:
            if self.do_commands:
                webbrowser.open('https://dnevnik.ru/marks/school/1000009993521/student/1000012990748/current',
                                new = 2)
                self.chat(self)
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
        elif self.text in ['steam', 'открой игры', 'стил', 'стим', 'тим', 'стин', 'открой игру']:
            if self.do_commands:
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                os.system('C:/steeeem/steam.exe.lnk')
                self.chat(self)
        elif self.text in ['телеграм', 'телеграмм']:
            if self.do_commands:
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                os.system('C:/steeeem/Telegram.exe.lnk')
                self.chat(self)
        elif self.text in ['видео', 'я хочу посмотреть видео']:
            if self.do_commands:
                webbrowser.open('https://www.youtube.com/', new = 2)
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                self.chat(self)
        elif self.text in ['дискорд', 'эскорт', 'дискомфорт', 'дискурс', 'дискурса']:
            if self.do_commands:
                os.system('C:/steeeem/disc.exe.lnk')
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                self.chat(self)
        elif self.text in ['github', 'гитхаб', 'гит хаб', 'git hub']:
            if self.do_commands:
                webbrowser.open('https://github.com/iLLokMaster/chatBOT')
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                self.chat(self)
        elif self.text in ['переводчик']:
            if self.do_commands:
                webbrowser.open('https://translate.yandex.ru/')
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                self.chat(self)
        elif self.text in ['гос услуги', 'госуслуги']:
            if self.do_commands:
                webbrowser.open('https://www.gosuslugi.ru/')
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                self.chat(self)
        elif self.text in ['шахматы', 'личес']:
            if self.do_commands:
                webbrowser.open('https://lichess.org/')
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                self.chat(self)
        elif self.text in ['инара', 'енара']:
            if self.do_commands:
                webbrowser.open('https://inara.cz/elite/news/')
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                self.chat(self)
        elif self.text in ['едсм', 'edsm']:
            if self.do_commands:
                webbrowser.open('https://lichess.org/')
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                self.chat(self)
        elif self.text in ['поиск тесла', 'быстрые маршруты']:
            if self.do_commands:
                webbrowser.open('https://spansh.co.uk/bodies')
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat))
                self.chat(self)
        elif 'найди в яндексе' in self.text or 'найти в яндексе' in self.text:
            if self.do_commands:
                compleat_open = ['открываю', 'выполняю', 'делаю запрос']
                user_text = self.text.replace('найди в яндексе', '')
                user_text = user_text.replace('найти в яндексе', '')

                blok_list = user_text.split()  # разбиваем слова по пробелам
                url_query = '%20'.join(blok_list)  # разделяем их через %20
                url = 'https://yandex.ru/search/?text=' + url_query + '&lr=213'  # подставляем
                webbrowser.open(url)
                self.say_and_print(user_text = self.text, phrase = random.choice(compleat_open))
                self.chat(self)
        else:
            if self.make_answer:
                self.recp()
            else:
                self.chat()

    def per_common(self, list2):
        """расчёт схожести эллемента из БД и запроса юзера с возвратом процентов схожести.
        Одна из функций вторичной обработки"""
        list1 = self.text
        common_elements = set(list1) & set(list2)
        percent_match = (len(common_elements) / len(set(list1 + list2))) * 100
        return percent_match

    def recp(self):
        """Подбор ответа на вопрос пользователя, запись в базу данных неизвесного вопроса с новым ответом.
        Одна из функций вторичной обработки"""
        global result_of_percentage
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
                if self.study:
                    self.say_and_print(user_text = self.text, phrase = 'Я вас не понял. Скажите ответ на ваш вопрос.(',
                                       phrase_that_not_sayed = '')
                    for self.text in self.listen():
                        otvet_polzovatelya = self.text
                        if self.text != '':
                            self.say_and_print(user_text = self.text)
                            cursor.execute(f"INSERT INTO AnsvQest VALUES ('{self.text}', '{otvet_polzovatelya}')")
                            data_base_sql3in_code.commit()
                            db.append([self.text, otvet_polzovatelya])
                            self.chat(self)
            else:
                a = sort_pers[-1][1]
                self.say_and_print(user_text = self.text, phrase = a)
                if self.study:
                    if sort_pers[-1][0] != 100:
                        self.say_and_print(user_text = self.text, phrase = 'вам понравился ответ?',
                                           phrase_that_not_sayed = '[да][нет]')
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

    def get_weather(self, city = "voronezh"):  # открытие сайта с прогнозом погоды
        city = 'voronezh'
        compleat = ['готово кмдр!', 'готово CMDR!', 'рад помочь!', 'держи!', 'лови!', 'compleat!',
                    'есть, сер!!!', 'вот держите, сер!', 'включаю', 'на', 'выполняю',
                    'сер, да, сер', 'Зачем тебе погода? Всё равно дома сидишь!',
                    'Держи свою погоду! Вы на него посмотрите, на улицу он собрался!']
        try:
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city
            response = requests.get(complete_url)
            weather = response.json()
            self.say_and_print(user_text = '', phrase = weather)
        except Exception as e:
            if self.debug:
                print(f'Exception <__main__.ChatBot%20object%20at%200x0000022B882A79B0> {e}')
            webbrowser.open(f"https://yandex.ru/pogoda/{city}")
            self.say_and_print(user_text = self.text,
                               phrase = random.choice(compleat),
                               phrase_that_not_sayed = 'не удалось сделать request')

    def listen(self):  # прослушивание пользовательского микрофона
        if self.voice:
            while True:
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


def settings4recognition():  # функция необходимая для назначения параметров распознования речи, подключения модели
    try:
        file = open('way_to_model_S2T', 'r')
        lines = file.readline()
        file.close()
        model = str(lines).replace('\n', '')
    except FileNotFoundError as E:
        print(E)
        model = Model('models/vosk-model-ru-0.42')
    try:
        rec = KaldiRecognizer(model, 16000)
        p = pyaudio.PyAudio()
        stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000)
        stream.start_stream()
        return stream, rec
    except AttributeError as E:
        print(E, '\n T2S не запущено по ранее выставленному пути. Запуск по стандартному пути.')
        model = Model('models/vosk-model-ru-0.42')
        rec = KaldiRecognizer(model, 16000)
        p = pyaudio.PyAudio()
        stream = p.open(format = pyaudio.paInt16, channels = 1, rate = 16000, input = True, frames_per_buffer = 8000)
        stream.start_stream()
        return stream, rec


# запуск приложения
if __name__ == '__main__':
    # тело программы
    say_phrases_engine, voices = settings4say()
    property_voice = voices[0]
    property_voice = property_voice.id
    say_phrases_engine.setProperty('voice', property_voice)
    say_phrases_engine.say('привет, это ваш ассистент, я загружаюсь, ожидайте!')
    say_phrases_engine.runAndWait()
    '''Проверка на наличие базы данных, при обнаружении которой(про удачном реквесте), происходит подключение к ней.
    А если такой базы не существует, то она создаётся, и туда добавляется одна пара(ключ: ззначение), 
    что необходимо для правильной работы программы(def per_com())'''
    data_base_sql3in_code = sqlite3.connect("DataBaseInFiles")
    cursor = data_base_sql3in_code.cursor()
    try:
        cursor.execute("SELECT * FROM AnsvQest")
    except sqlite3.Error:
        cursor.execute("""CREATE TABLE AnsvQest (
            answer city,
            qestion city
        )""")
        cursor.execute("INSERT INTO AnsvQest VALUES ('привет', "
                       "'Привет, как у тебя дела?')")
        cursor.execute("INSERT INTO AnsvQest VALUES ('что такое дивизии 7 на 2', "
                       "'Пехотная дивизия 7/2 в игре Hearts of Iron IV — это шаблон, "
                       "который включает 7 пехотных батальонов и 2 артиллерийских батальона. "
                       "В состав поддержки входят инженерная рота, противотанковая рота, "
                       "рота снабжения, рота ПВО и рота разведки.')")
        cursor.execute("INSERT INTO AnsvQest VALUES ('hi', "
                       "'hello! H R U')")
        cursor.execute("INSERT INTO AnsvQest VALUES ('Hoi 4 divisions 7 by 2 what is it', "
                       "'The 7/2 Infantry Division in Hearts of Iron IV is a "
                       "template consisting of 7 infantry and 2 artillery battalions. "
                       "The division is supported by an engineering company, "
                       "an anti-tank company, a supply company, an air defense company, "
                       "and an intelligence company.')")
    db = cursor.execute("SELECT * FROM AnsvQest").fetchall()
    data_base_sql3in_code.commit()
    app = QApplication([])
    window = ChatBot(form_maker = True)
    window.show()
    stream, rec = settings4recognition()
    # Синтез и распознование речи
    say_phrases_engine.say('говорите')
    say_phrases_engine.runAndWait()
    ChatBot()
    app.exit(app.exec())
