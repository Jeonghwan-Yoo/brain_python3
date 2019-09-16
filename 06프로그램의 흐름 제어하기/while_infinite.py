while True:
    print('반복을 계속할까요? [예/아니오] : ')
    answer=input()

    if answer=='예':
        print('반복을 계속합니다.')
    elif answer=='아니오':
        break #반복문의 실행을 취소시키는 기능.
    else:
        print('정상적인 답변이 아닙니다.')