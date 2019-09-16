'''
17.1 pygame 소개
게임과 같은 멀티미디어 소프트웨어 개발을 위해 만들어진 파이썬 라이브러리
SDL(Simple DirectMedia Layer) 라이브러리를 기반으로 다양한 운영체제를 지원하고,
조이스틱 입력, 그래픽 처리, 사운드 재생 등 다양한 기능을 탑재.
pygame은 오픈소스로 개발되고 있고, API레퍼런스를 비롯하여 다양한 정보를 얻을 수 있다.

17.1.1 pygame 라이브러리 설치
pygame-xxxxxx-cp36-none-win_amd64.whl 설치파일
>pip install pygame...whl

17.1.2 게임 루프
게임 루프는 게임과 사용자 간의 지속적인 상호 작용을 하는 무한 루프입니다.
게임이 자신의 상태를 화면에 표시하면 사용자는 표시된 상태에 따라 조이스틱이나
키보드 등의 명령을 입력합니다.
게임은 이렇게 입력된 명령을 처리하고 자신의 상태를 변경한 후, 다시 사용자에게 상태를 화면에.
게임의 시작부터 끝까지 이 과정을 지속적으로 반복합니다.
1)사용자 입력 처리:사용자가 조이스틱, 키보드를 통해 입력한 명령을 처리합니다.
2)게임 상태 업데이트:주인공의 에너지, 총알 수, 위치 등을 갱신합니다.
3)게임 상태 그리기:갱신된 내용을 화면에 그려 넣습니다.

17.1.3 pygame을 사용하는 방법
1)pygame 관련 모듈 반입
2)pygame 초기화
3)스크린 크기 설정
4)게임 루프
5)pygame 관련 모듈 사용 자원 해제

1)pygame 관련 모듈 반입
import pygame

2)pygame 초기화
모듈을 반입한 후에는 pygame.init()를 호출해 관련 모듈을 초기화합니다.
pygame.init()

3)스크린 크기 설정
pygame.display.set_mode()를 호출하여 게임 스크린의 크기를 지정합니다.
set_mode()는 (너비, 높이)로 이루어진 튜플로 매개변수로 입력받고
게임 상태를 표시할 도화지 역할을 하는 Surface객체를 반환합니다.
screen=pygame.display.set_mode((400,300))
게임 루프를 작성하기 전에 루프의 주기를 결정할 pygame.time.Clock 객체를 생성
clock=pygame.time.Clock()

4)게임 루프
무한 루프를 하나 만들고 사용자 입력 처리, 게임 상태 업데이트, 게임 그리기 코드를 구현.
수행 후에는 앞에서 만든 clock객체의 tick()을 호출해야 합니다.
tick()은 FPS(Frame Per Second)를 매개변수로 받아 지정한 시간 간격으로 게임 루프를 실행.
tick()메소드에 FPS를 30으로 입력하면 게임 루프는 1초에 30번씩만 실행됩니다.
while True:
    #1)사용자 입력 처리
    #2)게임 상태 업데이트
    #3)게임 상태 그리기
    clock.tick(30)

5)pygame 관련 모듈 사용 자원 해제
사용자의 명령이나 게임 상태 업데이트에 의해서 게임 루프를 빠져 나오게 되면 
애플리케이션이 종료되기 전에 pygame.quit()을 호출합니다.
pygame.quit()은 pygame의 모듈들이 사용하고 있던 자원들을 정리합니다.
pygame.quit()

17.1.4 처음 만들어보는 pygame 애플리케이션
시간이 지남에 따라 스크린의 색상을 하얀색에서 빨간색으로 점점 변화시키는 기능.
완전히 빨간색이 되면 다시 하얀색이 되어 빨간색으로 변하기를 반복.
hello_pygame.py

17.1.5 pygame에서의 사용자 입력 처리
사용자 입력 이벤트를 담당하는 모듈은 pygame.event입니다.
pygame.event.get()는 게임의 이벤트 큐에 있는 모든 이벤트를 순서열로 만들어 반환.
events=pygame.event.get()
게임 QUIT:게임종료
키보드 KEYDOWN:키누름
키보드 KEYUP:키누름 해제
마우스 MOUSEMOTION:마우스 움직임 
마우스 MOUSEBUTTONUP:마우스 버튼 누름 해제 
마우스 MOUSEBUTTONDOWN:마우스 누름
조이스틱 JOYAXISMOTION:조이스틱 중심축 움직임
조이스틱 JOYBALLMOTION:조이스틱 볼이 움직임
조이스틱 JOYHATMOTION:조이스틱 햇 스위치 움직임
조이스틱 JOYBUTTONUP:조이스틱 버튼 누름
조이스틱 JOYBUTTONDOWN:조이스틱 버튼 누름 해제
스크린 VIDEORESIZE:스크린 사이즈 변경
스크린 VIDEOEXPOSE:스크린이 다시 그려져야함
스크린 ACTIVEEVENT:게임 윈도우 활성화/비활성화
기타 USEREVENT:사용자 정의 이벤트
게임 루프에서 빠져나왔지만 사용자에게 게임을 종료할 것인지를 묻는 절차를 넣을 수 있고,
상대방에게 게임 종료 메시지를 송신하는 절차를 넣을 수도 있습니다.
사용자가 키보드 이벤트를 제공할 때, 이벤트가 발생한 키의 이름과 종류를 제목 표시줄에 출력.
keyboard_input.py

pygame.event.get()은 키를 눌렀을 때의 최초의 이벤트만 감지합니다.
사용자가 특정 키를 계속 누르고 있는지를 알아내야 할 때는 pygame.key.get_pressed() 이용
이 함수는 전체 키 배열에 대해 키가 현재 눌려져 있는지의 여부를 bool형식의 튜블로 반환
키가 눌려져 있다면 True를 반환.
스페이스키가 눌려져 있는지를 알고 싶을 때는 pygame.key.get_pressed()가 반환한 튜플에
해당 키를 나타내는 상수(pygame.K_SPACE)를 첨자로 넘기면 됩니다.
keys=pygame.key.get_pressed()
if keys[pygame.K_SPACE]:
    print("스페이스 키 눌렸음!")
커서 키가 눌려져 있는지를 감시하고 현재 눌려져 있는 키의 이름을 출력.
keyboard_input2.py

17.1.6 pygame으로 그리기
텍스트 그리기
텍스트를 그릴 때는 pygame.font.SysFont클래스를 이용
#1)SysFont 생성자에 폰트명과 폰트 크기를 입력
sf=pygame.font.SysFont("Monospace",20)
#2)Sysfont.render()가 하는 일은 텍스트를 그려넣은 Surface 객체를 반환하는 것.
이 메소드의 1번째 매개변수는 출력할 텍스트, 2번쨰는 안티알리아싱(Anti-aliasing)여부,
3번째 매개변수는 텍스트의 색상
text=sf.render("Hello, World.",True,(0,0,255))
#3)Surface.blit()은 다른 Surface 객체를 자신에게 그려넣는 일을 함
이 메소드의 1번째의 매개변수는 그려넣을 Surface 객체.
2번째의 매개변수는 해당 Surface 객체를 그려 넣을 좌표
screen.blit(text, (10,10))
text_render.py

도형그리기
pygame.draw.line(Surface,color,start_pos,end_pos,width=1):직선을 그립니다.
pygame.draw.rect(Surface,color,Rect,width=0):직사각형을 그립니다.
pygame.draw.polygon(Surface,color,pointlist,width=0):다각형을 그립니다.
pygame.draw.ellipse(Surface,color,Rect,width=0):타원을 그립니다.
게임 화면의 왼쪽에서 오른쪽으로 도형을 이동시키면서 숫자를 입력했을 때 도형을 변신시킴.
shapes.py

이미지 그리기
pygame.image.load()함수는 이미지 파일을 읽어 들여 Surface객체를 만들어 반환합니다.
이 함수가 지원하는 이미지 형식은 JPG, PNG, GIF, BMP,...
#load() 함수는 이미지 파일로부터 Surface 객체를 반환
img=pygame.image.load("image.png")
#img 객체가 그려질 위치와 크기를 나타내는 pygame.Rect 객체를 반환.
rect=img.get_rect()
while True:
    screen.blit(img,rect) #img 객체를 그립니다.
이미지 파일을 읽어들여 게임화면에 그리되, 왼쪽에서 오른쪽으로 계속 이동.
image.py

17.1.7 pygame으로 오디오 재생하기
pygame.mixer.Sound 클래스는 오디오를 재생하는 기능을 가지고 있으며,
OGG나 압축되지 않은 WAV형식의 오디오 파일을 지원합니다.
#Sound 생성자에 오디오 파일 경로를 입력
fire_sound=pygame.mixer.Sound('fire.ogg')
#play()메소드는 오디오 파일을 재생
fire_sound.play()
#stop()메소드는 오디오 파일 재생을 중지
fire_sound.stop()
게임이 시작된 후 아무 키나 입력하면 오디오를 재생.
sound.py

17.2 스프라이트의 이해
스프라이트(Sprite)는 다른 이미지와 합성하기 위해 사용하는 이미지나 애니메이션.
스프라이트를 이용하지 않는다면 사람이 달리는 풍경을 매 프레임마다 그려야 합니다.
달리는 사람의 애니메이션만 별도의 스프라이트로 만들고 배경과 합성하면 더 작은 용량으로 효과.
게임 그래픽을 위해 소모되는 메모리도 절약. 객체의 상태 변화나 객체들 간 충돌 처리도 용이.

게임에서는 스프라이트 애니메이션의 각 프레임을 스프라이트 시트(Sprite Sheet)에 모아 사용.
이 스프라이트 시트 내의 프레임을 차례대로 게임 화면에 합성시키면 달리는 사람의 애니메이션.

17.2.1 pygame.sprite.Sprite와 pygame.sprite.Group
pygame.sprite.Sprite 클래스는 스프라이트를 표현하는 클래스.
Sprite클래스는 그대로 사용할 수 없고, 이 클래스를 상속하는 파생 클래스를 정의하고
게임 객체에 필요한 메소드나 데이터 속성을 추가해서 사용해야 합니다.
update():객체의 상태를 업데이트합니다.
add():스프라이트를 그룹에 추가합니다.
remove():스프라이트를 그룹에서 제거합니다.
kill():스프라이트가 속해 있는 모든 그룹에서부터 스프라이트를 제거합니다.
alive():스프라이트가 한 그룹에라도 속해있는지의 여부를 반환합니다.
groups():스프라이트가 속해 있는 모든 그룹을 반환합니다.
update()하나를 제외하면 모두 "그룹"에 관련.
게임 객체의 상태를 관리하는 일은 모두 프로그래머의 몫.

Sprite의 파생 클래스는 다음 사항을 만족.
1)스프라이트 객체를 그룹에 추가하기 전에 Sprite.__int__()메소드를 호출.
2)pygame.Surface 형식의 image 데이터 속성을 할당해둬야 한다.
3)pygame.Rect 형식의 rect 데이터 속성을 할당해둬야 한다.
4)update()메소드를 오버라이드 해야 한다.
만족해 무기를 발사하거나 점프를 하는 등의 고유 기능을 추가할 수 있다.
Sprite클래스의 상속 조건 4가지를 만속시키는 Runner를 정의하고
Runner클래스는 시트를 읽어들이고, update()를 호출할 때마다 프레임을 이동합니다.
SpriteAnimation/runner.py

게임루프 안에서 Runner클래스의 update()를 호출하고 갱신된 이미지를 화면에 넣는다.
SpriteAnimation/sprite_only.py

Sprite클래스는 pygame.sprite.Group클래스와 함께 사용하도록 고안됨.
Group은 Sprite객체의 컨테이너 기능을 하는 클래스.
sprites():이 그룹에 소속되어 있는 모든 스프라이트의 목록을 반환합니다.
copy():그룹을 복사합니다.
add():스프라이트를 그룹에 추가합니다.
remove():스프라이트를 그룹에서 제거합니다.
has():그룹이 특정 스프라이트를 갖고 있는지 확인합니다.
update():그룹에 소속되어 있는 모든 스프라이트 객체의 update()메소드를 호출합니다.
draw():이 메소드의 매개변수로 입력받은 Surface 객체에 대해, 그룹에 소속되어 있는
각 스프라이트 객체의 image 데이터 속성과 rect 데이터 속성을 매개변수로 Surface.blit()호출.
clear():그룹이 갖고 있는 스프라이트 위로 배경을 그립니다.
empty():모든 스프라이트를 그룹에서 제거합니다.

Sprite와 Group을 함께 사용함으로써 스프라이트 객체를 종류별로 분류하기가 쉽습니다.
탄막 슈팅 게임은 많은 스프라이트를 동시에 화면에 그립니다. 개별 스프라이트의 상태를
업데이트하고 화면에 그리는 대신, 종류별로 그룹으로 묶어 상태업데이트와 화면출력을 수행하도록
하면 코드를 훨씬 단순하게 만들 수 있습니다.

Runner스프라이트를 세 개 생성하고 Group객체에 등록합니다. 각 스프라이트에 대해
update()메소드와 blit()대신 Group객체의 update()와 draw()를 호출해 상태를 갱신하고 출력.
SpriteAnimation/sprite_group.py

17.2.2 스프라이트간의 충돌 처리
주인공 스프라이트가 그려지는 영역과 적 스프라이트가 그려지는 영역이 겹치는지를 확인.
pygame.sprite.groupcollide()는 스프라이트 그룹간의 충돌 여부를 평가하고,
충돌이 일어난 스프라이트 객체를 자동으로 그룹에서 제거해줍니다.
게다가 어떤 스프라이트에 충돌이 발생했는지를 dict객체에 담아 출력해줍니다.
while True: #게임 루프
    #1,2는 충돌 테스트를 수행할 그룹, 3,4는 충돌이 발생한 객체를 모든 그룹에서 제거할지.
    collided=pygame.sprite.groupcollide(group1,group2,False,True)
    for item in collided.items():
        print(item)

똑같은 장면 위에 총알이 한 발 등장하고, 오른쪽에서 왼쪽으로 이동하며 Runner와 "충돌"
총알과 부딪힌 Runner스프라이트객체는 하나씩 제거.
SpriteAnimation/sprite_group_collide.py

17.3 투석기 게임

17.3.1 게임 컨셉 및 구조
주인공은 투석기이고 악당은 외계인.
투석기가 준비된 3개의 돌을 다 쓰기 전까지 외계인을 맞추면 클리어, 소진하면 게임오버.
게임 진행에 따라 GAME_INIT, GAME_PLAY, GAME_OVER, GAME_CLEAR 상태를 가짐.
GAME_INIT은 게임 화면에 게임 제목을 표시하고 사용자의 입력을 기다립니다.
사용자가 게임을 시작하면 GAME_PLAY상태로 전이되며, 결과에따라 CLEAR나 OVER상태.

투석기가 발사한 돌은 곡선을 그리는 공식을 알아내야 구현할 수 있다.

17.3.2 게임에 사용할 상수 정의
중력 가속도가 9.8이 아닙니다. 물리 세계와 컴퓨터의 화면속은 완전히 다른 세계.
모든 것이 물리 세계와는 다르게 나타납니다. 눈에 그럴듯하게 눈속임.
Catapult/const.py

17.3.3 스프라이트 클래스 정의:배경, 투석기, 돌, 외계인, 폭발
게임에 사용할 스프라이트의 부모 클래스
Animation클래스는 Sprite를 상속하는 한편, Catapult, Stone, Alien, Explosion의 부모.
이 클래스의 구현 목적은 스프라이트 클래스들이 공통적으로 사용할 기능을 구현해 상속.
init_animation()은 스프라이트 시트 파일을 읽고 FPS에 따른 프레임 변경 시간 등 초기화.
calc_next_frame()은 시간이 얼마나 지났는지를 보고 애니메이션 프레임을 전환할지 결정.
Catapult/animation.py

Stone 스프라이트 클래스
투석기가 던지는 돌을 표현합니다.
각 프레인 크기는 8픽셀이면, 총 프레임 수는 4개.
Stone은 발사되지 전에는 STONE_READY이다가 발사명령을 입력하면 setup()을 통해
발사파워, 발사각, 발사 위치를 객체에 저장한 후 상태를 STONE_FLY로 변경.
STONE_FLY가 된 Stone 객체는 게임 루프가 호출하는 move()를 통해 외계인을 향해 날아감.
Stone의 위치가 게임 화면을 벗어나면 상태를 다시 STONE_READY로 돌려 발사 준비 상태로.
move()는 내부적으로 calculate_position()과 map_position()을 호출.
calculate_position()은 포물선 공식을 이용해 시간의 변화에 따른 돌의 위치를 계산하고,
map_position()은 calculate_position()이 계산한 결과를 게임화면 좌표에 맞춰 변환.
Catapult/stone.py

Catapult 스프라이트 클래스 정의
다섯 프레임으로 이루어진 시트. 각 프레임은 픽셀입니다.
투석기를 앞/뒤로 이동시키는 forward()/backward(), 돌을 발사하는 fire()메소드.
fire()는 게임 루프로부터 발사 파워와 발사각을 입력받아 데이터 속성에 저장하고,
Catapult 객체의 상태를 CATAPULT_FIRE로 변경.
update()가 호출될 때 상태를 확인하고 발사 애니메이션을 실행합니다.
발사 애니메이션의 끝에 도달하면 Catapult는 다시 CATAPULT_READY로 돌아가고,
stone객체의 setup()을 호출함으로써 돌이 날아가도록 만듭니다.
setup()호출받은 stone은 STONE_FLY로 바껴 외계인을 향해 날아갑니다.
catapult.py

Alien 스프라이트 클래스 정의
Alien클래스는 alien.png를 스프라이트 시트로 이용.
애니메이션의 각 프레임의 크기는 32*32이며 총 프레임의 수는 3개 입니다.
숨 쉬는 것 말고는 특별한 기능이 없습니다.
Catapult/alien.py

Explosion 스프라이트 클래스 정의
돌과 외계인이 충돌했을 때 사용됩니다.
스프라이트 시트 이미지는 explosionsprites.png.
각 프레임은 픽셀의 크기를 가지며 모두 25개로 이루어져 있습니다.
폭발 애니메이션이 끝났을 때 kill()를 호출하여 스프라이트 객체가 속한 그룹에서 제거.
Catapult/explosion.py

17.3.4 메인 모듈(게임 루프)
Background 스프라이트 클래스. 배경의 움직임을 담당.
background.png이고, 1200*300px.
이 배경 이미지를 게임 루프를 통해 게임 화면의 왼쪽 방향, x축의 음으로 움직이게.
배경 이미지가 x축으로 -800만큼 이동하면 배경 이미지의 마지막 부분이 화면에 걸칩니다.
이 때 다시 배경 이미지의 x좌표를 0으로 초기화한 후 다시 왼쪽으로 움직이게 하면,
바람이 불어 구름이 움직이는 것 같은 효과.
Catapult/game_main.py




'''