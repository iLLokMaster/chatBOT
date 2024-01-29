установка библиотек/install librares
-
    pip install sqlite3
    pip install re

принцип работы/how does it work
-
eng:
As you have already understood, this is a chatbot. My chatbot works on simple human learning and has its own open database. The training takes place by adding data to the database. The project is based on the following method of work, I do not know if it was used before me or not, but I openly declare that the project was developed by me personally, and no one else. Actually, the first lines of the project establish a connection to the database:

    import sqlite3
    DataBaseSQL3inCode = sqlite3.connect("DataBaseInFiles")
    cursor = DataBaseSQL3inCode.cursor()
    
After the connection to the database is established, the db variable (from the English data base) is assigned the value of the database stored in the code. And the changes are saved.

   db = cursor.execute("SELECT * FROM AnsvQest").fetchall()
   DataBaseSQL3inCode.commit()
   
Next, the program functions begin, we will skip them, but then we will return to them. So, we are on line 49 (while True:), here we take the user's message for the chatbot, check for keywords for the program to work (for example, exit).
Next, the program passes the prompt variable with the message to the recp function.
in the lines below, the request is being processed. The query is converted to lowercase and special characters(!,.no."@) are removed.

     pers = []
     pr = prompt
     pr = pr.lower()
     pr = re.sub('\W+',' ', pr )

Next, the processed user's query is checked for similarity with each subsequent one from the first column in the table (db(AnsvQest)).

    for k in range(len(db)):
        list_a = pr
        list_b = re.sub('\W+',' ', db[k][0] )
        result = per_com(list_a, list_b)
        pers.append([result, db[k][1]])

A new table is created in which the obtained results are stored with percentages of coincidence. And they are immediately sorted in descending order of percentages.

     sortPers = sorted(pers)

Well, if the percentage is 0, then the program writes: "I didn't understand you."
otherwise, if the percentage is less than 100, then we ask the user for his answer to his own question, which will be added to the database.

 if result == 0:
print('I didn't understand you')
else:
print(sortPers[-1][1])
 if sortPers[-1][0] != 100:
if input('did you like the answer?[yes = anything][no = .] ').lower() == '.':
otvet_polzovatelya = input("your answer")
db.append([prompt, otvet_polzovatelya])
print(db)

 then the program loops.


рус:
Как ва уже поняли, это чат бот. 
Мой чат бот работает на простом обучении человеком и имеет свою открытую базу данных. 
Обучение происходит методом добавления данных в базу.
Проект основан на следующем методе работы, я не знаю применяли его до меня или нет, но я открыто заявляю что, проект разрабатывался лично мной, и никем более. Собственно первые строки проекта устанавливают соединение с базой данных:

    import sqlite3
    DataBaseSQL3inCode = sqlite3.connect("DataBaseInFiles")
    cursor = DataBaseSQL3inCode.cursor()
    
После устоновки соединения с базой данных, в переменную db(от английского data base) присваивается значение хранимой в коде базы данных. И изменения сохраняются.

    db = cursor.execute("SELECT * FROM AnsvQest").fetchall()
    DataBaseSQL3inCode.commit()
    
Далее начинаются функции программы, мы из пропустим, но потом к ним вернёмся.
Итак, мы на строке 49 (while True:), здесь мы берём у пользователя его сообщение для чат бота, проверяем на ключевые слова для работы программы(например exit).
Далее программа передаёт переменную prompt с сообщением в функцию recp.
в строках ниже запрос обрабатывается. Запрос переделывается в нижний регистр и убираются специальные символы(!,.№"@).

    pers = []
    pr = prompt
    pr = pr.lower()
    pr = re.sub('\W+',' ', pr )

Далее обработанный запрос польнователя проверяется на схожесть с каждым последующим из первого столбца в таблице(db(AnsvQest)).

    for k in range(len(db)):
        list_a = pr
        list_b = re.sub('\W+',' ', db[k][0] )
        result = per_com(list_a, list_b)
        pers.append([result, db[k][1]])
        
Создаётся новая таблица, в которой хранятся полученные результаты с процентам совпадения. И сразу сортируются по убыванию процентов.

    sortPers = sorted(pers)

Ну и если процент равет 0, то программа пишет: "я вас не понял".
иначе, если процент меньше 100, то просим у пользоватея его ответ на свойже вопрос, который добавится в базу данных.

    if result == 0:
        print('я вас не понял')
    else:
        print(sortPers[-1][1])
        if sortPers[-1][0] != 100:
            if input('вам понравился ответ?[да = anything][нет = .] ').lower() == '.':
                otvet_polzovatelya = input("ваш ответ")
                db.append([prompt, otvet_polzovatelya])
                print(db)

 далее программа зацикливается.
 
ближайшие планы на проект/immediate plans for the project 
-
    -сделать граффическую оболочку;
    -сделать поддержку режима диалога;
    -сделать сохранение базы данных в облаке;
    -сделать голосовой ввод;
    -сделать воспроизведение ответа голосом;
    -обучать ИИ

    -make a graffiti wrapper;
    -make dialog mode support;
    -save the database to the cloud;
    -make voice input;
    -make a voice response playback;
    -train AI
