import threading

count=0

def on_timer():
    global count
    count+=1
    print(count)

    #10회 실행된 후 다시 Timer객체를 만들고 start()를 호출하여 1초 후에 다시실행할 준비.
    #11을 출력할 준비
    timer=threading.Timer(1,on_timer)
    timer.start()

    if count==10: #그러나 조건문에 의해 준비 중이던 timer 객체는 cancel()을 호출당함. 
        print("Canceling timer...")
        timer.cancel()
    
    '''
    더 효율적이게 짜려면.
    if count<10:
        timer=threading.Timer(1, on_timer)
        timer.start()
    '''
print("Starting timer...")
on_timer()
