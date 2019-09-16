import sqlite3

conn=sqlite3.connect('test.db')
cursor=conn.cursor()

cursor.execute("""SELECT NAME, PHONE, EMAIL FROM PHONEBOOK""")

#하나만 튜플로
one=cursor.fetchone()
print(one)

#다음 커서부터 모든것을 리스트로
rows=cursor.fetchall()

for row in rows:
    print("NAME:{0}, PHONE:{1}, EMAIL:{2}".format(row[0],row[1],row[2]))

cursor.close()
conn.close()

