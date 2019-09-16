with open('movie_quotes.txt','r') as file:
    lines=file.readlines()
    
    line='' #없어도 출력은 된다.
    for line in lines:
        print(line, end='')