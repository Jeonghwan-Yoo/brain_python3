import sys
from wand.image import Image

if len(sys.argv) < 3:
    print('{0} <ORIGINAL PATH> <TARGET FORMAT>'.format(sys.argv[0]))
    sys.exit()

original_path=sys.argv[1]
target_format=sys.argv[2]

with Image(filename=original_path) as image:
    print("Original : {0}, {1}".format(image.format, image.size))

    #convert()는 변환된 형식의 Image인스턴스를 새로 생성합니다.
    with image.convert(target_format) as converted:
        print("Converted : {0}, {1}".format(converted.format, converted.size))
        converted.save(filename=original_path+'.'+target_format)