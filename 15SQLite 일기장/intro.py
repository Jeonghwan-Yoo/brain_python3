'''
15.1 데이터베이스에 대해
데이터베이스(Database)는 자료를 저장하고 저장된 자료를 다시 운용하기 위한 목적으로
구축된 시스템.

15.1.1 데이터베이스의 역사
컴퓨터 이전부터도 데이터를 잃어버리기 않기 위해 기록을 해왔다.
컴퓨터가 등장하면서 컴퓨터를 이용해 데이터를 처리하기 시작. 초기 저장매체는 '파일'

계층형/네트워크형 데이터베이스
늘어나는 데이터와 산업 전반에 걸쳐 거대해지는 시스템에 대응하는 사람들은 '데이터 모델'을 사용
현실세계의 데이터를 다시 논리적으로 정의하고 표현하는 방법.
계층형은 데이터가 계층 구조를 이룰 수 있는 경우에 사용되는 시스템
네트워크형은 데이터간의 관계가 네트워크를 이루는 경우에 사용.

관계형 데이터베이스
가장 일반적으로 사용되는 시스템. 데이터의 구조를 테이블로 구성. SQLite

객체 지향 데이터베이스
기존의 데이터베이스 시스템의 문제와 멀티미디어 데이터의 처리를 위해 고안됨.
나중에는 객체 지향 데이터베이스와 관계형데이터베이스의 장점을 결합시킨 객체 관계형이 등장.

15.1.2 DBMS(Database Management System)
데이터베이스의 역할(데이터를 저장하고 운용하게) 그 자체를 수행하는 소프트웨어.
Oracle, SQL Server, MySQL...
DBMS는 대부분의 경우 데이터의 입출력 창구 역할을 하는 응용프로그램과 함께 사용.
DBMS는 저마다 API(Application Programming Interface)를 제공.

15.1.3 관계형 데이터베이스의 기본 구조
관계형 데이터베이스는 데이터베이스가 여러 개의 테이블을 소유하는 형식.
이름, 전화, 이메일 등의 열을 '필드(field)' 실제 데이터를 이루는 각 행은 '레코드'라고합니다.

15.1.4 SQL 익히기
SQL(Structured Query Language)은 관계형 데이터베이스에서 사용하는 질의 언어.
데이터베이스와 테이블의 생성과 수정,삭제 기능부터 데이터의 검색, 추가, 삭제, 수정 등의
데이터 처리 기능을 모두 수행.

SQL연습을 위한 SQLite3셀 내려받기.

테이블의 생성:CREATE TABLE
레코드를 추가하고 조회하는 등의 작업을 하려면 테이블이 있어야 합니다.
CREATE TABLE은 각 필드의 자료형과 크기 등으로 구성된 테이블의 구조를 매개변수로 생성.
CREATE TABLE <테이블> (필드1 필드형식1, 필드2 필드형식2, ...)
테이블을 만들고, 각 레코드를 식별할 수 있는 기본 키(Primary Key)를 지정.
>CREATE TABLE PHONEBOOK (NAME CHAR(32), PHONE CHAR(32), EMAIL CHAR(64) PRIMARY KEY);
>.schema PHONEBOOK으로 테이블의 스키마를 확인.

DROP TABLE
테이블을 삭제하고자 할 때 이용. 매개변수는 삭제할 테이블 이름 뿐.
>DROP TABLE PHONEBOOK;

레코드 추가:INSERT 문
레코드를 테이블에 추가할 때 사용.
INSERT INTO <테이블> ([필드1, 필드2, ...]) VALUES([데이터1, 데이터2,...])
>INSERT INTO PHONEBOOK (NAME, PHONE, EMAIL) VALUES ('박신혜','021-322-1542',
'shinhye@park.com');

기본키 필드에 중복된 값을 넣어 INSERT를 하면 에러가 뜸니다. 항상 UNIQUE해야한다.

레코드 조회:SELECT 문
"<테이블>에서 <필드>를 선택하라"
SELECT <필드> FROM <테이블>
> SELECT NAME FROM PHONEBOOK;
여러 개의 필드를 얻으려면 쉼표(,)를 구분자로.
> SELECT NAME, PHONE FROM PHONEBOOK;
필드 목록을 생략하고 '*'를 입력하면 모든 필드에 대해 조회
> SELECT * FROM PHONEBOOK;

WHERE:특정 조건의 레코드에 대해 작업
<SELECT 문> WHERE <조건>
> SELECT * FROM PHONEBOOK WHERE NAME='박신혜';
텍스트 형식 필드의 경우 값이 일부만 일치하는 레코드를 찾을 수 있습니다.
WHERE 질의 대신 LIKE를 이용하면 됩니다.
> SELECT * FROM PHONEBOOK WHERE PHONE LIKE '021%';
%는 필드의 값이 ~로 시작하는 레코드 조회

ORDER BY:조회 결과의 정렬
조회 결과가 여러 레코드로 구성되어 있을 경우, 특정한 기준으로 정렬.
> SELECT * FROM PHONEBOOK ORDER BY NAME ASC;
NAME필드에 대해 오름차순으로 정렬.
> SELECT * FROM PHONEBOOK ORDER BY NAME DESC;
NAME필드에 대해 내림차순으로 정렬.

레코드 수정:UPDATE 문
테이블에 이미 존재하는 레코드의 특정 필드를 수정할 때 사용합니다.
UPDATE <테이블> Set [필드1]=[데이터1], [필드2]=[데이터2], ... WHERE [조건]
> UPDATE PHONEBOOK SET PHONE='026-333-2424', EMAIL='python@python.org' 
WHERE NAME='이무기';
반드시 WHERE절과 함께 사용해야 합니다. 안쓰면 모든 레코드에 대해 결과를 적용함.

레코드 삭제:DELETE 문
레코드를 삭제할 때 사용합니다.
어느 레코드만 지울 지 WHERE절에 명시. 안쓰면 모든 레코드를 삭제하므로 주의.
DELETE FRO <테이블> WHERE [조건]
> DELETE FROM PHONEBOOK WHERE EMAIL='python@python.org';

15.2 SQLite의 파이썬 API
파이썬3에는 SQLite 라이브러리가 기본 탑재. import sqlite3
1)커넥션(Connection)열기
2)커서(Cursor)열기
3)커서를 이용하여 데이터 추가/조회/수정/삭제
4)커서 닫기
5)커넥션 닫기

DBMS들은 클라이언트 컴퓨터와는 별도의 서버 컴퓨터에 설치하여 사용하는 경우가 많다.
이런 환경에서 클라이언트 컴퓨터에 설치되어 있는 응용프로그램들은 네트워크를 통해
DBMS에 접근합니다.
이 때 DBMS와 응용프로그램간에 형성하는 논리적인 연결을 커넥션이라고 합니다.
SQLite는 파일기반의 임베디드 DBMS이므로 데이터 베이스의 파일을 연다고 생각해도 됨.
커넥션 닫기는 데이터 베이스 파일을 닫는다.
커서는 실질적으로 SQL을 실행하고 그 결과에 대해 후속작업을 할 수 있게 하는 객체.

15.2.1 커넥션 열고 닫기
커넥션은 sqlite3.connect()함수를 이용해 생성.
connect()함수에는 데이터베이스 파일의 경로를 매개변수로 입력합니다.
import sqlite3
conn=sqlite3.connect('test.db') #커넥션 열기. test.db가 있으면 열고 없으면 만듦.
conn.close() #커넥션 닫기.

15.2.2 커서로 작업하기
커서는 커넥션 객체의 cursor()메소드를 이용해 얻을 수 있습니다.
import sqlite3
conn=sqlite3.connet('test.db')
cursor=conn.cursor() #커서 열기
cursor.close() #커서 닫기
conn.close()
커서 객체의 중요한 임무 중 하나는 SQL문을 실행하는 것.
이 임무를 위해 커서는 execute()메소드를 가지고 있습니다.

테이블 생성
test.db파일 안에 PHONEBOOK테이블을 생성.

레코드 추가
execute()메소드는 매개변수 치환 기능을 지원합니다.
일일이 문자열을 결합하는 대신 매개변수 치환기능을 사용하면 좋은 코드.
매개변수를 치환할 부분에 ?를 넣고 ?에 들어갈 매개변수를 튜플 안에 넣어 execute()매개변수로.
cursor.execute("""
INSERT INTO PHONEBOOK (NAME, PHONE, EMAIL) VALUES(?, ?, ?)
""", ('김범수','021-445-2424', 'visual@bskim.com'))
execute사용할 때 문장을 문장에 넣어야 해서 따옴표3개. 
레코드 추가 수정 삭제 등을 실행한 후 에는 반드시 Connection객체의 commit()함수를 불러야.
그렇지 않으면 실제 데이터베이스 파일에는 아무 변경이 이루어지지 않습니다.
데이터의 일관성(Consistency)을 위한 트랜잭션(Transaction)을 지원하기 때문.
execute()메소드를 통해 INSERT문을 실행하고 나면 커서 객체의 lastrowid변수가 갱신됨.
lastrowid는 마지막으로 추가되거나 변경된 레코드의 번호를 나타내며 여러 테이블에 대한
트랜잭션을 수행할 때 사용됩니다.
insert_record.py

레코드 조회
SELECT문을 실행한 후 결과를 얻어올 때는 커서 객체의 fetchone() or fetchall() 이용
fetchone()은 SELECT실행 결과에서 레코드를 하나씩만 가져옵니다.
row=cursor.fetchone()
print(row)
fetchall()은 한 번에 모든 결과 레코드를 가져옵니다.
rows=cursor.fetchall()
for row in rows:
    print("NAME:{0}, PHONE:{1}, EMAIL:{2}".format(row[0],row[1],row[2]))
상황과 용도에 따라 적절하게 골라 사용.
select_record.py

레코드 수정
레코드 추가와 같다.
update_record.py

레코드 삭제
레코드 추가/수정과 동일
delete_record.py

15.3 140자 일기장 만들기
GUI를 가진 일기장 프로그램을 만들기.

15.3.1 140자 일기장이 사용할 테이블 구조
DIARY                          DIARY_IMG
DIARY_ID INTEGER  <----       IMG_ID INTEGER
(Auto)                 |       (Auto)
CREATEDATE DATETIME    |       IMG BLOB
노트 CHAR(140)          -----  DIARY_ID INTEGER


첫 번째 테이블의 이름은 DIARY.
날짜(CREATEDATE)와 일기 텍스트(N O T E) 필드를 가지고 있습니다.
이 두 필드는 레코드의 식별자로써는 문제가 좀 있습니다.
노트필드와 CREATEDATE필드에는 중복되는 내용이 입력될 공산이 크기 때문.
레코드의 식별자로 사용하려면 유일한 값을 가져야 합니다.
SQLite는 테이블에 사용할 마땅한 레코드 식별자가 없는 경우를 위해 자동증가 정수 형식제공
DIARY테이블은 DIARY_ID필드를 기본키로 사용합니다.
DIARY_ID필드는 일기 내용과 관계가 없지만 레코드가 추가될때 자동으로 값이 증가해 식별가능.

두 번째 테이블의 이름은 DIARY_IMG입니다.
일기에 들어갈 이미지를 저장하는 '보조적인'용도로 사용.
이미지는 대개 텍스트에 비해 많은 저장 공간을 요구하는 데이터이므로
IMG필드는 대용량 바이너리 데이터 형식인 BLOB(Binary Large OBject)를 사용.

DIARY테이블과 DIARY_IMG텥이블처럼 필수-보조 역할로 나뉘는 구조를 마스터-디테일관계.
연결고리는 DIARY_ID입니다.
DIARY_IMG테이블은 IMG_ID필드를 기본키로 사용하지만, DIARY테이블에 저장되어 있는
레코드의 기본 키를 가리키기 위한 필드를 가지고 있습니다.
DIARY_IMG의 DIARY_ID필드는 자동으로 입력되지 않아 직접 값을 지정.
마스터 테이블에 데이터를 먼저 추가하고, 이 데이터에서 얻은 키를 이용해
디테일 테이블에 데이터를 그다음에 추가합니다.
DIARY에 레코드 삽입---->DIARY_IMG에 레코드 삽입

15.3.2 사용자 인터페이스
윈도우 왼쪽에는 입력창이 있고 오른쪽에는 일기의 내용을 보여주는 창이 있습니다.
일기 입력창의 StaticBitmap은 이미지를 표시하는 위젯.
이미지를 테이블에 입력하기 전에 미리보기용으로 사용합니다.
일기의 내용을 보여주는 창에 사용한 위젯은 wx.html2.WebView입니다.
이 위젯은 HTML을 렌더링해서 보여주는 기능을 갖는 기능이 한정된 작은 웹브라우저.

15.3.3 140자 일기장 코드
윈도우 하나로 입력과 출력을 모두 수행.
wx.Frame의 파생클래스를 하나 정의하고 아래의 기능을 그 안에 구현.
1)__init__()메소드
2)테이블 생성 기능
3)일기 입력창의 이벤트 처리기
4)이미지 찾기와 미리보기
5)텍스트와 이미지의 데이터베이스 입력
6)일기 텍스트와 이미지 표시.
7)일기 삭제와 다음 페이지 이동
8)140자 일기장 프로그램 기동
140Diary.py

__init__()메소드
위젯을 생성하고, 위젯을 사이저로 배치하고, 데이터를 초기화하는 것.

테이블 생성 기능
CheckSchema()의 역할
커서 객체를 이용해서 두 개의 CREATE TABLE을 실행하며,
그 결과 만들어지는 테이블은 DIARY, DIARY_IMG.

외래키는 다른 테이블에서 기본 키로 사용되고 있는 값을 참조하는 필드.
DIARY테이블에 존재하지 않는 DIARY_ID는 DIARY_IMG테이블에도 저장할 수 없다.

일기 입력창의 이벤트 처리기
일기 내용을 텍스트로 입력할 때 현재 몇 개의 글자가 입력했는지를 실시간으로 알려줌.

이미지 찾기와 미리 보기
이미지 찾기 기능은 [이미지 추가]버튼을 클릭했을 때 파일 대화상자를 띄우고
대화상자에서 사용자가 선택한 파일의 경로를 가져오는 코드를 필요로 합니다.
파일 대화상자는 따로 구현할 필요없이 wx.FileDialog 클래스를 이용하면 구현할 수 있다.
openFileDialog=wx.FileDialog(self,"Open",
wildcard="Image files(*.png,*.jpg,*.gif)|*.png;*.jpg;*.jpeg;*.gif",
style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)
wildcard는 파일 대화상자가 사용자에게 표시할 내용을 결정하는 필터.
'|'왼쪽은 FileDialog하단의 필터 콤보박스에 표시하는 용도로.
오른쪽은 파일 목록에 해당 확장자를 가진 파일만 보여주도록 하는 필터.
style 매개변수는 파일 대화상자에 소소한 변화를 줍니다. 플래그는 5개
wx.FD_OPEN:'열기'모드로 파일 대화상자를 띄웁니다.
wx.FD_SAVE:'저장'모드로 파일 대화상자를 띄웁니다.
wx.FD_OVERWRITE_PROMPT:'저장'모드에서 같은 이름을 가진 파일을 선택했을 때
덮어쓸 것인지를 사용자로부터 확인 받는 대화상자를 띄웁니다.
wx.FD_MULTIPLE:'열기'모드에서 복수 개의 파일 선택을 허용합니다.
wx.FD_CHANGE_DIR:작업 디렉토리를 사용자가 선택한 파일이 있는 곳으로 변경합니다.

미리보기 기능은 먼저 파일 대화상자를 통해 얻어온 경로의 이미지를 wx.Image객체로 읽고,
wx.Image객체가 담고 있는 이미지를 줄이거나 늘여서 표시할 크기에 맞춥니다.
그다음 wx.Image객체를 wx.Bitmap객체의 생성자에 매개변수로 넘기고,
다시 wx.Bitmap객체를 imageStaticBitmap의 비트맵으로 지정합니다.
img=wx.Image(파일 경로, wx.BITMAP_TYPE_ANY)
img=img.Scale(300,200) #300*200크기 변경
#wx.Bitmap객체를 생성하고 이것은 self.imageStaticBitmap의 비트맵으로 지정합니다.
self.imageStaticBitmap.SetBitmap(wx.Bitmap(img)) 

텍스트와 이미지의 데이터베이스 입력
BLOB필드에 이미지를 저장할 때는 sqlite3.Binary()함수를 이용해야만 합니다.
이미지 파일의 내용을 담은 bytes객체를 데이터베이스에 저장하는 코드
self.cursor.execute("""
INSERT INTO DIARY_IMG(IMG_ID,IMG,DIARY_ID) VALUES(NULL,?,?)
""", (sqlite3.Binary(open(self.input_image_path,"rb").read()), diary_id))

일기 텍스트와 이미지 표시
일기 내용을 데이터베이스로부터 읽어와서 HTML로 구성한 후
Webview 위젯을 이용해서 사용자에게 보여주는 코드를 작성하는 것.

일기 삭제와 이전/다음페이지 이동
[삭제][Prev][Next]버튼을 눌렀을 때 EVT_WEBVIEW_NAVIGATING이벤트의 이벤트처리.

'''