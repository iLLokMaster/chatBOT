import re
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
        print('я вас не понял')
    else:
        print(sortPers[-1][1])
        if sortPers[-1][0] != 100:
            if input('вам понравился ответ?[да = anything][нет = .] ').lower() == '.':
                otvet_polzovatelya = input("ваш ответ")
                cursor.execute(f"INSERT INTO AnsvQest VALUES ('{prompt}', '{otvet_polzovatelya}')")
                DataBaseSQL3inCode.commit()
                db.append([prompt, otvet_polzovatelya])
                print(db)
            #вам понравился ответ?

while True:
    prompt = str(input("your prompt: "))
    if prompt == 'exit':
        DataBaseSQL3inCode.close()
        print('пока')
        exit()
    recp(prompt)
