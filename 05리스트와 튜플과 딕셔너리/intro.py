'''
5.1 리스트
List는 데이터의 목록을 다루는 자료형.
Slot이 있고 리스트의 각 슬롯에 꽂혀있는 개별 데이터를 일컬어 요소(Element).
리스트를 알아두면 많은 데이터를 다룰 때 한결 정돈된 코드.
리스트를 만들 때는 대괄호[]를 사용
>>>a=['김개똥', '박짱구', '이멍충'] #각 데이터는 콤마로 구분.
>>>a
['김개똥', '박짱구', '이멍충']
>>>a[0] #문자열처럼 참조 연산이 가능.
'김개똥'
>>>a[2]
'이멍충'
순서열이므로 슬라이싱가능
>>>a=[1,2,3,4,5,6,7,8,9,10]
>>>a[0:5]
[1,2,3,4,5]
+연산자를 통한 리스트간의 결합
>>>a=[1,2,3,4]
>>>b=[5,6,7]
>>>a+b
[1,2,3,4,5,6,7]
리스트 내의 특정 위치에 있는 데이터를 변경하려면 참조 연산을 이용
>>>a=[1,2,3,4,5]
>>>a[2]=30 #첨자를 입력하면 특정 요소에 접근해 내용을 변경할 수 있습니다.
>>>a
[1,2,30,4,5]
리스트의 길이를 잴 때도 len()
>>>a=[1,2,3]
>>>len(a)
3

5.1.1 리스트 메소드
append():리스트의 끝에 새 요소를 추가합니다.
>>>a=[1,2,3]
>>>a.append(4)
>>>a
[1,2,3,4]
extend():기존 리스트에 다른 리스트를 이어 붙입니다. +와 같은 기능.
>>>a=[1,2,3]
>>>a.extend([4,5,6])
>>>a
[1,2,3,4,5,6]
insert():첨자로 명시한 리스트 내의 위치에 새 요소를 삽입합니다. insert(첨자, 데이터)
>>>a=[2,4,5]
>>>a.insert(0,1) #0 위치에 데이터 1을 삽입합니다.
>>>a
[1,2,4,5]
remove():매개변수로 입력한 데이터를 리스트에서 찾아 발견한 첫 번째 요소를 제거.
>>>a=['BMW', 'BENZ', 'VOLKSWAGEN', 'AUDI']
>>>a.remove('BMW')
>>>a
['BENZ', 'VOLKSWAGEN', 'AUDI']
pop():리스트의 마지막 요소를 뽑아내어 리스트에서 제거합니다.
>>>a=[1,2,3,4,5]
>>>a.pop()
5
>>>a
[1,2,3,4]
마지막이 아닌 특정 요소를 제거하고 싶을 때는 요소의 인덱스를 입력.
>>>a=[1,2,3,4,5]
>>>a.pop(2) #2 위치 요소 제거(3번째)
3
>>>a
[1,2,4,5]
index():리스트 내에서 매개변수로 입력한 데이터와 일치하는 첫 번째 요소의 첨자를 알려줌.
찾고자하는 데이터와 일치하는 요소가 없으면 오류
>>>a=['abc', 'def', 'ghi']
>>>a.index('def')
1
count():매개변수로 입력한 데이터와 일치하는 요소가 몇 개 있는지 셉니다.
>>>a=[1,100,2,100,3,100]
>>>a.count(100)
3
>>>a.count(200)
0
sort():리스트 내의 요소를 정렬. reverse=True는 내림차순, 입력 없으면 오름차순.
reverse=True와 같이 이름을 명시하여 사용하는 매개변수를 키워드 매개변수.
>>>a=[3,4,5,1,2]
>>>a.sort()
>>>a
[1,2,3,4,5]
>>>a.sort(reverse=True)
>>>a
[5,4,3,2,1]
reverse():리스트 내 요소의 순서를 반대로 뒤집습니다.
>>>a=[3,4,5,1,2]
>>>a.reverse()
>>>a
[2,1,5,4,3]

5.2 튜플
튜플은 'N개의 요소로 된 집합'.
리스트는 변경이 가능하고 튜플은 변경이 불가능.
특정 요소에 접근해 데이터를 변경하는 일이 리스트에서는 가능하지만 튜플은 불가능
튜플은 변경이 불가능하므로 sort()가 없다.
리스트는 목록 형식의 데이터를 다루는데 적합하고, 튜플은 위경도 좌표나 RGB 색상처럼
작은 규모의 자료 구조를 구성하기에 좋습니다.

쓰는이유
불가능한 자료형(Immutable Type)은 성능을 향상시키는데 도움을 줍니다.
데이터를 할당할 공간의 내용이나 크기가 달라지지 않기 때문에 생성 과정이 간단하고,
데이터가 오염되지 않을 것이라는 보장이 있기 떄문에 복사본 대신 원본을 사용해도 되서.
프로그래머가 자기 코드를 신뢰할 수 있다는 것.
코드를 설계할 때부터 변경이 가능한 데이터와 그렇지 않은 데이터를 정리해서 코드에 반영.
문자열도 튜플처럼 변경이 불가능한 자료형.
문자열의 내용을 바꾸고 싶다면 바뀐 내용을 가질 문자열 하나를 새로 만들어야 합니다.

튜플만드는법은 괄호()를 이용하는 것, 괄호를 생략해도 된다.
>>>a=(1,2,3)
>>>a
(1,2,3)
>>>type(a)
<class 'tuple'>
>>>a=1,2,3,4
>>>a
(1,2,3,4)
>>>type(a)
<class 'tuple'>
튜플도 리스트와 문자열처럼 순서열 자료형입니다. 참조 연산, 슬라이싱, 결합이 가능.
>>>a=(1,2,3,4,5,6)
>>>a[:3]
(1,2,3)
+연산자를 통한 결합
>>>a=(1,2,3)
>>>b=(4,5,6)
>>>c=a+b
>>>c
(1,2,3,4,5,6)
참조 연산은 가능하지만 요소 변경은 허용되지 않습니다.
>>>a=(1,2,3)
>>>a[0]
1
튜플의 길이를 잴 때는 len() 함수
>>>a=(1,2,3)
>>>len(a)
3

5.2.1 패킹과 언패킹
여러 가지 데이터를 튜플로 묶는 것을 튜플 패킹(Tuple Packing)
>>>a=1,2,3
>>>a
(1,2,3)
튜플의 각 요소를 여러 개의 변수에 할당하는 것을 튜플 언패킹(Tuple Unpacking)
>>>one, two, three=a (위에 이어서)
>>>one
1
>>>three
3
언패킹을 할 때는 튜플 요소의 수와 각 요소를 담아낼 변수의 수가 일치해야 합니다.
언패킹을 활용하면 여러 개의 변수에 한번에 할당을 수행할 수 있습니다.
>>>city,latitude,longtitude='Seoul', 37.541, 126.986
>>>city
'Seoul'

5.2.2 튜플 메소드
제공하는 메소드가 2개뿐
index():매개변수로 입력한 데이터와 일치하는 튜플 내 요소의 첨자를 알려줍니다.
>>>a=('abc', 'def', 'ghi')
>>>a.index('def')
1
count():매개변수로 입력한 데이터와 일치하는 요소가 몇 개 있는지 셉니다.
>>>a=(1, 100, 2, 100, 3, 100)
>>>a.count(100)
3
>>>a.count(200)
0

5.3 딕셔너리
리스트처럼 첨자를 이용해서 요소에 접근하고, 그 요소를 변경할 수도 있습니다.
딕셔너리는 문자열과 숫자를 비롯해서 변경이 불가능한 형식이면 어떤 자료형이든 사용가능.
딕셔너리의 첨자는 키(Key)라고 하고, 키가 가리키는 슬롯에 저장되는 데이터를 값(Value).
키-값의 쌍으로 구성됩니다. 단어-뜻처럼
탐색 속도가 빠르고, 사용하기도 편합니다.
딕셔너리를 만들 때는 중괄호{}를 이용. 특정 슬롯에 참조하려면 대괄호[]를 이용
>>>dic={}
>>>dic['파이썬']='www.python.org'
>>>dic['마이크로소프트']='www.microsoft.com'
>>>dic['애플']='www.apple.com'
>>>dic['파이썬']
'www.python.org'
>>>type(dic)
<class 'dict'>
>>>dic
{'애플': 'www.apple.com', '파이썬': 'www.python.org', 
'마이크로소프트': 'www.microsoft.com'}
배열이 데이터를 저장할 요소의 위치로 인덱스를 사용하지만, 딕셔너리는 키 데이터를 그대로사용.
탐색 속도가 거의 소요되지 않습니다. 
키를 이용해서 단번에 데이터가 저장된 위치의 주소를 계산하기 때문에.
이런 작업을 해싱(Hashing). 
변경이 불가능한 자료형에 대해서만 해싱할 수 있어서 변경이 가능한 자료형은 키로 못함.
키-값쌍의 순서가 입력한 순서와는 다른데, 저장할 때 키를 해싱해서 주소를 계산해내기 때문.
딕셔너리를 사용할 때는 데이터의 입력 순서보다는 키를 활용한 빠른 탐색을 추구.

메소드
keys()는 키의 목록을, values()는 값의 목록을 추려냅니다.
>>>dic.keys()
dict_keys(['애플', '파이썬', '마이크로소프트'])
>>>dic.values()
dict_values(['www.appe.com', 'www.python.org', 'www.microsoft.com'])
items()는 키와 값의 쌍으로 이루어진 전체 목록을 반환
>>>dic.items()
dict_items([('파이썬', 'www.python.org'), ('애플', 'www.apple.com'),
('마이크로소프트', 'www.microsoft.com')])
in 연산자를 이용하면 특정 키가 키 목록 안에 존재하는지 확인할 수 있고, 값도 할 수 있다.
>>>'애플' in dic.keys()
True
>>>'www.microsoft.com' in dic.values()
True
키-값 쌍을 제거하려면 pop(). 매개변수로는 삭제할 키-값 쌍의 키를 입력.
>>>dic.pop('애플')
'www.apple.com'
>>>dic
{'파이썬': 'www.python.org', '마이크로소프트': 'www.microsoft.com'}
딕셔너리의 데이터를 전부 정리하고자 할 떄는 clear()
>>>dic.clear()
>>>dic
{}


'''