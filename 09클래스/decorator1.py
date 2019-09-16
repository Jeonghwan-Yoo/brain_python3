class MyDecorator:
    def __init__(self,f):
        print("Initializing MyDecorator>..")
        self.func=f #func데이터 속성이 print_hello를 저장.
    def __call__(self):
        print("Begin : {0}".format(self.func.__name__))
        self.func()
        print("End : {0}".format(self.func.__name__))

def print_hello():        
    print("Hello.")

print_hello=MyDecorator(print_hello) #인스턴스가 만들어지며 __init__()가 호출
print_hello() #__call__()덕분에 MyDecorator 객체를 호출하듯 사용가능.