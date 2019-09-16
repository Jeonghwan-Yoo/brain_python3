#cls 매개변수를 통해 클래스 속성에 접근하는 예제
#클래스의 객체가 얼마나 생성되었는지를 셉니다.
class InstanceCounter:
    count=0
    def __init__(self): #인스턴스가 만들어질 때마다 실행. 수를 세기에 적합.
        InstanceCounter.count+=1
    @classmethod
    def print_instance_count(cls): #클래스 속성인 count를 출력.
        print(cls.count)
    
if __name__=='__main__':
    a=InstanceCounter()
    InstanceCounter.print_instance_count()

    b=InstanceCounter()
    InstanceCounter.print_instance_count()

    c=InstanceCounter()
    c.print_instance_count()