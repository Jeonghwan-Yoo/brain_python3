import sys
from wand.color import Color
from wand.drawing import Drawing
from wand.image import Image

if len(sys.argv) < 3:
    print('{0} <ORIGINAL PATH> <TEXT>'.format(sys.argv[0]))
    sys.exit()

original_path=sys.argv[1]
text=sys.argv[2]

with Image(filename=original_path) as image:
    with image.clone() as clone:
        with Drawing() as draw:
            draw.stroke_color=Color('#FF0000')
            draw.fill_color=Color('#FFFFFFA0') #RRGGBBAA(투명도)
            draw.rectangle(left=10, top=15, width=220, height=55) #사각형 그리기
            
            draw.stroke_color=Color('#00FF00')
            draw.stroke_width=2
            draw.line((10,5),(230,5)) #직선 그리기
            draw.line((10,80),(230,80)) 
            
            draw.stroke_color=Color('#000000FF')
            draw.fill_color=Color('#000000')
            draw.font='C:\Windows\Fonts\JOKERMAN.TTF'
            draw.font_size=30
            draw.text(20,51,text) #텍스트 출력(좌표, 텍스트)

            Drawing.draw(draw,clone) #draw(clone)와 동일. 이미지에 draw의 작업결과 출력
            
            clone.save(filename='watermark_'+original_path)