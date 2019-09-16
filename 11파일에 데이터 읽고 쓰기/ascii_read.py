#errors='ignore'로 해당 인코딩으로 처리가 안되는 문자열이 있을 때는 지나치도록.
with open('greetings_utf8.txt','r',encoding='ascii',errors='ignore') as file:
    lines=file.readlines()
    line=''
    for line in lines:
        print(line,end='')
#인코딩으로 처리가 안되는 문자열이 있을 때는 무시해서 ?가 출력됨.