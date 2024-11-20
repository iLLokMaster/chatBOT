![iStock-927504604](https://github.com/iLLokMaster/chatBOT/assets/130349746/ae1d948f-3f1b-436c-9b82-bc62b59ee63b)
для чего нужен этот проект?
-
В первую очередь, он нужен для помощи управления в играх. Он помогает отвечать на уже известные или похожие вопросы по играм, сам умеет управлять играми, то есть будет тыкать по кнопкам, когда вы дали ему комманду. Это хорошая функция для игр, в которых не требуется постояное вмешательство пользователя.

ссылки на модели/models
-
Большая модель/big:[https://vk.com/away.php?to=http%3A%2F...](https://vk.com/away.php?to=http%3A%2F%2Falphacephei.com%2Fkaldi%2Fmodels%2Fvosk-model-ru-0.10.zip&cc_key)
Маленькая модель/small: https://vk.com/away.php?to=https%3A%2...

Какие применялись технологии?
-
в этом проекте применялись технологии машинного обучения, технологии распознавания речи, технологии синтеза речи и многие другие.
что интересно этот текст сейчас пишет мой же бот под диктовку. конечно он не расставляет знаки препинания, но что сейчас есть тоже уже отлично! 

интерфейс программы
-
интерфейс моей программы очень простой. на главном окне находится сам чат, также на этом окне вы можете увидеть поле ввода текста и кнопку отправки. на следующей одноимённой вкладке находятся настройки. при открытии вкладки настройки появляются ещё две вкладки. первая вкладка так называется для простого пользователя, в этой вкладке нет каких-либо настроек которые могут значительно повлиять на работу или сломать программу. во второй вкладке уже есть больше настроек, среди них находится как и собственный путь к расположению файлов так и другие различные настройки. 

функции чат бота
-
как уже упоминалось выше бот умеет писать под диктовку. (этот текст все ещё пишется этим же ботом под диктовку) 
1) бот умеет говорить погоду.
2) умеет голосовыми командами менять свои же настройки
3) открывать браузер
4) открывать различные сайты
5) помогать в играх
6) открывать различные приложения
7) искать и воспроизводить информацию из интернета
8) и самая главная функция. если бот не видит среди списка выше ни каких команд, то он сам начинает обрабатывать вопрос, если же такой вопрос есть в базе данных его кто-то другой уже задавал, то бот без проблем ответит на него, если есть похожий вопрос, бот ответит вам, ссылаясь на похожий вопрос, и спросит понравился ли вам ответ. если же похожего вопроса вообще нет в базе данных, тобот без замедления спросит у вас ответа на этот вопрос.
   !!!обратите внимание, что бот у вас будет спрашивать ответ на ваш вопрос только если вы включили это в настройках.
   это были основные функции этой программы, под большинством из этих пунктов скрываются куда большие большие возможности. 

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
1)скачайте проект. Скачайте python(https://www.python.org/) и (по желанию ) среду разработки, к примеру PyCharm(https://www.jetbrains.com/pycharm/download/other.html)советую версию не выше 2023.2.5.

2)поместите файлы проекта в одной удобной для вас папке.

3)откройте main.py как PyCharm(или средой разработки которую вы устоновили)

4) если вы хотите, что бы у вас открывался стим, дискорд, браузер и тд, то по этому пути('C:/steeeem') разместите ярлыки на программы.
4)запускайте!

!!!ЕСЛИ НА МОМЕНТ ЧТЕНИЯ В ФАЙЛАХ ПРОЕКТА ЕСТЬ КОКОЙ ЛИБО ФАЙЛ С РАСШИРЕНИЕМ .exe, ТО ПРОСТО УСТАНОВИТЕ ЕГО ВМЕСТЕ С БАЗОЙ ДАННЫХ И ОСТАЛЬНЫМИ НЕОБХОДИМЫМИ ФАЙЛАМИ!!!

============================================================================================


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
    
Далее начинаются функции программы, мы их пропустим, но потом к ним вернёмся.
Итак, мы на строке (while True:), здесь мы берём у пользователя его сообщение для чат бота, проверяем на ключевые слова для работы программы(например exit).
Далее программа передаёт переменную prompt с сообщением в функцию recp.
в строках ниже запрос обрабатывается. Запрос опускается в нижний регистр и в нём убираются специальные символы(!,.№"@).

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
    -сделать поддержку режима диалога;
    -сделать сохранение базы данных в облаке;
    -обучать ИИ
    -чтение данных из быстрых ответов яндекса

    -make dialog mode support;
    -save the database to the cloud;
    -train AI

Если вы нашли баг(ошибку в программе)
-
У вас есть варианты:

    -связаться со мной(https://tapy.me/illok)
    -вспомнить мемчик(да ладно, и так сойдёт!!!)
    -исправить самому, и создать в проекте новую ветку.

Если вы захотели стать разработчиком проекта/If you want to become a project developer
-
У вас есть варианты:

    -связаться со мной(https://tapy.me/illok)
    -делать самому новые ветки в проекте

You have options:

    -contact me(https://rape.me/ilook )
    -make new branches in the project yourself

