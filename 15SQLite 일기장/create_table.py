import sqlite3

conn=sqlite3.connect('test.db')
cursor=conn.cursor()
#test.db 안에 PHONEBOOK 테이블을 생성합니다.
cursor.execute("""
CREATE TABLE PHONEBOOK (NAME CHAR(32), PHONE CHAR(32), EMAIL CHAR(64) PRIMARY KEY)
""")

cursor.close()
conn.close()