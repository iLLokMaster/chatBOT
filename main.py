import re
import sqlite3 as sql
con = sql.connect('bod.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS `BOD` (`question` STRING, `answer` STRING)")
def SAL_ALL():
    cur.execute("SELECT * FROM BOD")
    return cur.fetchall()
def L_F_SQL(q_p):
    if q_p == 1:
        q = 'answer'
    else:
        q = 'question'
    ques = con.execute(f'SELECT * FROM bod WHERE question ={q}').fetchone()
    return ques
def per_com(list1, list2):
    common_elements = set(list1) & set(list2)
    percent_match = (len(common_elements) / len(set(list1 + list2))) * 100
    return percent_match
def recp(prompt):
    pers = []
    pr = prompt
    pr = pr.lower()
    pr = re.sub('\W+',' ', pr )
    for k in range(len(SAL_ALL())):
        list_a = pr
        list_b = re.sub('\W+',' ', L_F_SQL(0)[k])
        print(list_b)
        result = per_com(list_a, list_b)
        pers.append([result, L_F_SQL(1)[k]])
    sortPers = sorted(pers)
    if result == 0:
        print('я вас не понял')
    else:
        print(sortPers[-1][1])
        if sortPers[-1][0] != 100:
            if input('вам понравился ответ?[да][нет] ').lower() == 'нет':
                cur.execute(f"INSERT INTO `BOD` VALUES ('{pr}', '{input('введите свой вариант ответа: ')}')")
                print(SAL_ALL())

while True:
    prompt = str(input("your prompt: "))
    if prompt == 'exit':
        print('пока')
        con.commit()
        cur.close()
        exit()
    print(prompt)
    recp(prompt)

