'''
12.1 threading.Timer
threading.Timer는 일정 주기마다 함수를 실행하는 기능을 가진 클래스.
인스턴스를 만들 때 함수와 그 함수를 실행할 주기를 매개변수로 주면 시간이 만료될 때마다 실행.
sleep(시간)->함수 실행하는 식.
import threading

def function_a():
    timer=threading.Timer(30,functoin_a)
    timer.start()
주기 30초, 실행할 함수는 function_a()를 매개변수.

Timer객체의 start() 메소드를 호출했을 때 시간 만료 이벤트는 단 한 번만 일어납니다.
그래서 주기적으로 시간 만료 이벤트를 발생시키려면 이벤트 처리 코드의 마지막에
Timer객체를 새로 생성하고 기동(start())해주는 코드를 추가해야 합니다.
start()메소드를 호출함으로써 30초마다 자신을 호출하도록 하고 있습니다.
function_a()처럼 다른 코드가 대리 실행하는 함수를 콜백함수(Callback Function)
Timer를 콜백함수 안에서 실행할 필요없고,
안에서 실행하는 이유는 콜백 함수를 주기적으로 반복해서 실행하기 용이해서.
TimerOnce.py

12.1.1 Timer 객체의 시작과 종료
Timer 객체가 임무를 시작하게 하려면 start()메소드를, 종료하려면 cancel()메소드를 호출.
TimerStartCancel.py

start()호출 후 cancel()메소드 호출(비효율)    count가 10이되면 아예 start()호출 안하기
timer=threading.Timer(1, on_timer)          if count<10:
timer.start()                                   timer=threading.Timer(1, on_timer)
                                                timer.start()
if count==10:
    print("Canceling timer...")
    timer.cancel()

12.1.2 Timer 콜백 함수에 매개 변수를 넘기는 방법
Timer생성자의 매개변수 중 args는 Timer 객체가 실행할 콜백 함수의 매개변수로 이용.
timer=threading.Timer(1, on_timer, args=[count]) #args는 리스트 형식
timer.start()
TimerParameter.py

12.2 OAuth 이해하기
OAuth는 사용자를 대신해서 트위터의 API를 호출할 수 있는 허가증을 얻는 절차.
트위터 API와 이 API를 호출하는 데 필요한 라이브러리는 쉽게 잘 만들어져 있다.
도용방지하려면 애플리케이션이 사용자의 ID와 암호는 모르지만 해당 사용자가 서비스를 이용.
이 모순을 풀어내는 방법이 OAuth입니다.
OAuth(Open Standard for Authorization)는 인가를 위한 개방형 표준규약입니다.
그 밖에 다른 회사가 자사의 인터넷 서비스 API에 접근할 수 있는 권한을
서드 파티 애플리케이션 제작자에게 위임하는 방법으로 OAuth를 채택하고 있다.
인가는 "어떤 일을 하는 데 있어서 필요한 권한을 부여하고 허락한다"
OAuth는 서비스 제공업체가 애플리케이션에게 필요한 권한을 사용자로부터 인가를
얻어 동작할 수 있도록 하는 절차를 정의하고 있습니다.
이번 프로그램이 바로 컨슈머(서드 파티 애플리케이션)에 해당
사용자는 해당 서비스에 가입되어 있는 이용자, 나.
서비스 제공업체(트위터)

OAuth 1.0a의 인가 과정은 컨슈머에게 서비스 제공업체의 API를 사용하는 데
필요한 허가증, '액세스 토큰'을 획득하는 과정입니다.
                           컨슈머                서비스 제공업체
"요청토큰획득"         "요청 토큰"요청   ------->  "요청 토큰"발급
                            v--------------------'           
"요청토큰"에 대한      사용자를 서비스
사용자의 인가          제공업체 페이지로  ------->  사용자 인가 획득                   
                      이동시킴                         |
                                                 사용자를 컨슈머
                                                 앱으로 이동시킴
                           v---------------------'
"엑세스 토큰"         "액세스 토큰"  ------------>  "액세스 토큰"
획득                  요청                         발급
                                v-----------------'
                      사용자에게 제공하는
                      서비스 이용          

'뻐꾸기 시계 트위터 봇'은 사용자의 개입 없이 동작할 필요가 있습니다.
최종적으로 획득하게 되는 액세스 토큰을 사전에 미리 코드 안에 입력하는 방법을 이용.

12.3 트위터로 애플리케이션 관리 페이지에서 컨슈머 키/액세스 토큰 얻기
1)계정 생성
2)트위터 애플리케이션 정보를 등록
3)항목을 입력 후 동의.
4)트위터 애플리케이션이 등록되면 정보가 나타납니다.
<Application Settings>에 컨슈머 키가 발급된거 확인.
5)트윗을 남길 수 있게 Access level을 Read and Write로 변경.
6)보통의 트위터 애플리케이션은 트위터 API에 접근하기 위한 액세스 토큰을
트위터에게 요청하는 과정을 거치지만,
우리가 만들 것은 각자의 계정으로만 동작할 것이므로 관리 페이지에서 수동으로
발급받는 액세스 토큰을 이용합니다.
[Keys and Access Tokens]->[Create my access token]:컨슈머 키와 액세스 토큰 확인.

12.4 Tweepy:파이썬을 위한 트위터 라이브러리
파이썬용 트위터 라이브러리를 공개해줍니다. Tweepy(github.com/tweepy)를 이용합니다.

12.4.1 Tweepy 설치
설치하려면 인터넷에 연결돼 있어야 합니다. cmd띄우고 'pip install tweepy'입력
pip 명령이 Tweepy 라이브러리를 자동으로 내려받고 site-packages에 설치합니다.
설치 후에 디렉토리에 가서 설치 되어있는지 확인.

pip(Python Package Index)는 파이썬으로 작성된 소프트웨어를 설치하고 관리하는 시스템.
파이썬의 기본 패키지에 포함됩니다. 안돼있으면 pip을 따로 설치.

12.4.2 Tweepy 테스트
OAuthHandler():트위터 인가를 수행하는 auth.OAuthHandler 클래스의 인스턴스 반환.
auth.OAuthHandler.set_access_token():auth.OAuthHandler 객체에 액세스 토큰을 지정
API():타임라인 읽기, 트윗, 리트윗, DM 등의 기능이 있는 API클래스 인스턴스를 반환.
API.home_timeline([since_id][,max_id][,count][,page]):현재 사용자의 타임라인을 읽음.
API.update_status(status[,in_reply_to_status_id][,lat][,long]
[,source][,place_id]):트윗을 포스트합니다.
tweepy_test.py

12.5 뻐꾸기 시계 트위터 봇 코딩하기
cuckoo_bot.py




'''