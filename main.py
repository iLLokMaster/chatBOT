import re
import sqlite3
import os
import random
import time
import webbrowser
import speech_recognition

debug = 0                                                                                       #set 1 to turn on debug
DataBaseSQL3inCode = sqlite3.connect("DataBaseInFiles")                                         #connect Data Base
cursor = DataBaseSQL3inCode.cursor()                                                            #create cursor
try:
    cursor.execute("SELECT * FROM AnsvQest")
except sqlite3.Error:
    cursor.execute("""CREATE TABLE AnsvQest (
            answer text,
            qestion text
        )""")                                                                                   ###create table ###perform only for the first time
    cursor.execute("INSERT INTO AnsvQest VALUES ('привет', "
                   "'Привет, как у тебя дела?')")                                                                                                
db = cursor.execute("SELECT * FROM AnsvQest").fetchall()                                        ###select all from Data Base and insert to db
DataBaseSQL3inCode.commit()                                                                     ###commit changes and cloce Data Base
def per_com(list1, list2):                                                                      ###calculation of the percentage of coincidence of the question from the database and the user's question
    common_elements = set(list1) & set(list2)
    percent_match = (len(common_elements) / len(set(list1 + list2))) * 100
    return percent_match
def recp(prompt):
    pers = []
    pr = prompt
    pr = pr.lower()                                                                              #pr = re.sub('\W+',' ', pr )
    for k in range(len(db)):
        list_a = pr
        list_b = db[k][0]                                                                        #list_b = re.sub('\W+',' ', db[k][0] )
        result = per_com(list_a, list_b)                                                         ###result = проценты совпадения
        pers.append([result, db[k][1]])
    sortPers = sorted(pers)
    
    if result == 0:
        print('Я вас не понял(')
        otvet_polzovatelya = input("Ваш ответ: ")
        cursor.execute(f"INSERT INTO AnsvQest VALUES ('{prompt}', '{otvet_polzovatelya}')")
        DataBaseSQL3inCode.commit()
        db.append([prompt, otvet_polzovatelya])
    else:
        print('Ответ бота: ')
        a = sortPers[-1][1]
        b = list(a)
        for alphabet in b:
            print( alphabet,  end='')
            time.sleep(0.01)
        if sortPers[-1][0] != 100:                                                                 ###вам понравился ответ?
            if input('\nВам понравился ответ? [Если да, то введите что-нибудь] [нет = .] ').lower() == '.':
                otvet_polzovatelya = input("\nваш ответ")
                cursor.execute(
                    f"INSERT INTO AnsvQest VALUES ('"
                    f"{prompt}', "
                    f"'{otvet_polzovatelya}')"
                )
                DataBaseSQL3inCode.commit()
                db.append([prompt, otvet_polzovatelya])
                #print(db)
            else:
                cursor.execute(f"INSERT INTO AnsvQest VALUES ('"
                               f"{prompt}', "
                               f"'{sortPers[-1][1]}')")
                DataBaseSQL3inCode.commit()
                db.append([prompt, sortPers[-1][1]])
while True:
    sr = speech_recognition.Recognizer()                                                           ###speech recognition
    sr.pause_threshold = 0.5
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(
            source = mic, 
            duration = 0.5
        )
        audio = sr.listen(source = mic)
        query = sr.recognize_google(
            audio_data = audio, 
            language = 'ru-RU'
        ).lower()     
    prompt = query                                                                                 #= str(input("\nВаш вопрос: ")).lower() and with out "query"
    
    if debug == 1:
        print(prompt)
    if prompt == 'exit' or prompt == 'выход':
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
            'почему ты меня бросаешь? не надо, пожалуйста.(котик с блестящими глазками)''пока', 
            'Приходите пожалуйста поскорее. Я по вам уже скучаю:(', 
            'не оставляйте меня одного на долго','нееееееее...', 
            'не оставляй меня на долго, пожалуйста, я очень тебя прошу'
        ]
        print(good_by[random.randint(0,len(good_by)-1)])
        exit()
    elif prompt == 'db' or prompt == 'ви' or prompt == 'data base' or prompt == 'your data base' or prompt == 'твоя база данных':
        if debug == 1:
            for h in range(len(db)):
                print(db[h])
    elif prompt == 'что ты умеешь':
        print('я умею отвечать на вопросы и постоянно обучаюсь, но не поддерживаю режим диалога. Мои программисты под контролем Прядиева Романа, очень стараются для продвижения проекта, и постоянно его поддерживают. Если вам угодно, вы можете обновить программу(https://github.com/iLLokMaster/chatBOT)')
    elif prompt == 'открой браузер':
        os.system('C:/Users/B-ZONE/AppData/Local/Yandex/YandexBrowser/Application/browser.exe')
        print('на')
    elif prompt == 'какое дз':
        webbrowser.open('https://dnevnik.ru/marks/school/1000009993521/student/1000012990748/current', new=2)
        print('держи')
    elif prompt == 'открой сам пикер':
        os.system('C:/Program Files (x86)/Steam/Steam.exe')
        time.sleep(10)
        os.system('C:/Users/B-ZONE/Desktop/игры/SteamAchievementManager-7.0.25/SAM.Picker.exe')
        print('на')
    else:
        recp(prompt)
