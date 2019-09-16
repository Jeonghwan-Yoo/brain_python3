import pygame
from pygame.color import Color
from animation import Animation
from stone import Stone
from const import *

class Catapult(Animation):
    # STATE : CATAPULT_READY -> CATAPULT_FIRE
    #           ^------|
    # READY일 때만 이동 가능
    # FIRE일 때는 아무것도 못함.
    def __init__(self, stone): #stone객체를 생성자의 매개변수로 받습니다.
        self.sprite_image = 'catapult.png'
        self.sprite_width = 32
        self.sprite_height = 32
        self.sprite_columns = 5
        self.fps = 30
        self.stone = stone
        self.state = CATAPULT_READY
        self.init_animation() #Animation으로부터 init_animation()을 호출.

    def update(self): 
        if self.state == CATAPULT_FIRE: #FIRE상태일 때는 던지기 애니메이션 실행.
            self.calc_next_frame()

            if self.current_frame == self.sprite_columns:
                self.current_frame = 0
                # 돌멩이 날리기 시작
                #던지기 애니메이션이 마지막프레임에 도착하면 READY도 바꾸고 돌을 던짐.
                self.state = CATAPULT_READY
                self.stone.setup(
                    (self.rect.x, self.rect.y), 
                    self.power, self.direction)
        else:
            self.current_frame = 0
                
        rect = (self.sprite_width*self.current_frame, 0, 
                self.sprite_width, self.sprite_height)
        self.image.blit( self.sprite_sheet, (0, 0), rect)
        self.image.set_colorkey(Color(255, 0, 255))

    def forward(self):
        #화면 내에서 한정된 위치까지만 1픽셀씩 오른쪽으로 이동시킵니다.
        if self.rect.x < 100:
            self.rect.x += 1

    def backward(self):
        #화면 내에서 한정된 위치까지만 1픽셀씩 왼쪽으로 이동시킵니다.
        if self.rect.x > 0:
            self.rect.x -= 1

    def fire(self, power, direction):
        self.state = CATAPULT_FIRE
        #돌을 던지는 데 필요한 발사파워, 발사각을 입력받아 데이터 속성에 저장.
        self.power = power
        self.direction = direction