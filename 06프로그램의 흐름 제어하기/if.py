import sys #파이썬 프로그램을 종료하는 exit()을 사용하기 위해

print('수를 입력하세요 : ')
a=int(input())

if a==0:
    print('0은 나눗셈에 이용할 수 없습니다.') #경고 메시지를 출력한 뒤
    sys.exit(0) #프로그램을 종료시킵니다.

print('3 /', a, '=', 3/a)