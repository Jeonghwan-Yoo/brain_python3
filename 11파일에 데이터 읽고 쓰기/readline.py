with open('movie_quotes.txt','r') as file:
    line=file.readline()
    #readline()은 파일의 끝에 도달하면 ''를 반환. 빈 줄 읽으면 개행문자 반환.
    #한 줄 다 읽고 \n를 만나서 커서 아래로 이동.
    while line!='': 
        print(line, end='')
        line=file.readline()