class Calculator:
    @staticmethod 
    def plus(a,b): #self매개변수가 없습니다.
        return a+b
    @staticmethod
    def minus(a,b):
        return a-b
    @staticmethod
    def multiply(a,b):
        return a*b
    @staticmethod
    def divide(a,b):
        return a/b

if __name__=='__main__':
    print("{0} + {1} = {2}".format(7,4,Calculator.plus(7,4))) #클래스 이름을 통해 접근.
    print("{0} - {1} = {2}".format(7,4,Calculator.minus(7,4)))
    print("{0} * {1} = {2}".format(7,4,Calculator.multiply(7,4)))
    print("{0} / {1} = {2}".format(7,4,Calculator.divide(7,4)))
    