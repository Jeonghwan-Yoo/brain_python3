'''
6.1 흐름 제어를 시작하기 전에
6.1.1 bool 자료형
bool은 True와 False 두 가지 값을 나타내는 자료형.
>>>a=3>2
>>>a
True
>>>type(a)
<class 'bool'>

6.1.2 논리 연산자
not, and, or은 참과 거짓을 다루는 논리 연산자.
not 연산자는 피연산자를 부정하는 결과.
>>>not True
False
>>>not 0 #0인 경우 거짓
True 
>>>not -1
False
>>>not None
True
>>>not 'ABC' #비어있지 않은 문자열을 부정
False
>>>not '' #빈 문자열을 부정
True
>>>not () #빈 튜플을 부정
True
>>>not [] #빈 리스트를 부정
True
>>>not {} #빈 딕셔너리를 부정
True
and 연산자는 두 피연산자 간의 논리곱을 수행.
>>>True and True
True
>>>True and False
False
or 연산자는 두 피연산자 간의 논리합을 수행.
>>>False or False
False
>>>False or True
True

6.1.3 흐름 제어문과 조건문
흐름 제어문은 흐름을 분기하거나 반복하기 전에 조건문의 결과가 참인지를 평가.
다양한 객체가 사용됩니다.
다음과 같을 때 거짓으로 평가
1)False
2)None
3)숫자 0, 0.0
4)비어있는 순서열
5)비어있는 딕셔너리
객체가 거짓으로 평가되는지를 알고 싶을 때는 bool()함수
>>>bool(False)
False
>>>bool(0.0)
False
>>>bool({})
False

6.1.4 코드블록과 들여쓰기
파이썬은 들여쓰기로 구역을 나눕니다.
들여쓰기는 space나 Tab 둘다 사용할 수 있지만 섞어서 사용할 수는 없습니다.
PEP-8에서 스페이스 4칸을 사용할 것을 권고.
들여쓰기를 시작하기 전 윗줄의 끝에 콜론(:)이 위치해 있어야 합니다.
if a==3:
    print(' ')
else:
    print(" ")

6.1.5 비교 연산자
==:양쪽에 위치한 피연산자가 서로 같으면 True, 아니면 False
>>>a=30
>>>a==30
True
>>>a==40
False
!=:양쪽에 위치한 피연산자가 서로 다르면 True, 아니면 False
>>>a='안녕'
>>>a!='안녕'
False
>>>a!='Hello'
True
>:왼쪽에 위치한 피연산자가 오른쪽 피연산자보다 크면 True, 아니면 False
>>>a=30
>>>a>20
True
>=:왼쪽에 위치한 피연산자가 오른쪽 피연산보다 크거나 같으면 True, 아니면 False
>>>a=30
>>>a>=30
True
<:왼쪽에 위치한 피연산자가 오른쪽 피연산자보다 작으면 True 아니면 False
>>>a=30
>>>a<40
True
<=:왼쪽에 위치한 피연산자가 오른쪽 피연산자보다 작거나 같으면 True, 아니면 False
>>>a=30
>>>a<=30
True

6.2 분기문
소프트웨어는 컴퓨터가 할 일의 목록.
컴퓨터는 소프트웨어에 기록된 목록을 보고 그대로 수행.
흐름을 가르는 문장.

6.2.1 if문
if 조건: #참일 때
    명령1
else: #거짓일 때
    명령2
if문의 조건은 참 아니면 거짓으로 평가될 수 있어야 합니다.
else는 필수사항은 아닙니다.
ifelse.py
if.py

여러 가지 조건을 생각할 때, else if를 줄인 elif를 사용.
if 조건1:
    명령1
elif 조건2:
    명령2
elif 조건3:
    명령3
else:
    명령4
코드블록은 또 다른 흐름 제어문을 가질 수 있습니다. 들여쓰기를 한 단계 더 깊이.
여러 조건을 평가할 때 중첩if 대신 and 나 or 연산자를 이용하는 것도 좋은 방법.
ifelif.py
ifif.py
ifand.py

6.3 반복문
컴퓨터의 강점 중 하나는 계산을 반복할 수 있다는 것. 흐름을 되풀이하는 것.

6.3.1 while문
while 조건:
    코드블록
조건이 참인 동안.
while.py

조건이 항상 True인 경우를 만들면 프로그램의 흐름은 영원히 반복하게 됩니다.
무한루프(Infinite loop)는 의도하지 않았으면 큰 문제지만,
365일 계속 수행해야 하는 서버나 게임은 필요로 하는 예입니다.
while True:
    코드블록
while_infinite.py

6.3.2 for문
조건을 평가하는 것이 아니라 순서열을 순회하다가 순서열의 끝에 도달했는지를 봅니다.
for 반복변수 in 순서열:
    코드블록
for.py

순서열은 리스트, 튜플, 문자열 등 어떤 것을 사용할 수 있습니다.
for문은 순서열의 각 원소를 처음부터 차례로 순회하면서 반복변수에 담아냅니다.
반복 횟수를 한 줄의 코드로 파악이 가능한 장점. 횟수가 정해져있을 경우 좋다.
for_list.py
for_string.py

for문에 가장 많이 사용되는 순서열은 레인지(Range)입니다.
레인지는 연속하는 두 수의 차이가 일정한 수열.
range()함수에 시작값, 멈춤값, 그리고 연속하는 두 수의 차를 매개변수로.
생성된 레인지의 마지막 요소가 멈춤값보다 한 단계 작다는 사실에 주의.
>>>for i in range(0,5,1): #시작값(<=), 멈춤값(<), 연속하는 두 수의 차
    print(i)
0
1
2
3
4
range() 연속하는 두 수의 차는 생략가능. 연속하는 두 수의 차를 1로 간주.
>>>for i in range(0,5): #시작값, 멈춤값.
    print(i)
0
1
2
3
4
range() 멈춤값만 입력해서 호출할 수도 있습니다. 시작값은 0, 차는 1로 간주.
>>>for i in range(5): #멈춤값
    print(i)
0
1
2
3
4
forfor.py

튜플 언패킹이 유용하게 사용.
>>>dic={'애플': 'www.apple.com', '파이썬': 'www.python.org',
    '마이크로소프트': 'www.microsoft.com'}
>>>for k,v in dic.items(): #k와 v에는 각 요소의 키와 값이 할당됩니다.
    print("{0} : {1}".format(k,v))
애플 : www.apple.com
파이썬 : www.python.org
마이크로소프트 : www.microsoft.com

6.3.3 continue와 break로 반복문 제어하기
continue는 반복문이 실행하는 코드블록의 나머지 부분을 실행하지 않고 다음 반복으로 건너감.
continue.py

break는 루프를 중단시키는 기능.
break.py

'''
