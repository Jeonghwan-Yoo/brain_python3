import struct

struct_fmt='=16s2fi' #char[16], float[2], int
struct_len=struct.calcsize(struct_fmt)

cities=[]
with open('cities.dat',"rb") as file:
    while True:
        buffer=file.read(struct_len)
        if not buffer: #파일의 끝에 도달하면 while 탈출.
            break
        city=struct.unpack(struct_fmt,buffer)
        cities.append(city)

    for city in cities:
        #pack하는 과정에서 문자를 할당하고 남은 공간에 채워진 \x00를 디코딩 한 후
        #빈 문자열로 다시 바꿔넣습니다.
        name=city[0].decode(encoding='utf-8').replace('\x00','')
        print('City:{0}, Lat/Long:{1}/{2}, Population:{3}'.format(
            name, city[1], city[2], city[3]
        ))