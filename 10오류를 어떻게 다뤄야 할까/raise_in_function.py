def some_function():
    print("1~10 사이의 수를 입력하세요:")
    num=int(input())
    if num<1 or num>10:
        raise Exception("유효하지 않은 숫자입니다. : {0}".format(num))
    else:
        print("입력한 수는 {0}입니다.".format(num))

try:
    some_function()
except Exception as err: #except문으로 처리되지 않으면 함수 밖으로 다시 던져집니다.
    print("예외가 발생했습니다. {0}".format(err))