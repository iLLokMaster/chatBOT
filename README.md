Как ва уже поняли, это чат бот. 
Мой чат бот работает на простом обучении человеком и имеет свою открытую базу данных. 
Обучение происходит методом добавления данных в базу.
Проект основан на следующем методе работы, я не знаю применяли еге до меня или нет, но я открыто заявляю что, проект разрабатывался лично мной, и никем более. Собственно первые строки проекта устонавливают соединение с базой даннных:

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
