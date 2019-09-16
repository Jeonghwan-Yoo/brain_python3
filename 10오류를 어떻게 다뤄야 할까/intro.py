'''
10.1 예외
예외(Exception)는 문법적으로는 문제가 없는 코드를 실행하는 중에 발생하는 오류.
정상적인 값을 입력하면 정상적인 결과지만 다른 값을 입력하면 오류가 발생하는 경우.
>>>def my_power(y):
    print("숫자를 입력하세요.")
    x=input()
    return int(x)**y
>>>my_power(3)
숫자를 입력하세요.
abc
#오류 발생.

10.2 try~except로 예외 처리하기
try 절 안에는 정상적인 경우에 실행할 코드블록을 배치 except 절에는 문제가 생겼을 때 뒤처리
try:
    #문제가 없을 경우 실행할 코드
except:
    #문제가 생겼을 때 실행할 코드

0으로 나누는 셈을 할 경우
>>>1/0
에러메시지~
ZeroDivisionError:division by zero
ZeroDivisionError가 어떤 수를 0으로 나누려 했을 때 파이썬이 일으키는 예외 형식.
try_except.py

10.2.1 복수 개의 except절 사용하기
늘어난 예외의 종류에 따른 예외 처리를 구현하려면 하나 이상의 except절을 사용
try:
    #문제가 없을 경우 실행할 코드
except 예외형식1:
    #문제가 생겼을 때 실행할 코드
except 예외형식2:
    #문제가 생겼을 때 실행할 코드
multiple_except.py

ZeroDivisionError와 IndexError는 예외 정보를 담고 있는 자료형일 뿐입니다.
예외형식의 인스턴스를 얻어내려면 as를 이용하면 된다.
try:
    #문제가 없을 경우 실행할 코드
except 예외형식1 as err:
    #문제가 생겼을 때 실행할 코드
except 예외형식2 as err:
    #문제가 생겼을 때 실행할 코드
err는 인스턴스의 식별자, 이름입니다.
multiple_except2.py
multiple_except3.py

10.2.2 try절을 무사히 실행하면 만날 수 있는 else
if에 else와는 다르다. try절에 있는 코드블록에서 예외가 일어나지 않으면 실행됩니다.
except절에 대한 else라고 생각할 수 있습니다.
try:
    #실행할 코드블록
except:
    #예외 처리 코드블록
else:
    #except절을 만나지 않았을 경우 실행하는 코드블록
try_except_else.py

10.2.3 어떤 일이 있어도 반드시 실행되는 finally
finally는 예외가 발생했든 아무 일이 없든 간에 '무조건' 실행됩니다.
그래서 파일이나 통신 채널과 같은 컴퓨터 자원을 정리할 때 사용.
try_except_finally.py

이렇게 사용할 수도 있습니다.
try:
    #코드블록
except:
    #코드블록
else:
    #코드블록
finally:
    #코드블록
try_except_else_finally.py

10.3 Exception 클래스
파이썬은 오류 상황에 대한 정보를 담는 예외 형식을 다양하게 제공합니다.
맨 위에는 BaseException. 모든 예외 형식은 BaseException클래스로부터 상속받습니다.
실질적인 시조로 간주되는 것은 그 밑에 Exception클래스.
Exception의 형제는 SystemExit, KeyboardInterrupt 같은 시스템 예외 클래스들.
코드 작성하면서 자주 사용하는 예외 형식은 거의 모두 Exception 클래스로부터 상속받음.
BaseException-SystemExit
              KeyboardInterrupt
              GeneratorExit
              Exception-ArithmeticError-ZeroDivisionError
                                       -...
                       -LookupError-IndexError
                                   -...
                       -...

상속에 의해 Exception클래스에 대한 예외 처리절이 다른 예외 처리절에 앞에서
위치하면 나머지 예외 처리절들이 모두 무시되는 일이 생깁니다.
ignored_exception.py

10.4 우리도 예외 좀 일으켜보자
피제수로 0을 입력받았다고 자동으로 ZeroDivisionError가 일어나는 것이 아니라,
/연산자가 입력받은 매개변수의 유효성을 판단하는 코드에 피제수가 0일경우 일어남.
예외를 일으키는 법은 예외 객체를 매개변수로 넘겨 raise문을 실행하면 됩니다.
text=input()
if text.isdigit()==False:
    raise Exception("입력받은 문자열이 숫자로 구성되어 있지 않습니다."):
>>>raise Exception("예외를 일으킵니다.") #다짜고자 raise문을 통해 예외를 일으킴.
에러메시지~
Exception: 예외를 일으킵니다. #예외 처리하는 곳이 없다 보니 인터프리터가 받아 출력.
>>>try:
    raise Exception("예외를 일으킵니다.")
except Exception as err:
    print("예외가 일어났습니다. : {0}".format(err))
예외가 일어났습니다. : 예외를 일으킵니다.

raise문을 통해 발생시킨 예외를 except로 받아 처리하지 않으면 자신을 받아주는
곳이 나올 때까지 상위코드로 나아갑니다.
함수에서 일어난 예외를 함수 안에서 처리하지 않으면 함수의 호출자에게로 던져집니다.
호출자도 처리를 안하고 그 호출자의 호출자도 처리를 안하면 파이썬 인터프리터가 받아냅니다.
raise_in_function.py

except절이 받아 한 번 처리한 예외를 그대로 상위 호출자에게 던지고 싶을 때에는
매개변수 없이 except 절에서 raise문을 실행하면 됩니다.
try:
    #예외 발생
except:
    raise
raise_again.py

10.5 내가만든 예외 형식
그냥 Exception 클래스를 상속하는 클래스를 정의하면 됩니다.
class MyException(Exception):
    pass
상속만으로도 예외 형식이 하나 완성되지만 기호에 따라 데이터 속성이나 메소드를 추가.
class MyException(Exception):
    def __init__(self):
        super().__init__("MyException이 발생했습니다.")
예외 형식의 인스턴스는 예외 상황을 점검하는 코드에서 raise문에 매개변수로 넘기면 됩니다.
if everything_is_fine==False:
    raise MyException()
InvalidIntException.py

'''