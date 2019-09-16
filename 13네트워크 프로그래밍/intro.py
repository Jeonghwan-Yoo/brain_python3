'''
파이썬은 HTTP, FTP, SMTP, POP3, Telnet 등 프로토콜을 구현한
다양한 인터넷 라이브러리를 제공합니다.

13.1 네트워크 프로그래밍에 앞서 알아둬야 할 기초
13.1.1 인터넷의 유래
네트워크(Network)는 어떤 물건이나 사람 등의 상호 연결되어 있는 체계.
지금 네트워크는 컴퓨터들이 상호 연결되어 있는 '컴퓨터 통신 네트워크'

예전에는 컴퓨터 사용방식은 중앙 컴퓨터에 더미 터미널 여러 개를 연결하는 것.
더미 터미널은 연산 능력은 전혀 없지만, 입력과 출력을 할 수 있는 기능.
중앙 컴퓨터와 '데이터를 주고 받는 기능' 이 큰 의미.

1958년 미국은 선진 기술 개발을 위해 DARPA를 만들고 
네트워크와 네트워크를 연결하는 방법을 구상하게 됩니다.
한쪽 네트워크에 접속한 사용자는 다른 네트워크에 있는 컴퓨터에 접근할 수 있습니다.
그 네트워크를 통해 또 다른 네트워크에도 접근 가능.
최소한의 비용으로 연구소들의 컴퓨터를 연결, 중복투자를 줄일 수 있고 자료를 빠르게 획득.
DARPANET이라고 불리던 네트워크는 연구기관들과 민간까지 연결되더니 1980년대 말에
인터넷이라고 하는 국제 통신망을 형성하게 됩니다.

13.1.2 TCP/IP 스택
컴퓨터끼리 네트워크에서 데이터를 주고 받으려면 그 네트워크에서 통용되는
'프로토콜(Protocol)'을 따라야 합니다.
즉, 컴퓨터들이 네트워크를 통해 데이터를 주고받기 위한 '통신 규약'

인터넷은 가장 큰 네트워크지만, 이외에도 다양한 통신 네트워크가 있습니다.
프로토콜에도 굉장히 다양한 종류가 있습니다.
TCP/IP가 실질적인 인터넷 표준 프로토콜로 자리잡습니다.
예로, 물리적인 통신 선로의 재질, 1:1 1:N N:N네트워크에서 상대를 어떻게 판단하는가,
바이트 오더에 대한 규칙 등 다양한 규칙의 범위.

TCP/IP는 인터넷에서 데이터를 주고 받는데 필요한 일련의 프로토콜 모음(Suite)
TCP/IP스택은 4개의 계층
Application Layer
Transport Layer
Internet Layer
Link Layer
링크 계층은 물리 계층, 네트워크 접속 계층, 미디어 접근 계층 등으로 불리우기도 합니다.

RFC(Request For Comment) 인터넷국제표준화기구에 의해 발행되는 메모.
인터넷 협회를 통해 RFC형태로 발행해 다른 전문가들의 검토를 받을 수 있게 하는것.
이후에 IETF에 의해 인터넷 표준으로 인정되기도 합니다.

링크 계층
TCP/IP는 네트워크의 물리적인 구성으로부터 독립적인 프로토콜.
무선이든 유선이든 다 연결할 수 있는게 링크 계츠에서 네트워크의 물리적인 연결 매체를 통해
패킷을 주고 받는 작업을 담당해주기 때문에 가능.
이 패킷에서 물리적 데이터 전송에 사용되던 부분을 제거하고 인터넷 계층에 넘깁니다.

패킷(Packet)
네트워크를 통해 오고 가는 데이터를 일컬어 '패킷'이라고 합니다.
패킷은 내용물+포장지.
포장지는 안전하게 보호하고 주소를 기입하기 위해 사용.
각 계층이 모두 패킷의 포장지여서 보낼 때는 각 계층에서 포장을 하고 받을 때는 포장을 뜯음.

인터넷 계층
패킷을 수신해야 할 상대의 주소를 지정하고, 나가는 패킷에 대해서는 적절한 크기로
분할하며 들어오는 패킷에 대해서는 재조립을 수행.
여기서 사용되는 규약이 인터넷 프로토콜(IP)입니다.
내보낸 패킷을 상대방이 잘 수령했는지에 대해 전혀 보장하지 않습니다.
파악하는 기능 자체가 없습니다.
그저 전송 계층에서 내려온 패킷에 주소를 붙여 네트워크 계층으로 보내기만 함.
여기에 사용하는 주소 체계가 바로 IP 주소.

전송 계층
패킷의 '운송'을 담당하는 프로토콜들이 정의되어 있습니다.
전송제어프로토콜(TCP)는 송신측과 수신측 간의 연결성을 제공하며,
신뢰할 수 있는 패킷 전송 서비스를 제공합니다.
여러 개의 패킷을 송신하는 경우 패킷 사이의 순서를 보장하며,
패킷이 유실되면 재전송을 해주기까지 합니다.
TCP는 IP가 제공하지 않는 연결성, 신뢰성을 제공합니다.
웹문서를 전달하는 기능을 하는 HTTP를 비롯한 많은 응용프로토콜이 TCP/IP위에서 동작.

TCP는 연결성과 신뢰성을 제공하느라 성능에서 손실을 봅니다.
데이터가 큰 경우에 여러 개의 패킷에 나눠 순서대로 보냄.
작고 전송 신뢰성을 요구하지 않는 데이터의 경우에는 TCP의 장점은 단점이 됨.
대안으로 전송계층에는 UDP(User Datagram Protocol)이 정의되어 있습니다.
연결성도 신뢰성도 제공하지 않지만 성능이 TCP보다 우수하기 때문에
전송 제어를 직접 처리하는 애플리케이션 수준에서 채용되는 경우가 많습니다.

애플리케이션 계층
각 응용 프로그램 나름의 프로토콜들이 정의되는 곳.
웹문서를 주고 받기 위한 HTTP(Hyper Text Trasfer Protocol)
파일 교환을 위한 FTP(File Transfer Protocol)
네트워크 관리를 위한 SNMP(Simple Network Management Protocol) 등...
애플리케이션 계층의 프로토콜들은 전송 계층의 TCP에 기반할 수도, UDP에 기반할 수도 있습니다.
HTTP와FTP는 상대적으로 큰 데이터여서 연결성과 신뢰성을 제공하는 TCP
SNMP는 단순한 정보만을 다루고 패킷을 유실해도 임무에 지장을 주지 않아 UDP
표준화된 프로토콜이 아니더라도 나름의 프로토콜을 정의해서 사용할 수 있습니다.

13.1.3 TCP/IP의 주소 체계:IP주소
패킷을 배달하려면 어디에서 보냈는지, 어디로 보낼지에 대한 주소가 필요합니다. IP주소.
IPv4는 부호없는 8비트 정수 4개로 구성. 0에서 255까지 값을 가지면 점(.)으로 연결.
주소고갈로 새로 IPv6가 나오고 128비트의 주소길이 16비트 8개를 콜론(:)으로 연결.

13.1.4 포트
네트워크 패킷이 드나들려면 '주소'뿐만아니라 출입문이 필요합니다. 포트(Port)
부호가 없는 16비트 정수로 0~65535 사이의 값을 이용합니다.
HTTP는 80번, FTP는 21번, Telnet은 23을 사용, HTTPS:443, SMTP:25, IRC:194, IIP:535
표준 프로토콜이 사용하고 있는 포트 번호는 합의된 값.
이런 포트번호를 '잘 알려진 포트번호' 1~1023사이의 수를 사용.
우리가 새로운 애플리케이션 프로토콜을 정의할 때는 범위를 피해서 정해야 됩니다.

포트와 보안
출입구를 얼마나 잘 단속하느냐. 꼭 필요한 포트만을 열어놓는 것이 최선.

13.1.5 TCP/IP의 동작과정
TCP/IP는 서버/클라이언트 방식으로 동작합니다. 양단 중 한쪽에서는 서비스를 제공.
웹서버와 웹브라우저, FTP서버와 FTP클라이언트, SMTP메일서버와 메일 클라이언트 등등.

통신을 위해서는 먼저 서버가 서비스를 시작해야 합니다.
클라이언트는 서버에 접속을 시도.
서버가 접속 시도를 수락하면 동등한 입장에서 데이터를 주고 받을 수 있습니다.
양쪽에서 보내고 받을 수 있고 용무가 끝나면 접속을 종료합니다.
종료 요청을 둘 중 아무대서나 할 수 있습니다.
서버                      클라이언트
서버시작
연결수락    <-----------  연결요청
데이터수신  <-----------  데이터전송
데이터수신  <-----------  데이터전송
데이터전송  ----------->  데이터수신
           <-----------  연결종료(서버가 할 수도 있음)
서버종료

13.2 socket과 TCPServer를 이용한 TCP/IP 프로그래밍
네트워킹 라이브러리들이 있는데 공통으로 socket모듈을 사용.
socket모듈은 TCP/IP, UCP/IP를 지원하는 버클리소켓 인터페이스를
여러가지 함수와 socket클래스를 통해 제공합니다.
socket클래스를 이용하면 거의 모든 인터넷 프로토콜을 구현할 수 있지만, 어렵습니다.

버클리 소켓?
소켓(Socket)은 컴퓨터를 네트워크에 연결할 수 있는 콘센트 역할.
버클리 소켓(BSD)는 유닉스의 네트워킹 API로 시작.
POSIX소켓, 윈도우소켓(Wisock)이 버클리 소켓 인터페이스를 거의 그대로 따름.
사실상의 네트워크 API의 표준.

TCPSever클래스는 서버 애플리케이션에서 사용하며 클라이언트의 연결 요청을 기다리는 역할.
TCPSever클래스가 실이라면 BaseRequestHandler클래스는 바늘 역할.
TCPSever클래스가 serve_forever()를 통해 클라이언트의 연결을 요청을 기다리다가 
클라이언트에게서 접속 요청이 오면 수락한 뒤 BaseRequestHandler객체의 
handle() 메소드를 호출합니다.
서버 애플리케이션은 이 handle() 메소드를 재정의해서 클라이언트와 데이터를 주고받는 일.

서버가 클라이언트 연결 요청을 수락해서 TCP 커넥션이 만들어지고 나면
서버 측의 socket 객체와 클라이언트 측의 socket 객체가 
socket.send()와 socket.recv()메소드를 통해 데이터를 주고 받을 수 있습니다.
서버 애플리케이션에서는 BaseRequestHandler의 request데이터 속성이 socket객체입니다.
서버와 클라이언트의 연결을 종료할 때는 socket의 close() 메소드를 호출하면 됩니다.
서버                                        클라이언트
TCPServer.serve_forever()     
BaseRequestHandler.handle()  <-----------   socket.connect()
socket.recv()                <-----------   socket.send()
(BaseRequestHandle객체의   
request데이터속성을 통해
소켓 객체 획득)
socket.recv()                <-----------   socket.send()
socket.send()                ----------->   socket.recv()
socket.close()               <-----------   socket.close() 서버에서 할 수 있다.

TCPSever와 BaseRequestHandler는 socketserver모듈에 정의
socket은 socket 모듈에 정의
클래스               메소드           설명
TCPServer           serve_forever()  클라이언트의 접속 요청을 수신 대기.
                                     요청이 있을 경우 수락하고, handle()를 호출
BaseRequestHandler  handle()         클라이언트 접속 요청을 처리합니다.
socket              connect()        서버에 접속 요청을 합니다.
                    send()           데이터를 상대방에게 전송합니다.
                    recv()           데이터를 수신합니다.

서버의 BaseRequestHandler를 상속하는 클래스
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address[0])           #클라이언트의 IP주소 출력
        buffer=self.request.recv(1024).strip()  #데이터 수신
        self.request.send(buffer)               #데이터 송신
상속 받은 MyTCPHandler는 handler()를 재정의.
handle()은 클라이언트의 연결 요청을 서버가 수락했을 때 호출됩니다.
호출됐다는 것은 통신할 준비가 됐다는 것.
handle()안에서는 통신을 종료하기 전까지 socket클래스의 인스턴스인
request데이터 속성을 이용하여 데이터를 주고 받으면 됩니다.

TCPServer의 객체를 만들 때 생성자 매개변수로 MyTCPHandler가 사용됨.
#TCPServer 생성자는 IP주소문자열과 숫자 형식의 포트 번호로 이루어진 튜플을 매개변수로.
#이 매개변수는 서버의 주소로 이용됨.
#뒤에는 상속된 클래스 이름.
server=socketserver.TCPServer(('192.168.100.11',5425),MyTCPHandler)
server.serve_forever() #클라이언트의 접속 요청을 받을 수 있습니다.

클라이언트에서 socket객체를 생성하고 서버에 연결을 요청하는 코드.
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("192.168.100.18",0)) #포트를 0으로 지정하면 OS에서 임의의 포트번호 할당.
#서버가 수신대기하고 있는 IP주소와 포트 번호를 향해 연결 요청.
sock.connect(('192.168.100.11',5425))

요청을 하면 수락하고, handle()을 호출. 이후에는 socket객체를 이용해 데이터통신가능.
클라이언트에서 socket 객체를 이용해서 데이터를 주고 받는 예제.
sbuff=bytes(message, encoding="utf-8") #텍스트는 인코딩 방식을 정하는게 좋음.
sock.send(sbuff) #데이터를 담은 bytes객체를 send()메소드에 매개변수로 넘김.
#수신할 데이터를 매개변수로 받아 상대방 노드로부터 데이터를 수신.
#사실 OS가 이미 상대방 노드로부터 OS의 버퍼에 받아놓은 데이터를 읽어오는것
rbuff=sock.recv(slen)
received=str(rbuff,encoding="utf-8")

클라이언트가 보내오는 메시지를 서버가 그대로 메아리쳐 돌려보내는 프로그램
EchoServer.py
EchoClient.py

cmd에서 IPCONFIG을 입력하면 자신의 IP를 알 수 있습니다.
네트워크에 연결되어 있지 않다면 둘다 127.0.0.1을 이용
127.0.0.1은 컴퓨터의 네트워크 입출력 기능을 시험하기 위해 가상으로 할당한 주소.
127.0.0.1을 향해 데이터를 기록하면 링크 계층을 거치지 않고 다시 자기 자신에게 패킷.
되돌아오는 입출력 기능 때문에 루프백(Loopback)주소라고 불립니다.

13.3 흐르는 패킷
TCP는 연결지향, 흐름 지향 프로토콜입니다.
TCP프로토콜도 전기처럼 양쪽이 연결되어 있어야하고 보내는 쪽에서 받는쪽으로 패킷을 흘림.
TCP프로토콜은 흐름 속에서 각 개별 패킷의 경계를 구분해야 합니다.
TCP통신 애플리케이션도 댐과 같은 역할을 하는 버퍼(Buffer)가 있습니다.
송신측 수신측 양쪽다 버퍼를 가지고 있고 거쳐야 합니다.

만약 두 애플리케이션이 TCP연결을 맺고있고, 송신 애플리케이션이 메모리에 들고 있는 데이터
'a','b','c'를 수신 애플리케이션에 보내려 한다고 합시다.
송신 메모리:'c','b','a'---->송신 버퍼
송신측 애플리케이션에서 socket.send(wBuffer)를 호출하면 데이터는 
메모리에서부터 송신버퍼로 이동하고, socket.send(wBuffer)는 송신 버퍼로 이동시킨 데이터의
크기인 3을 반환합니다.
송신버퍼:'c','b','a'-->수신 버퍼
운영체제는 송신버퍼에 있는 내용을 연결을 맺고 있는 수신측으로 보내기 시작합니다.
네트워크 대역폭이 넓고 품질도 좋다면 많은 데이터가 빠른 속도로 수신측으로 이동.
송신버퍼:'c','b'------->수신 버퍼:'a'-->수신 메모리
수신측의 애플리케이션에서는 데이터를 담기 위한 rBuffer를 정의하고,
rBuffer=socket.recv(16)을 호출.
16바이트를 읽어오려고 시도하지만 실제 수신 버퍼에는 'a'하나 밖에없어서
rBuffer에 'a'만 담아냅니다. 
수신 버퍼:'c','b'-->수신 메모리:'a'
그러는 동안 수신버퍼에 'b','c'가 도착합니다. 
수신측은 다시 호출하여 'b','c'를 rBuffer에 저장.
수신메모리:'c','b','a'

13.3.1 프로토콜 설계와 네트워크 애플리케이션 프로그래밍 예제.
TCP네트워크는 내 컴퓨터에서 사용하던 객체를 bytes형식으로 변환해서 보내고,
bytes로 들어온 데이터를 내컴퓨터에서 객체로 바꿔야하고,
수신한 데이터가 정상인지 검사해야하고, 안정성을 위해 연결상태도 점검해야하고.

파일업로드 프로토콜
FUP는 헤더와 바디의 두 부분으로 나뉩니다.
바디에는 실제로 전달하고자 하는 데이터를 담고,
헤더에는 본문 길이를 비롯해 메시지의 속성 몇 가지를 담을 겁니다.
바디의 길이는 담는 데이터에 따라 달라지지만 헤더의 길이는 16바이트로 항상 일정.
수신한 패킷을 분석할 때는 가장 먼저 16바이트를 먼저 확인해서 메시지의 속성을 확인하고,
그 다음에 바디의 길이만큼을 또 읽어 하나의 메시지 끝을 끊어내야 합니다.

파일 업로드 메시지
Header(16bytes)----MSGID(4bytes)
Body(nbytes)       MSGTYPE(4bytes)
                   BODYLEN(4bytes)
                   FRAGMENTED(1bytes)
                   LASTMSG(1bytes)
                   SEQ(2bytes)

고정 길이와 가변 길이의 비교
스트림에서 패킷의 경계를 구분해 내는 일은 TCP 네트워크 프로그래밍에서 필수적.
경계를 구분하는 방법은 메시지 포맷을 설계할 때 고려해야 하는데 고정, 가변.
고정 길이 형식에서는 모든 메시지가 같은 길이를 갖습니다.
구현하기는 편하지만, 대역폭이 낭비될 가능성이 높다는 단점.
가변 길이 형식에서는 두 가지 방식을 사용하는데,
메시지를 두 부분으로 나눠서 길이가 고정된 앞부분에 뒷부분의 길이를 기입하는 방식과
메시지를 구분하는 특정 값(''라든지)을 이용하는 방식.
후자의 경우에는 텍스트 방식의 통신에 주로 이용.
전자는 바이너리 통신에 이용. FUP도 해당.

MSGID(4byte):메시지 식별 번호
MSGTYPE(4byte):메시지의 종류 ----- 0x01:파일 전송요청
                                  0x02:파일 전송 요청에 대한 응답
                                  0x03:파일 전송 데이터
                                  0x04:파일 수신 결과
BODYLEN(4byte):메시지 본문의 길이(단위:byte)
FRAGMENTED(1byte):메시지의 분할 여부 ---- 0x0:미분할
                                         0x1:분할
LASTMSG(1byte):분할된 메시지의 마지막인지의 여부 ---- 0x0:마지막아님
                                                   0x1:마지막임
SEQ(2byte):메시지의 파편 번호

MSGTYPE이 4가지 종류여서 바디 종류도 4가지
파일 전송 요청. 
메시지는 클라이언트에서 사용합니다.
FILESIZE(8byte):전송할 파일 크기(단위:byte)
FILENAME(BODYLEN-FILESIZE(8)):전송할 파일의 이름

파일 전송 요청에 대한 응답
메시지는 서버에서 사용하며, 클라이언트에서 보낸 파일 요청 메시지의
메시지 식별 번호와 같이 결과를 클라이언트에게 전송.
MSGID(4byte):파일 전송 요청 메시지의 메시지 식별 번호
RESPONSE(1byte):파일 전송 승인 여부 --- 0x0:거절
                                       0x1:승인

0x02 메시지의 0x1을 담고 클라이언트에 돌아오면, 클라이언트는 파일 전송을 개시
클라이언트의 파일은 네트워크 전송에 알맞도록 잘게 쪼개져 
파일 전송 데이터 메시지에 담겨 서버로 날아갑니다.
DATA(헤더의 BODYLEN):파일 내용

클라이언트가 마지막 파일 데이터를 전송할 때는 파일 전송 데이터 메시지 헤더의
LASTMSG 필드에 0x01을 담아 보냅니다.
마지막 파일 전송 데이터 메시지를 수신한 서버는 파일이 제대로 수신됐는지를 확인해서
파일 수신 결과 메시지를 클라이언트에 보냅니다.
이때 메시지 바디에는 0x03의 MSGID와 파일 수신 결과가 함께.
MSGID(4byte):파일 전송 데이터의 식별 번호
RESULT(1byte):파일 전송 성공 여부 --- 0x0:실패
                                    0x1:성공

서버와 클라이언트가 메시지를 주고 받는 과정
서버                            클라이언트
    <---------------------------
        파일 전송 요청(0x01)
    --------------------------->
        파일 전송 응답(0x02)
    <---------------------------    
        파일 데이터(0x03)
    <---------------------------
        파일 데이터(0x03)
    <---------------------------
        파일 데이터(0x03)
    --------------------------->
        파일 전송 결과(0x04)

서버/클라이언트가 같이 사용할 모듈 만들기
파일 업로드 서버와 클라이언트는 모두 FUP 프로토콜을 사용.
FUP 프로토콜을 처리하는 코드를 서버와 클라이언트 양쪽에서 공유할 수 있음.
FUP 프로토콜을 클래스 라이브러리로 만드려고 합니다.
FUP프로토콜에서 사용할 각종 상수와 메시지의 구조를 나타내는 Message클래스를 정의.
FUP/message.py

메시지의 헤더를 나타냄
FUP/message_header.py

메시지 본문을 표현하는 클래스.
파일 전송 요청(BodyRequest), 파일 전송 요청에 대한 응답(BodyResponse),
파일 전송 데이터(BodyData), 파일 수신 결과(BodyResult) 4가지 클래스
FUP/message_body.py

FUP프로토콜에 맞춰 socket메소드를 쉽게 다룰 수 있는 유틸리티 클래스.
메시지를 스트림으로 보내고 받기 위한 메소드를 가짐.
FUP/message_util.py

파일을 클라이언트로부터 수신하여 저장하는 서버 프로그램
FUP/file_receiver.py

서버에 파일을 전송하는 클라이언트
FUP/file_sender.py

'''