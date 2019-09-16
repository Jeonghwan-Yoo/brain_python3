class ClassVar:
    text_list=[]

    def add(self, text):
        self.text_list.append(text)
    def print_list(self):
        print(self.text_list)

if __name__=='__main__':
    a=ClassVar()
    a.add('a')
    a.print_list() #['a'] 출력을 기대

    b=ClassVar()
    b.add('b')
    b.print_list() #['b'] 출력을 기대 하지만 ['a', 'b']
    #클래스 속성으로 정의된 text_list변수를 모든 인스턴스가 공유하게 되어 생긴 문제.
