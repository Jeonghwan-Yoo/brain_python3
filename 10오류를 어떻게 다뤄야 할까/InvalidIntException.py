#문자열을 정수로 변환하는 convert_to_integer()함수가
#매개 변수를 확인하다가 자신이 처리할 수 없는 문자가 들어 있으면 InvalidIntException()
class InvalidIntException(Exception):
    def __init__(self, arg):
        super().__init__('정수가 아닙니다. : {0}'.format(arg))

def convert_to_integer(text):
    if text.isdigit(): #부호(+,-) 처리 못함.
        return int(text)
    else:
        raise InvalidIntException(text)

if __name__=='__main__':
    try:
        print('숫자를 입력하세요:')
        text=input()
        number=convert_to_integer(text)
    except InvalidIntException as err:
        print('예외가 발생했습니다 ({0})'.format(err))
    else:
        print('정수 형식으로 변환되었습니다. : {0}({1})'.format(number,type(number)))
