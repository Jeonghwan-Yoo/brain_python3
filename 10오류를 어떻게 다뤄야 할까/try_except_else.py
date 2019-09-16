my_list=[1,2,3]

try:
    print("첨자를 입력하세요:")
    index=int(input())
    print("my_list[{0}]:{1}".format(index,my_list[index]))
except Exception as err: #잘못된 첨자가 입력됐을 때
    print("예외가 발생했습니다 ({0})".format(err))
else: #정상적인 첨자가 입력됐을 때
    print("리스트의 요소 출력에 성공했습니다.")
