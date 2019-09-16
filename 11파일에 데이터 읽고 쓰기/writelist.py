#리스트에 담아 사용중인 여러 중의 문자열을 파일에 저장할 때
lines=["we'll find a way we always have - Interstellar\n",
    "I'll find you and I'll kill you - Taken\n",
        "I'll be back - Terminator 2\n"]

with open('movie_quotes.txt','w') as file:
    for line in lines:
        file.write(line)