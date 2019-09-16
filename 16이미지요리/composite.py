import sys
from wand.image import Image

if len(sys.argv) < 3:
    print('{0} <Image 1> <Image 2>'.format(sys.argv[0]))
    sys.exit()

image1_path=sys.argv[1]
image2_path=sys.argv[2]

with Image(filename=image1_path) as image1:
    with Image(filename=image2_path) as image2:
        with image1.clone() as clone:
            image2.transparentize(0.7) #image2의 투명도를 70%로 지정
            clone.composite(image2, 100, 100) #image2를 image1의 100,100 좌표에 합성
            clone.save(filename=image1_path+'_'+image2_path)