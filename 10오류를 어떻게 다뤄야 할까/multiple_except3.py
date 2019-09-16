my_list=[1,2,3]

try:
    print("첨자를 입력하세요:")
    index=int(input())
    print(my_list[index]/0)

except ZeroDivisionError as err: #ZeroDivisionError만 처리함
    print("0으로 나눌 수 없습니다. ({0})".format(err))
#위에 구체적인 except가 있다면 먼저 올수는 없다. 구체적인것을 안써도 된다.
except : #ZeroDivisionError를 제외한 모든 예외들이 발생할 때. 
    print("예외가 발생했습니다.")