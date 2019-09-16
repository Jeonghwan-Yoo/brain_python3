import sys
from wand.image import Image

if len(sys.argv) < 4:
    print('{0} <ORIGINAL PATH> <ROW> <COL>'.format(sys.argv[0]))
    sys.exit()

original_path=sys.argv[1]
#이미지를 나눌 줄과 칸 수를 row와 col 변수에 각각 지정
row=int(sys.argv[2])
col=int(sys.argv[3])

with Image(filename=original_path) as image:
    print("Original : {0}, {1}".format(image.format, image.size))
    #이미지의 높이를 줄 수로 나누고, 너비를 칸 수로 나누어 조각 이미지의 크기를 구함.
    cropped_height=int(image.height/row)
    cropped_width=int(image.width/col)

    for i in range(0, row):
        for j in range(0, col):
            left=j*cropped_width
            right=left+cropped_width
            top=i*cropped_height
            bottom=top+cropped_height

            #슬라이스 연산자로 이미지를 자르고 잘라낸 이미지를 저장.
            with image[left:right, top:bottom] as cropped:
                print("Cropped:{0}, {1}".format(cropped.format, cropped.size))
                cropped.save(filename='{0}.{1}.{2}'.format(i,j,original_path))


