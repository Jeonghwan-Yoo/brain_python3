import pygame

pygame.init()
screen=pygame.display.set_mode((400,300))
pygame.display.set_caption("Hellom pygame!")

clock=pygame.time.Clock()
run=True
gb=[255,255]

#게임 루프
while run: #게임 루프는 run변수가 True인 동안에만 동작합니다.
    #1)사용자 입력처리
    for event in pygame.event.get():
        if event.type==pygame.QUIT: #애플리케이션을 종료하고자 할 때 발생.
            run=False

    #2)게임 상태 업데이트
    if gb[0]==0:
        gb[0]=255
        gb[1]=255
    else:
        gb[0]-=1
        gb[1]-=1
    
    #3)게임 상태 그리기
    screen.fill(pygame.color.Color(255,gb[0],gb[1])) #게임 화면을 채웁니다.
    pygame.display.flip() #화면 전체를 갱신합니다.

    clock.tick(60)

pygame.quit()