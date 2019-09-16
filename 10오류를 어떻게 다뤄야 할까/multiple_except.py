my_list=[1,2,3]

try:
    print("첨자를 입력하세요:")
    index=int(input())
    print(my_list[index]/0)
except ZeroDivisionError: #0~2사이로 입력된다면
    print("0으로 나눌 수 없습니다.")
except IndexError: #2를 벗어나면
    print("잘못된 첨자입니다.")
#첨자를 입력하세요:
#2
#0으로 나눌 수 없습니다.

#첨자를 입력하세요:
#10
#잘못된 첨자입니다.