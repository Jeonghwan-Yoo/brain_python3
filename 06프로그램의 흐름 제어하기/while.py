print('몇 번 반복할까요? : ')
limit=int(input())

count=0
while count<limit: #count가 limit보다 작은 동안
    count=count+1
    print('{0}회 반복.'.format(count))

#count<limit이 거짓이면 반복을 멈춥니다.
print('반복이 종료되었습니다.')