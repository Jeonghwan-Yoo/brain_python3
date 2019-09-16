import pygame
from pygame.color import Color
from pygame.sprite import Sprite
from pygame.surface import Surface

class Runner(Sprite): #Sprite의 파생 클래스 정의.
    def __init__(self):
        Sprite.__init__(self) #1)Sprite.__init__()메소드를 호출.

        self.sprite_image = 'runnersprite.png'
        self.sprite_width = 70
        self.sprite_height = 100 
        self.sprite_sheet = pygame.image.load(
                                self.sprite_image).convert()
        self.sprite_columns = 14
        self.current_frame = 0
        #image데이터속성할당.
        self.image = Surface((self.sprite_width, self.sprite_height)) 

        rect = (self.sprite_width*self.current_frame, 0, 
                self.sprite_width, self.sprite_height)
        self.image.blit( self.sprite_sheet, (0, 0), rect)
        self.image.set_colorkey(Color(255, 0, 255)) #투명하게 표시할 생을 지정.
        self.rect = self.image.get_rect() #3)rect 데이터 속성 할당.
       
    def update(self): #4)update()정의
        if self.current_frame == self.sprite_columns - 1: #마지막 이미지이면
            self.current_frame = 0 #다시 처음 이미지로.
        else:
            self.current_frame += 1

        rect = (self.sprite_width*self.current_frame, 0, 
                self.sprite_width, self.sprite_height)
        self.image.blit( self.sprite_sheet, (0, 0), rect)