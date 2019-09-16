import sys
from wand.image import Image

if len(sys.argv) < 3:
    print('{0} <ORIGINAL PATH> <SCALE>'.format(sys.argv[0]))
    sys.exit()

original_path=sys.argv[1]
scale=float(sys.argv[2]) #크기 조정 배율. 소수일 수도 있으므로.

with Image(filename=original_path) as image:
    print("Original : {0}, {1}".format(image.format, image.size))

    #복사본을 만든 후 resize()를 호출.
    resized=image.clone()
    resized.resize(int(image.width*scale), int(image.height*scale))
    print("Resized : {0}, {1}".format(resized.format, resized.size))
    resized.save(filename='{0}.{1}'.format(scale, original_path))