'''
16.1 이미지 매직
이미지 매직(Image Magick)은 이미지 편집 소프트웨어입니다. CMD에서 실행하는 것이 특징.
이미지 형식 변환, 이미지 회전, 합성 등등 편집에 필요한 다양한 기능을 제공.
다양한 프로그래밍 언어에 대한 인터페이스가 존재합니다.

16.1.1 이미지 매직 설치

16.1.2 Wand:이미지 매직 파이썬 API 라이브러리

16.1.3 Wand 설치
>pip install Wand

16.2 Wand를 이용한 이미지 편집
관련 모듈을 코드에 반입하는 것으로 시작됩니다. 사용할 모듈은 wand.image
이 모듈 안에서도 특히 Image클래스를 주로 사용.
파일 형식 바꾸기:Image.convert()
크기 바꾸기:Image.resize()
이미지 자르기:슬라이스 연산자. image[0:0,100:200]
이미지 회전:Image.rotate()
이미지 뒤집기:Image.flip() #상하뒤집기
             Image.flot() #좌우뒤집기
이미지 명도, 채도, 색상 변경하기:Image.modulate()
이미지 합성:Image.composite()
워터 마크:Image.watermark()

이미지에 도형이나 텍스트를 그려 넣을 때는 image.drawing모듈의 Drawing클래스도 사용
Drawing.line()
Drawing.rectangle()
Drawing.text()
Drawing.draw()

이미지 복사 플로그램. 이미지 파일을 열고, 복제한 뒤, 복제본을 저장.
image_copy.py

16.2.1 이미지 파일 형식 바꾸기
wand.Image클래스의 convert()메소드 이용.
새 이미지 형식의 이름을 매개변수로 받습니다.
지원하는 이미지 형식
bmp:비트맵 이미지 파일 형식. 1~24비트의 색을 표현할 수 있음
gif:Graphics Interchange Format. 최대 256색까지 저장할 수 있는 비손실 압축 형식
jpeg:Joint Photographic Experts Group. 손실 압축 이미지 표준
png:Portable Network Graphics. gif의 표현한계,특허 문제를 해소하기 위한 개발된 파일 형식.
tiff:Tagged Image File Format. 스캐너 제조사들이 개발한 파일 형식
ico:마이크로소프트 윈도의 아이콘에 쓰이는 그림 파일 형식
pdf:Portable Document Format. 어도비의 전자 문서 형식
psd:Photoshop document. 어도비의 포토샾 파일 형식
사용자로부터 원본 파일의 이름과 변환할 파일 형식을 받으면, 해당 복제본을 만들어 저장.
convert_format.py

16.2.2 이미지 크기 바꾸기
이미지의 크기를 변경할 때는 resize()를 이용
재조정할 이미지의 너비와 높이를 매개변수로 입력받습니다.
with Image(filename=original_path) as image:
    image.resize(100, 50) #어떤 이미지이건 너비 100, 높이 50으로 크기 변경
고정된 크기로 변경하면 원본 비율이 망가질 수 있다.
따라서 고정 크기 대신 '비율'을 입력 받아 크기를 조정.
resize.py

16.2.3 이미지 자르기
이미지 자르기를 위한 슬라이스 연산자([]). 대각선 (x1, y1), (x2,y2)이루어지는 사각형을 잘라냄
cropped=image[x1:x2, y1:y2]
원본 이미지를 사용자로부터 입력 받은 줄과 칸 수로 나누어 자르는 기능.
crop.py

16.2.4 이미지 회전
Image클래스의 rotate()메소드를 이용
매개변수는 시계방향 회전각도와 회전시켰을때 남는 공간에 채워넣을 색상.
rotated.rotate(degree, background=Color(bgcolor))
사용자로부터 회전 각도와 배경색을 입력받아 이미지를 회전시키는 기능
rotate.py

16.2.5 이미지 뒤집기
상하로 뒤집을 때는 flip(), 좌우로 뒤집을 때는 flop()
with Image(filename=original_path) as image:
    image.flip() #상하
    imgae.flop() #좌우
flip()와 flop()을 이용해서 사용자로부터 입력받은 이미지를 뒤집습니다.
flipflop.py

16.2.6 이미지에 텍스트와 도형 넣기
텍스트와 도형을 그려 넣을 때는 wand.drawing.Drawing클래스가 필요.
먼저 wand.drawing모듈로부터 Drawing클래스를 반입합니다.
from wand.drawing import Drawing
from wnad.image import Image
인스턴스를 생성
with Image(filename=original_path) as image:
    with Drawing() as draw:
Drawing 객체의 메소드를 이용해 도형을 그려넣을 때, 외곽선 색과 크기 등을 지정후 메소드호출.
draw.stroke_color=Color('#FF0000')
draw.fill_color=Color('#FFFFFFA0')
draw.rectangle(left=10, top=15, width=220, height=55) #사각형 그리기
draw.stroke_color=Color('#00FF00')
draw.stroke_width=2
draw.line((10,5),(230,5)) #직선 그리기
문자를 그려넣는 text()메소드를 호출하기전에 폰트를 지정해야 합니다.
draw.font='C:\Windows\Fonts\JOKERMAN.TTF'
draw.font_size=30
draw.text(20,51,text)
그리기가 끝났으면 Drawing.draw()를 이용해 작업 결과를 Image객체에 출력해줘야 합니다.
Drawing.draw(draw,image)
Drawing객체를 이용해서 이미지에 워터마크를 그려 넣는 작업.
watermark_text.py

16.2.7 이미지 명도, 채도, 색상 변경하기
Color는 Brightness, Saturation, Hue 세 가지 속성을 지닙니다.
Brightness:색의 밝기를 나타냅니다. 명도가 높으면 밝고 가벼운 느낌. 명도가 낮으면 
어둡고 무거운 느낌. 백분율로 표현하며 가장 높은 건 흰색, 가장 낮은 건 검정색.
Saturation:색의 선명함을 나타내는 척도. 유채색(흰~검계열이 아닌)에만 존재하는 속성으로
채도가 높을수록 색의 순도가 높고 선명하며 낮을수록 색이 탁해집니다.
백분율로 표현하며 무채색은 0%. 순수한 유채색은 채도가 100%
Hue:색의 종류를 말하지만, '색상환에 대응하여 빨강을 기준으로 0도가 되는 각도'
0빨강, 30주황, 60노랑, 90연두...360빨강
각도로 당연히 0~360값을 가지지만, modulate()는 백분율로 변환해서 입력해야 합니다.
value = (Hue * (100 / 180)) + 100을 이용해 대입.
modulate.py

16.2.8 이미지 합성
이미지 두 개를 하나로 합치는 것을 합성.
Image객체의 composite()메소드를 이용한다.
image1.composite(image2, 100, 100) #image1위의 (100,100) 위치에 image2를 합성해라
합성을 더 자연스럽게 하려면 한쪽 이미지를 살짝 투명하게.
투명하게 만드려면 transparentize()메소드를 이용한다. 매개변수는 0~1의 값.
image2.transparentize(0.7) #투명도를 70%로 변환.
composite.py

16.2.9 워터 마크
composite()와 transparentize()기능을 한번에 수행하는 메소드 watermark()
image2.transparentize(0.7);image1.composite(image2,100,100)을
image1.watermark(image2, 0.7, 100, 100)으로 나타낼 수 있다.
첫 번째 매개변수는 Image객체, 두 번째는 투명도, 세 번째와 네 번째는 합성할 이미지의 x,y
watermark.py



'''