import re
import sqlite3
import os
import random
import time
import webbrowser
#connect Data Base
DataBaseSQL3inCode = sqlite3.connect("DataBaseInFiles")
#create cursor
cursor = DataBaseSQL3inCode.cursor()
try:
    cursor.execute("SELECT * FROM AnsvQest")
except sqlite3.Error:
    ###create table
    ###perform only for the first time
    cursor.execute("""CREATE TABLE AnsvQest (
            answer text,
            qestion text
        )""")
    cursor.execute("INSERT INTO AnsvQest VALUES ('привет', 'Привет, как у тебя дела?')")
###select all from Data Base and insert to db
db = cursor.execute("SELECT * FROM AnsvQest").fetchall()
    ###commit changes and cloce Data Base
DataBaseSQL3inCode.commit()
###body of programm
def per_com(list1, list2): #calculation of the percentage of coincidence of the question from the database and the user's question
    common_elements = set(list1) & set(list2)
    percent_match = (len(common_elements) / len(set(list1 + list2))) * 100
    return percent_match
def recp(prompt):
    pers = []
    pr = prompt
    pr = pr.lower()
    pr = re.sub('\W+',' ', pr )
    for k in range(len(db)):
        list_a = pr
        list_b = re.sub('\W+',' ', db[k][0] )
        result = per_com(list_a, list_b)
        pers.append([result, db[k][1]])
    sortPers = sorted(pers)
    #result = проценты совпадения
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
            print(alphabet, end='')
            time.sleep(0.01)

        if sortPers[-1][0] != 100:
            if input('\nВам понравился ответ? [Если да, то введите что-нибудь] [нет = .] ').lower() == '.':
                otvet_polzovatelya = input("\nваш ответ")
                cursor.execute(f"INSERT INTO AnsvQest VALUES ('{prompt}', '{otvet_polzovatelya}')")
                DataBaseSQL3inCode.commit()
                db.append([prompt, otvet_polzovatelya])
                #print(db)
            #вам понравился ответ?
            else:
                cursor.execute(f"INSERT INTO AnsvQest VALUES ('{prompt}', '{sortPers[-1][1]}')")
                DataBaseSQL3inCode.commit()
                db.append([prompt, sortPers[-1][1]])
while True:

    
    prompt = ''
    aai.settings.api_key = "35b431952e5c4660adb43c39b15ce663" # Replace with your API key
    FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
    config = aai.TranscriptionConfig(speaker_labels=True)
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(
        FILE_URL,
        config=config
    )
    for utterance in transcript.utterances:
        prompt += utterance.text
    print(f"вы сказали: {prompt}")

    
    #prompt = str(input("\nВаш вопрос: "))
        if prompt == 'exit' or prompt == 'выход':
        print('     сохраняем изменения в базе')
        try:
            DataBaseSQL3inCode.close()
            print('     изменения сохранены')
        except sqlite3.Error as e:
            print("     не удалось сохранить изменения")
            error_code = e.args[0]
            print(f"     Error code: {error_code}")
        good_by = ['почему ты меня бросаешь? не надо, пожалуйста.(котик с блестящими глазками)''пока', 'Приходите пожалуйста поскорее. Я по вам уже скучаю:(', 'не оставляйте меня одного на долго','нееееееее...', 'не оставляй меня на долго, пожалуюста, я очень тебя прошу']
        print(good_by[random.randint(0,len(good_by)-1)])
        exit()
    elif prompt == 'db'.lower() or prompt == 'ви'.lower() or prompt == 'data base'.lower() or prompt == 'your data base'.lower() or prompt == 'твоя база данных'.lower():
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
