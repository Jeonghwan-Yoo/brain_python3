'''
9.1 객체 지향 프로그래밍
9.1.1 객체와 클래스
객체(Object) = 속성(Attribute) + 기능(Method)
속성은 사물의 특징. 기능은 어떤 것의 특징적인 동작.
객체=변수+함수

저 변수와 함수를 객체로 '응집'시키려면 class 키워드가 필요합니다.
class Car: #Car 클래스의 정의 시작.
    def __init__(self):
        self.color=0xFF0000 #변수정의
    def forward(self): #함수 정의
        pass
    ...
클래스는 자료형이고 객체는 변수.
my_car=Car() #자료형:Car클래스, 객체:my_car
객체 대신에 인스턴스(Instance)라는 용어를 사용하기도 합니다.
클래스가 설계도라면, 객체는 그 설계를 바탕으로 실체화한 것이어서.
객체뿐 아니라 변수도 인스턴스라고 부릅니다.

9.1.2 객체 지향 프로그래밍을 해야 하는 이유
결합도는 한 시스템을 구성하는 요소간의 의존성을 나타내는 말.
A를 수정했을 때 B에 부작용이 생긴다면 강한 결합도.
고객과 품질 부서로부터 버그 리포트가 올라오면 프로그래머는 패치를 만들어야 합니다.
결합도가 높으면 코드를 고칠 때마다 부작용(Side effect)가 발생할 수 있습니다.
같은 목적과 기능을 위해 객체로 묶인 코드 요소들은 객체 내부에서만 강한 응집력을
발휘하고 객체 외부에 주는 영향은 줄이게 됩니다.
객체 위주로 이루어질 수 있도록 지향하면 결합도를 낮추는 결과.

9.2 클래스의 정의
class 클래스이름:
    코드블록
클래스의 코드블록은 변수와 메소드(Method)로 이루어집니다.
기능(Method):사물의 동작. 행위, 방법.
메소드(Method):기능에 대응하는 파이썬 용어. 함수와 거의 동일하지만, 메소드는 클래스의 멤버.
함수(Function):일련의 코드를 하나의 이름 아래 묶은 코드 요소.
클래스 안에 정의되어 있는 변수와 메소드는 클래스의 '멤버(Member)'
일반 변수와 클래스의 멤버 변수를 구분하기 위해 '데이터 속성(Data Attribute)' 용어.
__init__()는 객체가 생성될 때 호출되는 메소드로써, 객체의 초기화를 담당.
객체의 데이터 속성도 이곳에서 정의하면 됩니다.
메소드의 첫 번째 매개변수(관습적으로 self가 사용)는 객체 자신을 나타냅니다.
명시적으로 이 매개변수를 정의하지만 호출할 때는 파이썬에서 자동으로 해당 매개변수를 채움.
정의할 때만 신경 써주면 호출할 때는 일반 함수와 동일한 방식으로 사용할 수 있다.

객체를 만들 때는 클래스 이름 뒤에 괄호()를 붙인 꼴인 생성자를 이용합니다.
my_car=Car() #Car 클래스의 인스턴스를 생성하여 반환.
생성자는 모든 자료형에 존재합니다.
>>>a=int(3)
>>>a
3
>>>a=str('hello')
>>>a
'hello'
데이터 속성이나 메소드에 접근하려면 점(.)을 이용해야 합니다. 읽을 때는 '~의'로 해석
Car.py

9.2.1 __init__() 메소드를 이용한 초기화
클래스의 생성자가 호출되면 내부적으로 또 다른 두 개의 메소드가 호출됩니다.
__new__()와 __init__()입니다.
이들은 마법(Magic) 메소드 또는 특별(Special) 메소드라고 불립니다.
이 메소드들은 정의를 해도 직접 호출할 일은 별로 없습니다.
대신 클래스에 어떤 일이 생길 때 파이썬이 마법처럼 호출해줍니다.
생성자가 호출되면 가장 먼저 __new__()가 호출됩니다.
이 메소드의 임무는 클래스의 인스턴스를 만드는 것, 정의는 권장하지 않습니다.
__new__()메소드는 클래스 메소드여서 인스턴스 속성에 접근하기 어렵습니다.
__init__()메소드는 인스턴스 메소드여서 인스턴스 변수를 다루기에 적합합니다.
__new__()는 생성, __init__()은 초기화의 임무를 나눠가집니다.

__init__()메소드가 아닌 클래스에 직접 데이터 속성을 정의한다면??
class ClassVar:
    text_list=[]
데이터 속성은 클래스의 정의 시점에 함께 같은 메모리에 할당됩니다.
즉, 객체가 생성되기 전부터 메모리에 적재되어 있습니다.
이렇게 클래스와 같은 시간/장소에 정의되는 데이터 속성을 '클래스 속성'이라고 합니다.
인스턴스와 같은 시간/장소에 정의되는 데이터 속성은 '인스턴스 속성'
클래스 속성으로 정의된 것이 모든 인스턴스와 공유됩니다.
ClassVar.py

이런 문제를 피하려면 데이터 속성을 정의할 때는 __init__()을 이용.
class InstanceVar:
    def __init__(self):
        self.text_list=[]
InstanceVar.py

__init__()은 생성자로부터 전달된 매개변수를 받아 객체의 상태를 초기화.
class ContactInfo:
    def __init__(self, name, email): #생성자로부터 매개변수를 전달받아 초기화.
        self.name=name
        self.email=email
sanghyun=ContactInfo('박상현', 'seanlab@gamil.com')
이렇게 생성자와 __init__()을 이용하면 객체가 처음에 가져야할 데이터를 지정.
ContactInfo.py

9.2.2 self에 대해
self는 바로 메소드가 소속되어 있는 객체.
외부에서는 객체이름이 있지만 내부에서는 객체를 지칭할 이름이 없어서 self를 도입.
self를 필수 매개변수로 입력받도록 했다.

9.2.3 정적 메소드와 클래스 메소드
인스턴스 메소드는 인스턴스(객체)에 속한 메소드를 말합니다.
이 말은 인스턴스를 통해 호출가능하다라는 뜻.

정적 메소드는 @staticmethod 데코레이터로 수식하며, self매개변수 없이 정의합니다.
class 클래스이름:
    @staticmethod #staticmethod데코레이터로 수식.
    def 메소드이름(매개변수): #self는 사용하지 않습니다.
        pass
class Calculator:
    @staticmethod
    def plus(a,b): #self가 없다.
        return a+b
인스턴스를 통해서도 접근이 가능하지만 클래스를 통해 호출하는 것이 보통.
다른 프로그래머로 하여금 인스턴스 메소드라고 착각하게 만들 수 있어서.
obj=Calculator()
obj.plus(3,5) #정적 메소드는 이렇게 인스턴스를 만들어 호출하지 않습니다.
a=Calculator.plus(7,4) #정적 메소드는 클래스를 통해 호출하는 것이 보통.
정적 메소드는 self 매개변수를 전달받을 방법이 없으므로 객체/인스턴스 변수에 접근X
따라서 정적 메소드는 객체의 데이터 속성과는 관계가 없는 코드로 구현하는 것이 일반적.
Calculator.py

클래스메소드는 정적 메소드처럼 클래스의 멤버이며, @classmethod데코레이터와 cls 매개변수.
class 클래스이름:
    @classmethod #classmethod데코레이터를 앞에 붙여줍니다.
    def 메소드이름(cls): #메소드의 매개변수를 하나 이상 정의합니다.
        pass
인스턴스 메소드에 self가 필수 매개변수였다면 클래스 메소드는 cls가 필수적.
self는 인스턴스를 나타내고 cls는 클래스를 나타냅니다.
>>>class TestClass:
    @classmethod
    def print_TestClass(cls):
        print(cls)
>>>TestClass.print_TestClass() #클래스를 통한 클래스 메소드 호출
<class '__main__.TestClass'>
>>>obj=TestClass()
>>>obj.print_TestClass() #인스턴스를 통한 클래스 메소드 호출
<class '__main__.TestClass'>
print_TestClass()를 호출할 때마다 TestClass 클래스를 암묵적인 매개변수로 전달.
InstanceCounter.py

9.2.4 클래스 내부에게만 열려있는 프라이빗 멤버
클래스도 안과 밖개념이 있습니다.
class YourClass:
    pass
                                 밖
class MyClass:                   
    def __init__(self):        | 안
        self.message="Hello"   |
                               |
    def some_method(self):     |
        print(self.message)    |

obj=MyClass()                    밖
obj.some_method()
클래스의 안에서만 접근이 가능한 멤버를 일컬어 '프라이빗(Private)'멤버라고 합니다.
반대로 안과 밖 모두에서 접근이 가능한 멤버는 '퍼블릭(Public)'멤버라고 합니다.
키워드를 이용하지 않고 작명법(Naming)으로 구분합니다.
프라이빗 멤버의 명명 규칙
1)두 개의 밑줄 __이 접두사여야 한다. __number(Private)
2)접미사는 밑줄이 한 개까지만 허용된다. __number_(Private)
접미사의 밑줄이 두 개 이상이면 퍼블릭 멤버로 간주. __number__(Public)
>>>class HasPrivate:
    def __init__(self):
        self.public="Public."
        self.__private="Private."
    def print_from_internal(self):
        print(self.public)
        print(self.__private)
>>>obj=HasPrivate()
>>>obj.print_from_internal()
Public.
Private.
>>>print(obj.public)
Public.
>>>print(obj.__private)
#객체 외부에서 접근할 수 없어 오류.

9.3 상속
클래스끼리 물려주는 것을 상속(Inheritance)라고 합니다.
물려받는 클래스(파생 클래스(Derived Class)나 자식클래스)가 
유산을 물려줄 클래스(기반 클래스(Base Class)나 부모클래스)를 지정합니다.
class 기반 클래스:
    #멤버 정의
class 파생 클래스(기반 클래스):
    #멤버를 정의하지 않아도 기반 클래스의 모든 것을 물려받습니다.
    #단, 프라이빗 멤버는 제외.
class Base:
    def base_method(self):
        print("base_method")
class Derived(Base): #상속을 통해 base_method()메소드를 가진다.
    pass

>>>class Base:
    def base_method(self):
        print("base_method")
>>>class Derived(Base):
    pass
>>>base=Base()
>>>base.base_method()
base_method
>>>derived=Derived()
>>>derived.base_method()
base_method

때로는 재활용하고자 하는 클래스의 인스턴스를 데이터 속성으로 갖는 것이
상속보다 더 나은 코드 재사용 방법이 될 수 있습니다.
이런 기법을 포함(Containment)라고 합니다.
class A:
    def methodA():
        pass
class B:
    def __init__(self):
        self.instance_of_A=A() #클래스의 인스턴스를 데이터 속성으로.
    def call_methodA(self):
        self.instance_of_A.methodA()

상속은 자식 클래스가 부모 클래스의 모습을 그대로 이어야 할 때 적합합니다.
컴퓨터의 로컬 디스크 파일에 로그를 남기는 Logger클래스가 있는데 여기에
네트워크로 로그를 전송하는 기능을 추가하고 싶다면 포함보다는 상속.
class Logger:
    def WriteOnFile(self):
        pass
class NetwordLogger(Logger): #상속.
    def WriteOnNetwork(self):
        pass

상속의 중요한 특징 중 하나는 "자식 클래스의 객체를 부모 클래스의 객체로 간주한다"는 것
자식 클래스는 부모 행세를 할 수 있습니다.
>>>class ArmorSuite:
    def armor(self):
        print("armored")
>>>def get_armored(suite): #ArmorSuite클래스를 염두에 두고 작성함.
    suite.armor()
>>>suite=ArmorSuite()
>>>get_armored(suite) #ArmorSuite의 armor()이 호출.
armored
>>>class IronMan(ArmorSuite):
    pass
>>>iron_man=IronMan()
>>>get_armored(iron_man) #함수를 바꾸지 않고 그대로.
armored
자식 클래스는 기반 클래스 행세를 잘 해냅니다.
이를 통해 코드는 업그레이드가 비교적 용이한 편.
>>>class A:
    def __init__(self):
        print("A.__init__()")
        self.message="Hello"
>>>class B(A): #B는 A로부터 상속.
    def __init__(self):
        print("B.__init__()")
>>>obj=B() #B의 __init__()만 호출.
B.__init__()
>>>obj.message
#A로부터 message를 물려받지 못해 에러호출
파이썬은 명시적인 것을 좋아합니다.
기반 클래스의 초기화 메소드를 프로그래머가 명시적으로 호출해주기를 원합니다.
>>>class A:
    def __init__(self):
        print("A.__init__()")
        self.message="Made in A"
>>>class B(A):
    def __init__(self):
        A.__init__(self) #B 클래스 안에서 A메소드를 호출.
        print("B.__init__()")
>>>obj=B()
A.__init__()
B.__init__()
>>>obj.message #A.__init__()호출해서 B의 인스턴스가 message데이터속성을 가집니다.
'Made in A'
하지만 이런식으로는 기반클래스를 바꾸면 모든 것을 수정해야됩니다.

모든 클래스의 시조 object
상속할 부모 클래스를 명시하지 않은 채 정의된 클래스는 object로부터 상속받습니다.
class A:
    pass
class A(object):
    pass
위의 두 class는 같습니다.

9.3.1 super()
super()은 부모 클래스의 객체 역할을 하는 프록시(Proxy)를 반환하는 내장함수.
super()함수의 반환값을 상위 클래스의 객체로 간주하고 코딩을 해도됩니다.
class A:
    def __init__(self):
        self.message="Hello"
class B(A):
    def __init__(self):
        super().__init__() #A.__init__(self)와 동일한 결과.
기반 클래스가 다른 클래스로 교체되거나 수정되어도 파생클래스가 받는 영향을 최소화.

super() 초기화뿐만아니라 객체 내의 어떤 메소드에서든 부모 클래스에 정의되어
있는 버전의 메소드를 호출하고 싶으면 super()를 이용.
super.py

super()없이 상위 클래스의 __init__()메소드를 호출하는 경우
파생 클래스의 구현이 비워져 있는경우, 파생 클래스의 인스턴스를 생성할 때
부모 클래스의 __init__()메소드가 호출됩니다.
>>>class Base:
    def __init__(self):
        print("Base")
>>>class Derived(Base):
    pass
>>>d=Derived() #Base.__init__()가 호출됨.
Base

9.3.2 다중 상속
자식 하나가 여러 부모로부터 상속받는 것.
파이썬에서는 파생 클래스를 정의할 때 기반 클래스의 이름을 콤마(,)로 구분해서
쭉 적어주면 다중 상속이 이루어집니다.
class A:
    pass
class B:
    pass
class C:
    pass
class D(A,B,C):
    pass

class A:
    def method(self):
        print("A")
class B(A):
    def method(self):
        print("B")
class C(A):
    def method(self):
        print("C")
class D(B,C):
    pass
D는 B,C로부터 상속을 받고 B와 C는 같은 부모인 A로부터 상속을 받습니다.
죽음의 다이아몬드라고도 불립니다.
B와 C는 method()를 재정의하고 D는 method()를 재정의하지 않았습니다.
정말애매하지만 파이썬은 다중 상속을 처리할 때 부모 클래스의 목록에서 가장 앞에
있는 클래스의 메소드를 물려줍니다.
>>>obj=D()
>>>obj.method()
B

9.3.3 오버라이딩
Overriding은 기반 클래스로부터 상속받은 메소드를 다시 정의하는 것.
method()를 물려받을 수 있었지만 자신만의 method()를 새로 정의했었습니다.
메소드를 부모로부터 그대로 물려받을 수도 있고 재정의할 수도 있습니다.
재정의하면서도 부모 버전의 메소드를 활용할 수도 있습니다. super()를 통해
>>>class Car:
    def ride(self):
        print("Run")
>>>class FlyingCar(Car):
    def ride(self):
        super().ride() #super()를 통해 부모 클래스 버전의 메소드를 호출
        print("Fly")
>>>my_car=FlyingCar()
>>>my_car.ride()
Run
Fly

9.4 데코레이터:함수를 꾸미는 객체
데코레이터는 __call__()메소드를 구현하는 클래스
__call__()은 객체를 함수 호출 방식으로 사용하게 만드는 마법 메소드입니다.
>>>class Callable:
    def __call__(self):
        print("I am called.")
>>>obj=Callable()
>>>obj() #인스턴스 뒤에 괄호를 붙여 호출하면 내부적으로는 __call__메소드가 호출됨.
I am called.

데코레이터는 자신이 수식할 함수나 메소드를 내부에 받아놓아야 합니다.
그래서 데코레이터는 __init__()메소드의 매개변수를 통해 함수나 메소드를 
넘겨받아 데이터속성에 저장.
class MyDecorator:
    def __init__(self,f): #__init__() 매개변수를 통해 함수를 받고 데이터 속성에 저장.
        print("Initializing MyDecorator...")
        self.func=f
    def __call__(self):
        print("Begin : {0}".format(self.func.__name__))
        self.func() #__call__()호출되면 생성자에서 저장해둔 함수를 호출.
        print("End : {0}".format(self.func.__name__))
데코레이터가 하는 일의 본질은 함수를 '대리 호출'해주는 것뿐.
@statimethod @classmethod에서도 함수의 머리 위에 장식처럼 꽂아 사용해서.

데코레이터를 사용하는 방법 1:생성자
@데코레이터의 꼴과는 다른 모습을 하는 데코레이터의 생성자를 이용할 수 있었습니다.
def print_hello():
    print("Hello.")
print_hello=MyDecorator(print_hello)
print_hello는 MyDecorator의 객체를 가리킵니다.
print_hello가 원래 가리키고 있던 함수도 안에 있습니다.
print_hello가 __call__()를 구현하는 MyDecorator의 인스턴스기 때문에 함수처럼 호출가능.
print_hello()
decorator1.py

데코레이터를 사용하는 방법 2:@기호
데코레이터는 @데코레이터의 꼴로 사용하는 것이 바람직.
def print_hello():                            @MyDecorator
    print("Hello.")             <===>         def print_hello():
print_hello=MyDecorator(print_hello)              print("Hello.")
decorator2.py

9.5 for문으로 순회를 할 수 있는(Iterable) 객체 만들기
9.5.1 이터레이터와 순회 가능한 객체
for문을 실행할 때 가장 먼저 하는 일은 순회하려는 객체의 __iter__()를 호출하는 것.
__iter__()는 이터레이터(Iterator)라고 하는 특별한 객체를 for문에게 반환합니다.
이터레이터는 __next__()를 구현하는 객체를 말하는데, for문은 수행할 때마다
__next__()를 호출하여 다음 요소를 얻어냅니다.
range()함수가 반환하는 것이 사실은 __iter__()를 구현하는 순회가능한 객체.
>>>iterator=range(3).__iter__()
>>>iterator.__next__()
0
>>>iterator.__next__()
1
>>>iterator.__next__()
2
>>>iterator.__next__()
#다음 요소가 없을 때에는 StopIteration 예외를 발생.
iterator.py

9.5.2 제네레이터(Generator)
이터레이터처럼 동작하는 함수이지만, 더 간편하게 구현할 수 있습니다.
클래스를 정의하지 않아도 되고 __iter__()나 __next__()구현할 필요도 없습니다.
함수 안에서 yield문을 이용하여 값을 반환하면 됩니다.
yield문은 return문처럼 함수를 실행하다가 반환하지만, 함수를 종료시키지않고 중단만합니다.
>>>def generator():
    yield 0
    yield 1
    yield 2
    yield 3
>>>iterator=generator()
>>>iterator.__next__()
0
>>>iterator.__next__()
1
>>>iterator.__next__()
2
>>>iterator.__next__()
3
>>>iterator.__next__()
#더 이상 값이 없을 때는 에러.
generator.py

9.6 상속의 조건: 추상 기반클래스
부모 클래스를 정의할 때 자식 클래스가 갖춰야 하는 모습을 규약으로 정의해 두고
규약을 따르지 않는 자식은 자식으로 인정하지 않는 겁니다.
추상 기반클래스는(Abstact Base Class)는 자식클래스가 갖춰야할 특징을 강제하는 기능.
자식클래스가 만족하지 않는다면 인스턴스를 생성할 때 파이썬은 TypeError예외.
abc모듈의 ABCMeta클래스와 @abstractmethod데코레이터를 이용합니다.
from abc import ABCMeta
from abc import abstractmethod
class AbstractDuck(metaclass=ABCMeta):
    @abstractmethod
    def Quack(self):
        pass
파이썬에서는 모든 것이 객체입니다. 객체의 자료형인 클래스가 존재해야 합니다.
메타 클래스는 '클래스에 대한 정보를 갖고 있는 클래스'입니다.
metaclass에 별도의 메타 클래스를 지정하지 않으면 type 클래스가 기본적으로 사용됨.
ABCMeta메타클래스는 클래스가 특정 메소드를 구현하는지를 테스트하는 기능.
AbstractDuck의 파생클래스는 @abstractmethod로 정의된 Quack()을 반드시 구현해야함.
>>>from abc import ABCMeta
>>>from abc import abstractmethod
>>>class AbstractDuck(metaclass=ABCMeta):
    @abstractmethod
    def Quack(self):
        pass
>>>class Duck(AbstractDuck):
    pass
>>>duck=Duck()
#에러 메시지
>>>class Duck(AbstractDuck):
    def Quack(self):
        print("[Duck] Quack")
>>>duck=Duck()
>>>duck.Quack()
[Duck] Quack
 
'''