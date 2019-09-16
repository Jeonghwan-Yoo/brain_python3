import pygame

pygame.init()
screen=pygame.display.set_mode((500,300))
pygame.display.set_caption("Keyboard Test")

clock=pygame.time.Clock()
run=True
key_status=""
key=None

#게임 루프
while run:
    #1)사용자 입력 처리
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        elif event.type==pygame.KEYDOWN:
            key_status="Key Down"
            key=event.key #event.key멤버 변수에는 어떤 키가 입력되었는지에 대한 정보.
        elif event.type==pygame.KEYUP:
            key_status="Key Up"
            key=event.key
    
    #2)게임 상태 업데이트

    #3)게임 상태 그리기
    screen.fill(pygame.color.Color(255,255,255))

    if key:
        #애플리케이션의 제목 표시줄에 어떤 키가 입력되었는지, 해당 키를 눌렀는지, 해제했는지
        pygame.display.set_caption(pygame.key.name(key)+" "+key_status)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()