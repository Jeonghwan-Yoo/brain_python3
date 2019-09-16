import pygame

pygame.init()
screen=pygame.display.set_mode((300,100))
pygame.display.set_caption("Drawing Shapes")

clock=pygame.time.Clock()
run=True
key=None
start_pos=[0,0]

#게임 루프
while run:
    #1)사용자 입력 처리
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==pygame.KEYDOWN:
            key=event.key
    
    #2)게임 상태 업데이트
    #게임 루프가 반복을 수행할 때마다 start_pos의 x좌표를 오른쪽으로 이동.
    if start_pos[0] > screen.get_width():
        start_pos[0]=0
    else:
        start_pos[0]+=1

    #3)게임 상태 그리기
    screen.fill(pygame.color.Color(255,255,255))

    if key==pygame.K_1: #1이 눌렸을 때 직선을 그림
        pygame.draw.line(screen,pygame.color.Color(0,0,0),start_pos,
        (screen.get_width(),screen.get_height()),1)
    elif key==pygame.K_2: #2가 눌렸을 때 타원을 그림
        pygame.draw.ellipse(screen,pygame.color.Color(255,0,0),
        pygame.Rect(start_pos,(50,50)))
    elif key==pygame.K_3: #3이 눌렸을 때 삼각형을 그림
        pygame.draw.polygon(screen,pygame.color.Color(0,255,0),
        [start_pos,(0,screen.get_height()),(screen.get_width(),screen.get_height())])
    elif key==pygame.K_4: #4가 눌렸을 때 사각형을 그림.
        pygame.draw.rect(screen,pygame.color.Color(0,0,255),
        pygame.Rect(start_pos,(50,50)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()    