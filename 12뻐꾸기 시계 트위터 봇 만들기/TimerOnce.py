import threading
import datetime

def function_a():
    print("Timer expried")
    print(datetime.datetime.now()) #현재 시간 출력

print(datetime.datetime.now()) #현재 시간 출력
#10초 후 function_a() 함수를 실행할 Timer 생성하고 start() 메소드 호출.
threading.Timer(10,function_a).start() 