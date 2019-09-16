import sys
from wand.image import Image

if len(sys.argv)<2:
    print('{0} <ORIGINAL PATH>'.format(sys.argv[0]))
    sys.exit()

original_path=sys.argv[1]

#이미지 파일을 Image 객체로 열 때는 생성자의 filename 매개변수에 파일 경로를 입력.
with Image(filename=original_path) as image:
    print("Original : {0}, {1}".format(image.format, image.size))

    #clone()은 메모리상에 복제본을 생성합니다.
    clone=image.clone()
    print("Clone {0}, {1}".format(clone.format, clone.size))
    #save()는 Image 객체의 내용을 이미지 파일에 저장합니다.
    clone.save(filename='clone.{0}'.format(original_path))
