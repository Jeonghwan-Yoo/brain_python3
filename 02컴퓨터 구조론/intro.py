'''
코딩을 배우기 전에 읽는 컴퓨터 구조론

2.1 폰 노이만 구조
데이터를 외부로부터 받아들이고 내보내는 입력/출력 장치(Input/Output)를 갖고 있고,
데이터와 명령어를 보관하는 기억 장치(Memory), 데이터의 가공을 담당하는 중앙 처리 장치(CPU)로 구성.
     기억 장치
   ||         ||
제어장치<->산술 논리 장치  <-> 입력 장치
    중앙 처리 장치        <-> 출력 장치

이미 에커트와 모클리가 세계 최초의 컴퓨터 에니악(ENIAC)의 설계를 끝내고 개발을 진행
프로그래밍에 필요한 명령어를 기억하고 있지 않기 때문에 계산식을 변경하면 다시 세팅해야하는 작업
에커트와 모클리는 별도의 컴퓨터 개발을 제안했고, 에드박(EDVAC)이 개발.
명령어를 기억 장치에 내장하고 있기 때문에 훨씬 자유로웠다. 프로그램 내장식 컴퓨터.
프로그램 내장식 컴퓨터(Stored-program computer)는 폰 노이만의 논문에서 본격적으로 소개되어
폰 노이만 구조(von Neumann Architecture)로 알려지게 됩니다.

2.1.1 중앙 처리 장치
CPU는 컴퓨터에서 가장 중요한 장치. 컴퓨터가 수행하는 계산은 모두 이 CPU를 통해 이루어짐.
산술 논리 장치(ALU)는 산술 연산과 참과 거짓을 다루는 논리 연산을 수행하는 회로를 가진다.
제어장치(CU)는 산술 논리 장치를 위대한 계산기로 만든다.
1)먼저 제어 장치가 기억 장치로부터 명령어를 가져옵니다(Fetch)
2)제어 장치는 가져온 명령어를 해독(Decode)합니다.
3)제어 장치는 해독한 명령어에 따라 산술 논리 장치에 데이터를 옮기고 어떤 연산을 수행할지 지시.
4)산술 논리 장치는 제어 장치가 지시한 대로 계산을 수행(Execute)합니다.
5)그리고 수행한 결과를 기억 장치에 다시 저장(Store)합니다.
명령어 인출->명령어 해독->산술 논리 장치 제어->계산 실행->결과 저장

기억 장치로부터 명령어를 불러오고 해독하며, 실행하는 주기를 '명령 주기(Instruction Cycle)'
CPU는 Clock을 가지고 있어서, 움직일 때마다 신호를 보내 명령 주기를 반복시킵니다.
명령 주기를 빠르게 반복할수록 컴퓨터는 주어진 시간 내에 할 수 있는 일이 많아집니다.
주기로 Hz 단위를 사용합니다.

2.1.2 기억 장치
Memory는 데이터와 함께 명령어를 저장하는 역할을 합니다.
용량이 클수록 많은 데이터, 빠르게 동작할수록 더 빨리 데이터를 교환.
메모리에 데이터를 기록하려면 CPU는 '쓰기 요청'을 보내고 가져오려면 '읽기 요청'을 보냅니다.
성능은 이 요청에 응답하기까지의 시간과 이러한 읽기/쓰기 요청을 연속적으로 처리하는 주기에 따라.

CPU와 가장 가까이에 있는 캐시(Cache)메모리.
캐시 메모리 아래에는 대게 램(RAM)으로 구성되는 주기억 장치.
CPU로부터 가장 멀리 떨어져 있는 보조기억 장치.
가장 성능이 좋은 것은 캐시이지만 가격도 가장 비쌉니다. 용량도 아주 작습니다.

2.1.3 입력/출력 장치
컴퓨터가 바깥세계와 소통하는 방법.
'입출력 버스(I/O BUS)'를 통해 중앙 처리 장치, 기억 장치와 정보를 주고 받습니다.
버스는 컴퓨터의 정보 전송 회로.
중앙 처리 장치   기억 장치   입출력 장치   입출력 장치
     |              |           |            |
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
입출력 버스는 각 장치 간의 연결 회로 구성을 단순화하는 장점이 있지만 편도 1차선 도로의 문제.
가장 느린 화물차의 속도 때문에 더 빠르게 달릴 수 있는 차량들의 속도가 제한되는 것.
이를 해결하기 위해 버스를 두 가지로 나눕니다.
CPU와 기억 장치는 시스템 버스(System Bus), 그다음 다양한 입출력 장치들은 입출력 버스로 묶어
CPU의 입출력 모듈에 연결했습니다.
입출력 버스의 표준은 USB, PCI, ISA...

2.2 운영체제와 애플리케이션
소프트웨어들도 애플리케이션에 해당. 컴퓨터를 사용한다는 것은 보통 애플리케이션을 사용.
운영체제(OS)는 애플리케이션이 다양한 하드웨어 위에서 동작할 수 있도록 하는 시스템 소프트웨어.
운영체제는 애플리케이션에게 API를 제공하여 운영체제가 제어하고 있는 하드웨어를 이용할 수 있게.

2.3 소프트웨어는 무엇으로 만드는가
전기 배선은 애니악이 계산할 때 사용하는 회로로 지금의 프로그램
뜨거운 진공관으로 운영 중단, 프로그램 변경하려면 수많은 배선 교체.
이후 폰 노이만의 에드박은 현대 컴퓨터의 조상.
이후에는 하드웨어를 중심으로 이루어졌고, 여전히 0과 1의 비트로 구성되는 기계어의 조합.
컴퓨터는 어떤 일이든 세세하게 지시해 주지 않으면 아무것도 하지 못합니다.
이런 점을 역으로 이용해 개발된 프로그래밍 언어가 바로 어셈블리(Assembly)
어셈블리어는 복잡한 기계어 명령을 사람이 이해할 수 있는 기호나 단어로 바꿔 만든 것.
어셈블리어는 컴파일(Compile)이라는 번역 과정을 거쳐 컴퓨터가 이해하는 기계어 코드로 변환.
코드를 작성한 후에는 컴파일러(Compiler)라는 소프트웨어를 이용해 실행 파일(프로그램)을 만듦
프로그램을 작성하기 위해 만들어진 인공 언어 체계를 프로그래밍 언어.

컴파일러는 소스코드를 컴파일하여 실행파일로 만듭니다.
프로그램을 실행하기 위해서는 실행파일만 있으면 됩니다.
반면에 인터프리터(Interpreter)는 소스코드를 미리 실행파일로 만드는 작업이 필요없다.
소스코드를 실시간으로 기계어로 해석해서 실행해주기 때문.
컴파일 방식은 오류를 발견하면 수정하고 확인하기 위해 무조건 컴파일 과정
인터프리트 방식은 오류를 발견해서 수정을 하면 바로 실행이 가능해 개발 속도가 빠른 편.
파이썬도 인터프리트 방식의 프로그래밍 언어.

컴파일:CPU가 실행할 수 있는 기계코드로 컴파일되므로 실행속도 빠름.
애플리케이션을 옮기는 경우, 대체로 코드를 그대로 사용할 수 없음. 이식성이 낮음.
인터프리트 방식:실행할 때마다 인터프리터가 소스코드를 기계코드로 번역해 실행속도 느림
인터프리터만 지원한다면 코드 변경할 필요 없이 어떤 환경에서나 실행 가능. 이식성이 높음.

2.4 파이썬 프로그래밍 언어
1989년 귀도 반 로섬이 개발을 시작한 언어. 코미디 쇼에서 따온 이름.
귀도는 만인을 위한 프로그래밍(CP4E) 언어로써 설계.
문법을 읽고 쓰기 쉽게 만들고, 인터프리트 방식을 채택해 코드의 수정-실행을 줄여 학습에 유리하게.
메모리가 허용하는 한 무한대의 정수를 다룰 수 있는 등 수치 처리에 강점.
다른 언어에 비해 생산성이 높고, 다른 언어로 작성된 코드와 결합하는 능력이 탁월.
라이브러리가 많이 있습니다.
라이브러리는 재사용할 수 있는 코드의 모음.
대다수 프로그래머가 자신이 만든 라이브러리를 무료로 공개하여 사용할 수 있게 함.
범용 프로그래밍 언어여서 시스템/임베디드 분야가 아니면 어떤 분야에서도 사용 가능.
오픈소스 프로젝트.
파이썬3은 하위 호환성을 제공하지 않습니다.

'''