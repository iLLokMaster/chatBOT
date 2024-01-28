Как ва уже поняли, это чат бот. 
Мой чат бот работает на простом обучении человеком и имеет свою открытую базу данных. 
Обучение происходит методом добавления данных в базу.
Проект основан на следующем методе работы, я не знаю применяли еге до меня или нет, но я открыто заявляю что, проект разрабатывался лично мной, и никем более. Собственно первые строки проекта устонавливают соединение с базой даннных:
import sqlite3
DataBaseSQL3inCode = sqlite3.connect("DataBaseInFiles")
    ###create cursor
cursor = DataBaseSQL3inCode.cursor()
    ###create table
    ###perform only for the first time
# cursor.execute("""CREATE TABLE AnsvQest (
#     answer text,
#     qestion text
# )""")
#cursor.execute("INSERT INTO AnsvQest VALUES ('привет', 'Привет, как у тебя дела?')")
    ###select all from Data Base and insert to db
db = cursor.execute("SELECT * FROM AnsvQest").fetchall()
    ###commit changes and cloce Data Base
DataBaseSQL3inCode.commit()
#DataBaseSQL3inCode.close()
