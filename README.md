[https://docs.google.com/presentation/d/1QbgpwSHkX0T0qiBFiA5IJRv1VEkjGxnLVhoZK7vk56w/edit#slide=id.g3170a74bc6c_0_160](https://docs.google.com/presentation/d/1QbgpwSHkX0T0qiBFiA5IJRv1VEkjGxnLVhoZK7vk56w/edit?usp=sharing)

![iStock-927504604](https://github.com/iLLokMaster/chatBOT/assets/130349746/ae1d948f-3f1b-436c-9b82-bc62b59ee63b)
для чего нужен этот проект?
-
В первую очередь он нужен для помощи в управлении играми. Он помогает отвечать на уже известные или похожие вопросы по играм, сам умеет управлять играми, то есть будет нажимать на кнопки, когда вы дадите ему команду. Это хорошая функция для игр, в которых не требуется постоянное вмешательство пользователя.

ссылки на модели/models
-
Большая модель/big:[https://vk.com/away.php?to=http%3A%2F...](https://vk.com/away.php?to=http%3A%2F%2Falphacephei.com%2Fkaldi%2Fmodels%2Fvosk-model-ru-0.10.zip&cc_key)
Маленькая модель/small: https://vk.com/away.php?to=https%3A%2...

Какие применялись технологии?
-
В рамках данного проекта были задействованы передовые технологии машинного обучения, включая распознавание речи и синтез речи, а также другие инновационные решения.
Примечательно, что в настоящее время текст создаётся моим собственным ботом, который генерирует его на основе моей диктовки. Конечно, он пока не способен расставлять знаки препинания, но это уже значительный шаг вперёд. 

интерфейс программы
-
Интерфейс моей программы отличается простотой и лаконичностью. В главном окне располагается сам чат, а также поле для ввода текста и кнопка отправки.
На следующей вкладке находятся настройки. При открытии этой вкладки появляются ещё две. Первая предназначена для простых пользователей и не содержит настроек, способных повлиять на работу программы или сломать её. Вторая же предоставляет более широкий спектр возможностей, включая настройку пути к файлам и другие параметры. 

функции чат бота
-
Как уже упоминалось ранее, бот способен выполнять различные действия по команде пользователя. В частности, он может:

1) Предоставлять информацию о погоде.
2) Изменять свои настройки с помощью голосовых команд.
3) Открывать браузер.
4) Переходить на различные веб-сайты.
5) Оказывать помощь в играх.
6) Запускать приложения.
7) Искать и воспроизводить информацию из интернета.
8) Анализировать вопросы пользователя и предоставлять ответы на них, используя базу данных или создавая новые.
   
Важно отметить, что бот будет запрашивать ответ на вопрос только в том случае, если пользователь включил эту функцию в настройках.
Эти функции представляют собой лишь малую часть возможностей программы. 

установка библиотек/install librares
-
    pip3 install asttokens attrs backcall beautifulsoup4 bleach certifi cffi charset-normalizer colorama decorator defusedxml docopt executing fastjsonschema idna ipthon jedi Jinja2 jsonschema jsonschema-specifications jupyter_client jupyter_core jupyterlab_pygments MarkupSafe matplotlib-inline mistune nbclient nbconvert nbformat packaging pandocfilters parso pickleshare pipreqs platformdirs prompt_toolkit pure_eval PyAudio pycparser Pygments PyQt5 PyQt5-Qt5 PyQt5-sip python-dateutil pywin32 pyzmq referencing requests rpds-py srt stack-data tinycss2 tornado tqdm traitlets typing_extensions urllib3 vosk wcwidth webencodings websockets yarg
    
https://docs.python.org/3/library/sqlite3.html

https://docs.python.org/3/library/re.html

https://pypi.org/project/SpeechRecognition/

https://github.com/sveinse/pyaudio

https://github.com/alphacep/vosk-api

https://github.com/MatteoBartoli03/requestsPython

https://pyautogui.readthedocs.io/en/latest/

https://github.com/pykaldi/pykaldi
    
Для обычных пользователей бета версии/For regular beta users
-
Для пользователей бета-версии:

1) Скачайте Python (https://www.python.org/) и, по желанию, среду разработки, например, PyCharm (https://www.jetbrains.com/pycharm/download/other.html), рекомендую версию не выше 2023.2.5.
2) Поместите файлы проекта в удобную для вас папку.
3) Откройте main.py в PyCharm (или в среде разработки, которую вы установили).
4) Если вы хотите, чтобы у вас открывались Steam, Discord, браузер и т. д., то по этому пути («C:\steeeem») разместите ярлыки на программы.
5) Запускайте!

Если на момент чтения в файлах проекта есть какой-либо файл с расширением .exe, то просто установите его вместе с базой данных и остальными необходимыми файлами.

============================================================================================

Eng:
1)download the project, namely the DataBase In Files and main.py . Download python(https://www.python.org /) and (optionally) a development environment, for example PyCharm(https://www.jetbrains.com/pycharm/download/other.html ) I recommend a version no higher than 2023.2.5, newer versions are paid.

2)Put the project files in one folder convenient for you.

3)Open main.py as PyCharm (or the development environment that you have installed)

4) Run!
5) 
!!!!!!IF THERE IS ANY FILE WITH THE .exe EXTENSION IN THE PROJECT FILES AT THE TIME OF READING, THEN JUST INSTALL IT ALONG WITH THE DATABASE!!!

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
Как вы уже, вероятно, догадались, это чат-бот.
Мой чат-бот функционирует на основе простого обучения человеком и обладает собственной открытой базой данных. Обучение осуществляется путём добавления данных в эту базу.
Проект основан на уникальном методе работы, который, насколько мне известно, не применялся ранее. Однако я открыто заявляю, что проект был разработан мной лично и никем более.
Первые строки проекта устанавливают соединение с базой данных.

    import sqlite3
    DataBaseSQL3inCode = sqlite3.connect("DataBaseInFiles")
    cursor = DataBaseSQL3inCode.cursor()
    
После устоновки соединения с базой данных, в переменную db(от английского data base) присваивается значение хранимой в коде базы данных. И изменения сохраняются.

    db = cursor.execute("SELECT * FROM AnsvQest").fetchall()
    DataBaseSQL3inCode.commit()
    
Далее следуют функции программы, которые мы временно оставим без внимания, но впоследствии к ним вернёмся.
Итак, мы находимся на строке while True: здесь мы запрашиваем у пользователя сообщение для чат-бота и проверяем его на наличие ключевых слов, необходимых для работы программы (например, exit).
Затем программа передаёт переменную prompt с сообщением в функцию recp.
В следующих строках запрос обрабатывается. Запрос преобразуется в нижний регистр, и из него удаляются специальные символы (!, №, @).

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

В случае, если процент равен нулю, программа выдаёт сообщение: «Я вас не понял».
Если же процент меньше ста, то программа запрашивает у пользователя ответ на вопрос, который затем добавляется в базу данных.

    if result == 0:
        print('я вас не понял')
    else:
        print(sortPers[-1][1])
        if sortPers[-1][0] != 100:
            if input('вам понравился ответ?[да = anything][нет = .] ').lower() == '.':
                otvet_polzovatelya = input("ваш ответ")
                db.append([prompt, otvet_polzovatelya])
                print(db)

 Далее программа зацикливается.
 
ближайшие планы на проект/immediate plans for the project 
-
Ru:
1)  Обеспечить поддержку режима диалога.
2)  Реализовать функцию сохранения базы данных в облачном хранилище.
3)  Обучить искусственный интеллект.
4)  Организовать чтение данных из быстрых ответов Яндекса.

Eng:
1)  Provide support for the dialog mode.
2)  Implement the function of saving the database to the cloud storage.
3)  Train artificial intelligence.
4)  Organize reading data from Yandex \ quick responses.

Если вы нашли баг(ошибку в программе)
-
У вас есть несколько вариантов:
1) связаться со мной (https://tapy.me/illok);
2) вспомнить мемчик (да ладно, и так сойдёт!);
2) исправить самому и создать в проекте новую ветку.

Если вы захотели стать разработчиком проекта/If you want to become a project developer
-
У вас есть варианты:

    -связаться со мной(https://tapy.me/illok)
    -делать самому новые ветки в проекте

You have options:

    -contact me(https://rape.me/ilook )
    -make new branches in the project yourself

