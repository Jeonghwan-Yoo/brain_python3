'''
7.1 이 단원을 시작하기에 앞서 알아둬야 하는 용어
7.1.1 정의
정의(Definition)은 어떤 이름을 가진 코드가 구체적으로 어떻게 동작하는지를 '구체적으로 기술'
>>>def hello():
    print("hello world!")
>>>hello()
hello world!

7.1.2 호출과 반환
함수를 부르는 행위를 호출(Call), 함수를 부르는 코드를 호출자(Caller)
함수가 호출자에게 결과를 돌려주는 것을 반환(Return).

7.2 함수 정의하기
함수는 def 키워드를 이용해서 코드블록에 이름을 붙인 형태.
def 함수이름(매개변수 목록):
    코드블록
    return 결과
매개변수 목록은 괄호()로 감싸며, 각 매개변수는 콤마(,)로 구분.
매개변수 목록 뒤에는 콜론(:).
return 문 뒤에 넘겨 실행하면 결과가 반환. 반환할 것이 없으면 생략해도 된다.
>>>def my_abs(arg):
    if(arg<0):
        result=arg*-1
    else:
        result=arg
    return result
>>>my_abs(-5)
5

7.3 매개변수를 입력받는 여러 가지 방법
매개변수는 호출자와 함수 사이의 관계를 맺어주는 변수.
프로그래머는 함수의 사양을 정확하게 파악하고 사용해야 합니다. 안그러면 오류 메세지.
매개변수 이름은 보통의 변수처럼 문자와 숫자와 _로 만들어집니다.
숫자가 앞에 오면 사용할 수 없습니다.
의미를 분명하게 전달하는 이름이 좋습니다.
매개변수에는 어떤 자료형이든 사용할 수 있습니다.
>>>def print_string(text, count):
    for i in range(count):
        print(text)
>>>print_string('안녕하세요', 3)
안녕하세요
안녕하세요
안녕하세요

7.3.1 기본값 매개변수와 키워드 매개변수

>>>def print_string(text, count=1): #매개변수를 정의할 때 값을 할당하면 기본값 매개변수
    for i in range(count):
        print(text)
>>>print_string('안녕하세요') #두 번째 매개변수를 생략하면 기본값.
안녕하세요
>>>print_string('안녕하세요', 2)
안녕하세요
안녕하세요

호출자가 매개변수의 이름을 일일이 지정해 데이터를 입력하는 것도 가능. => 키워드 매개변수.
>>>def print_personnel(name, position='staff', nationality='Korea'):
    print('name={0}'.format(name))
    print('position={0}'.format(position))
    print('nationality={0}'.format(nationality))
>>>print_personnel(name='박상현')
name=박상현
position=staff
nationality=Korea
>>>print_personnel(name='박상현', nationality='ROK')
name=박상현
position=staff
nationality=ROK

7.3.2 가변 매개변수
str.format() 함수는 매개변수의 수가 유동적입니다.
가변 매개변수(Arbitrary Argument List)를 이용하면 된다.
def 함수이름(*매개변수): #매개변수 앞에 *를 붙이면 해당 매개변수는 가변으로 지정.
    코드블록
>>>def merge_string(*text_list):
    result=''
    for s in text_list:
        result=result+s
    return result
>>>merge_string('아버지가', '방에', '들어가신다.')
'아버지가방에들어가신다.'
*를 이용하여 정의된 가변 매개변수는 튜플입니다.
두개를 사용해 **를 가변 매개변수의 이름 앞에 붙여주면 딕셔너리 타입.
>>>def print_team(**players): #**를 붙이면 딕셔너리 가변 매개변수
    for k in players.keys():
        print('{0} = {1}'.format(k,players[k]))
>>>print_team(카시야스='GK', 호날두='FW', 알론소='MF', 페페='DF')
카시야스 = GK
페페 = DF
알론소 = MF
호날두 = FW

가변 매개변수의 '앞'에 정의되는 일반 매개변수는 키워드 매개변수를 이용할 수 없습니다.
>>>def print_args(argc, *argv):
    for i in range(argc):
        print(argv[i])
>>>print_args(3, "argv1", "argv2", "argv3")
argv1
argv2
argv3
>>>print_args(argc=3, "argv1", "argv2", "argv3") #에러
반대로, 일반 매개변수가 뒤에 있을 때는 키워드 매개변수로 호출해야 합니다.
>>>def print_args(*argv, argc):
    for i in range(argc):
        print(argv[i])
>>>print_args("argv1", "argv2", "argv3", argc=3)
argv1
argv2
argv3
>>>print_args("argv1", "argv2", "argv3", 3) #에러

7.4 호출자에게 반환하기
return문 세 가지 방법
1)return문에 결과 데이터를 담아 실행하기=>함수가 즉시 종료되고 호출자에게 결과 전달
2)return문에 아무 결과도 넣지 않고 실행=>함수가 즉시 종료.
3)return문 생략하기=>함수의 모든 코드가 실행되면 종료.
>>>def multiply(a, b):
    return a*b #함수의 실행을 종료시키고 자신에게 넘겨진 데이터를 호출자에게 전달.
>>>result=multiply(2,3)
>>>result
6
return문은 가급적 코드블록의 마지막에 하나만 실행하도록 하는 것이 좋습니다.
프로그래머가 실수로 버그를 만들기 쉬운 원인.
>>>def my_abs(arg):
    if arg<0:
        return arg*-1
    elif arg>0:
        return arg
>>>result=my_abs(0) #return을 실행하지 못하고 함수가 종료되면 호출자에게 None을 반환
>>>result
>>>result==None
True
>>>type(result)
<class 'NoneType'>
return문에 아무 결과도 넣지 않고 실행해도 None을 반환.
이것은 호출자에게 반환한다기보다는 함수를 '종료'시키는 용도.
>>>def ogamdo(num):
    for i in range(1, num+1):
        print('제 {0}의 아해'.format(i))
        if i==5:
            return #함수 종료
>>>ogamdo(8)
제 1의 아해
제 2의 아해
제 3의 아해
제 4의 아해
제 5의 아해
return문을 굳이 쓸 필요가 없다면 생략가능.
>>>def print_something(*args):
    for s in args:
        print(s)
>>>print_something(1,2,3,4,5)
1
2
3
4
5

7.5 함수 밖의 변수, 함수 안의 변수
>>>def scope_test():
    a=1 #함수를 호출하면 그 때 함수의 코드가 실행되면서 a가 메모리에 생성.
    print('a:{0}'.format(a))
>>>a=0 #함수 밖에서 a를 정의하고 0으로 초기화
>>>scope_test() #호출되면 함수 내부에서 a를 정의하고 1로 초기화
a:1
>>>print('a:{0}'.format(a)) #함수 밖에서는 여전히 0을 갖고 있다.
a:0

변수는 자신이 생성된 범위(코드블록) 안에서만 유효합니다.
함수 안에서 만든 변수는 함수 안에서만 살았다가 종료되면 끝:지역 변수(Local variable)
함수 외부에서 만든 변수는 프로그램이 살아있는 동안에는 살았다가 종료될 때 같이 소멸
이렇게 프로그램 전체를 유효 범위를 가지는 변수:전역 변수(Global variable)
전역 변수는 함수 또는 객체 사이에 데이터 교환이 필요할 때 사용.
파이썬은 함수 안에서 사용되는 모든 변수를 지역 변수로 간주.
전역 변수를 사용하려면 global 키워드를 이용해야 합니다.
>>>def scope_test():
    global a #유효 범위가 전역임을 알리고, 지역 변수의 생성을 막습니다.
    a=1 
    print('a:{0}'.format(a))
>>>a=0
>>>scope_test() #0으로 초기화된 a에 접근해 1로 변경
a:1
>>>print('a:{0}'.format(a))
a:1

7.6 자기 스스로를 호출하는 함수:재귀 함수(Recursive Function)
함수가 자기 자신을 부르는 것을 재귀 호출(Recursive Call)
함수가 호출자이자 피호출자가 되는 것.
재귀 함수는 재귀 관계식(Recurrence relation,점화식)으로 옮길 때 유용
>>>def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
>>>factorial(5)
120
재귀 함수는 호출 비용이 큽니다. 성능이 떨어지는 소프트웨어를 만들게 합니다.
반복문으로 대체하는 것이 낫습니다.
재귀 함수를 만들 때는 재귀 함수가 종료될 조건을 만들어줘야 합니다.
무한루프에다가 호출의 단계가 깊어질수록 메모리를 추가로 사용해서 매우 안좋을수 있다.
>>>def no_idea():
    print("나는 아무 생각이 없다.")
    print("왜냐하면")
    no_idea()
>>>no_idea()
나는 아무 생각이 없다.
왜냐하면
나는 아무 생각이 없다.
왜냐하면
나는 아무 생각이 없다.
왜냐하면
...
재귀 단계가 파이썬에서 지정해 놓은 최대 재귀 단계를 초과하면 에러를 일으키고 종료.

7.7 함수를 변수에 담아 사용하기
>>>def print_something(a):
    print(a)
>>>p=print_something #()없이 함수의 이름만을 변수에 저장.
>>>p(123) #변수의 이름 뒤에 ()를 붙여 함수처럼 호출.
123
>>>p('abc')
abc

순서열이나 딕셔너리에도 담을 수 있습니다.
>>>def plus(a,b):
    return a+b
>>>def minus(a,b):
    return a-b
>>>flist=[plus,minus] #plus()함수와 minus()함수를 리스트의 요소로 집어 넣습니다.
>>>flist[0](1,2) #plus(1,2)
3
>>>flist[1](1,2) #minus(1,2)
-1
어떻게 가능할까요?
파이썬이 함수를 일급 객체(First Class Object)로 다루기 때문.
일급 객체는 매개변수로 넘길 수 있고 함수가 반환할 수도 있으며 함수에 할당이 가능한 객체.
>>>def hello_korea():
    print('안녕하세요.')
>>>def hello_english():
    print('Hello.')
>>>def greet(hello):
    hello() #입력받은 매개변수 hello 뒤에 괄호를 붙혀 호출합니다.
    #함수를 정의하는 시점에서는 hello가 함수인지 매개변수의 수가 맞는지는 검사안함.
    #호출하는 시점에서 검사.
>>>greet(hello_korean) #greet()함수에 hello_korean()함수를 매개변수로 넘겨 호출
안녕하세요.
>>>greet(hello_english) #greet()함수에 hello_english()함수를 매개변수로 넘겨 호출
Hello.

>>>def hello_korean():
    print('안녕하세요.')
>>>def hello_english():
    print('Hello.')
>>>def get_greeting(where):
    if where=='K':
        return hello_korean #hello_korean()을 반환
    else:
        return hello_english #hello_english()을 반환.
>>>hello=get_greeting('K')
>>>>hello()
안녕하세요.

7.8 함수 안의 함수:중첩 함수(Nested Function)
중첩 함수는 자신이 소속된 함수의 매개변수에 접근할 수 있다는 특징.
>>>import math
>>>def stddev(*args):
    def mean(): #중첩함수
        return sum(args)/len(args)
    def variance(m): #중첩함수
        total=0
        for arg in args:
            total+=(arg-m)**2
        return total/(len(args)-1)
    v=variance(mean())
    return math.sqrt(v)
>>>stddev(2.3, 1.7, 1.4, 0.7, 1.9)
0.6
또 다른 특징은 자신이 소속되어 있는 함수 외부에서는 보이지 않는다는 것.
>>>mean() #에러메세지

7.9 pass:구현을 잠시 미뤄두셔도 좋습니다.
pass 키워드는 함수나 클래스의 구현을 미룰 때 사용합니다.
들여쓰기뿐이어서 애매한 빈코드를 코드블록으로 만들기 위해.
def empty_function():
    pass
클래스 등의 구현을 비워둘 때도 사용가능
class empty_class:
    pass

'''