'''
파이썬은 기본적으로 Tkinter라고 하는 UI 툴킷을 함께 제공.
Tkinter는 룩앤필(모양새와 사용성)이 운영체제와 자연스럽게 어울리지 않고,
GUI가 복잡해질수록 다루기가 힘들어진다는 단점.
기본적으로 제공하는 위젯의 종류가 적어 별도의 모듈을 추가적으로 내려받아야합니다.
wxPython은 서드파티모듈이지만 대부분을 극복할 수 있습니다.
플랫폼도 독립적.

14.1 wxPython 소개
wxWidget은 1992년부터 개발되어온 크로스 플랫폼 GUI툴킷.
같은 코드로 다양한 GUI플랫폼에서 동작할 수 있는 프로그램을 만들도록 도와줌.
wxPython은 wxWidget 위에 파이썬 코드를 입혀 파이썬에서도 사용할 수 있도록 개발된 라이브러리.

14.2 wxPython-Phoneix 설치
하나는 소스 코드를 내려받아 빌드하는것
또 다른 하나는 pip명령어를 이용하는 것.
시스템에 맞는 wxPython-Phoenix 설치 파일을 내려받습닏.
파이썬 버전과 플랫폼 종류를 잘 확인. 확장자는 .whl
둘 중 하나.
>pip install "파일이름"
>pip install -U wxPython

14.3 wxPython 애플리케이션의 시작과 끝, wx.App 클래스
wxPython을 하면서 가장 먼저 알아둬야 할 wx.App.
wx.App클래스는 wxPython 애플리케이션의 시작과 끝입니다.
wxPython시스템을 초기화하고 구동하는 역할을 갖고 있고, 
이벤트를 감시하고 처리하는 이벤트 루프를 수행하기 때문.
wxPython을 사용하는 모든 애플리케이션은 반드시 하나의 wx.App의 인스턴스를 갖고 있어야 합니다.

생명주기
시작
wx.App객체 생성 ----- OnInit()호출
위젯 생성 ----- Frame, Button, List 등 각종 위젯 생성
이벤트 처리기 등록 ----- 이벤트와 이벤트 처리기 연결
wx.App.MainLoop() 호출 ----- 이벤트 루프 실행
종료

wx.App의 인스턴스가 만들어지면 wxPython 시스템이 초기화되고,
초기화가 완료되면 OnInit()메소드가 자동으로 호출.
OnInit()을 재정의해서 윈도우와 위젯 생성을 해도 되지만, 꼭 그럴필요는 없다.
wx.App의 인스턴스 생성 코드 이후에도 위젯을 생성할 수 있으므로.
다음으로 이벤트 처리기를 만들어서 이벤트와 연결하고 wx.App.MainLoop()를 호출하면
애플리케이션이 시스템이 보내는 이벤트를 감시하다가 해당 이벤트와 연결된 이벤트 처리기를 호출.
StartingWxPython.py

14.3.1 wx.App.OnInit() 메소드
wx.App이 wxPython 체계를 구동하는 역할.
윈도우, 버튼, 텍스트 상자 같은 모든 wxPython 위젯은 wx.App의 인스턴스가 만들어진 이후에 생성.
__init()__이 아닌 OnInit()을 이용해야 합니다. (wxWidget에서)
OnInit()은 __init__() 메소드가 실행된 다음에(wxPython 체계의 초기화가 완전히 이루어진 후에)
호출되기 때문에 GUI 애플리케이션에 필요한 위젯을 생성하는 데에 적합합니다.
wx.App의 파생클래스를 만들고 OnInit()을 오버라이딩하고, 기존 코드와 같다.
OnInit.py

OnInit()을 사용하지 않는다는 것은 wx.App의 파생클래스를 정의하지 않는다는 것.
파생 클래스가 없어도 수행 가능하고 수월합니다. 취향차이

14.4 GUI의 창틀:wx.Frame 클래스
wx.Frame은 창의 틀이라고 할 수 있습니다. 위젯으로 꾸민 GUI을 창 밖으로 보이는 풍경.
대개는 wx.Frame 파생 클래스를 만들어 씁니다.
그리고 그 안에 여러 가지 위젯으로 GUI를 구성해서 넣는 것.

14.4.1 wx.Frame의 파생 클래스로 윈도우 만들어 띄우기
wx 모듈을 반입하고 wx.Frame을 상속하는 클래스를 정의하기만 하면 됩니다.
import wx

class MyFrame(wx.Frame):
    pass

MyFrame.__init__()메소드 안에서 부모 클래스인 wx.Frame의 __init__()를 호출해 초기화.
EmptyWindow.py

14.4.2 wx.Frame의 이벤트와 이벤트 처리기 연결하기
wx.Frame을 포함해서 wxPython의 각 위젯에는 일어날 수 있는 사건들이 미리 정의.
버튼을 클릭했을 때 EVT_BUTTON이벤트, 윈도우를 닫을 때는 EVT_CLOSE
이벤트 처리기(Event Handler)는 이벤트가 발생했을 때 호출되는 함수나 메소드.
def OnClose(event):
    pass
이벤트 처리기가 어떤 클래스의 멤버로 구성된다면 self매개변수.
class MyFrame(wx.Frame):
    def OnClose(self, event):
        pass
이렇게 정의해둔 이벤트 처리기는 Bind() 메소드를 통해 이벤트를 연결합니다.
wx.Frame을 비롯한 모든 wxPython의 위젯은 wx.EvtHandler 클래스를 둡니다.
그리고 거기에 Bind()가 정의되어 있습니다.
class MyFrame(wx.Frame):
    def __init__(self):
        #Bind() 첫번째 매개변수는 이벤트, 두번째는 이벤트 처리기.
        self.Bind(wx.EVT_CLOSE, self.OnClose)
    def OnClose(self, event):
        pass
wx.Frame을 상속하는 MyFrame에 닫기 이벤트에 대한 이벤트 처리기를 구현.
CloseEvent.py

14.4.3 wx.Frame의 속성 조정하기
wx.Frame의 크기, 색상, 스타일을 변경하는 방법
크기를 변경할 때는 SetSize().
SetSize()에는 윈도우의 너비와 높이를 나타내를 wx.Size타입의 객체를 매개변수로 넘겨줍니다.
frame=wx.Frame()
frame.SetSize(wx.Size(300,200)) #윈도우의 크기를 폭 300px, 높이 200px로 지정
왼쪽 마우스 버튼을 클릭하면 400px*200px 오른쪽클릭하면 200px*400px로 변경하는 예제
WindowSize.py

윈도우의 배경색을 바꿀 때에는 SetBackgroundColour()
매개변수로 wx.Colour 객체를 입력받습니다.
wx.Colour클래스는 RGBA(red,green,blue,alpha(투명도))를 이용해 색을 표현하는데
각각 0~255사이의 값으로 입력받아 색을 조합합니다.
frame=wx.Frame()
frame.SetBackgroundColour(wx.Colour(255,0,0,0)) #윈도우 배경색을 빨간색으로.
왼쪽 마우스 버튼을 클릭하면 배경색을 파란색, 오른쪽 버튼을 클릭하면 빨간색으로 변경
WindowColour.py

스타일들은 비트 논리합(|) 연산자로 여러 개를 조합해서 사용할 수 있습니다.
wx.DEFAULT_FRAME_STYLE:기본 윈도우 스타일.
wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|
wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN
wx.ICONIZE:윈도우 최소화
wx.CAPTION:윈도우에 타이틀바 표시
wx.MINIMIZE:윈도우 최소화
wx.MINIMIZE_BOX:윈도우 최소화 버튼 표시
wx.MAXIMIZE:윈도우 극대화
wx.MAXIMIZE_BOX:윈도우 최대화 버튼 표시
wx.CLOSE_BOX:윈도우 닫기 버튼 표시
wx.STAY_ON_TOP:최상위 윈도우 여부
wx.SYSTEM_MENU:시스템 메뉴 표시
wx.RESIZE_BORDER:윈도우 외곽의 크기 조정 경계 표시
wx.FRAME_TOOL_WINDOW:윈도우에 작은 타이틀바 표시(작업표시줄x)
wx.CLIP_CHILDREN:부모 윈도우를 다시 그려야할 때 자식 윈도우가 차지하는 영역을
제외(깜박임 방지)
윈도우 외곽의 크기 조정 경계와 타이틀바만 표시한다면
frame=wx.Frame()
frame.SetWindowStyle(wx.RESIZE_BORDER|wx.CAPTION)
왼쪽마우스클릭하면 크기 조정 경계와 타이틀바만 표시, 오른쪽클릭하면 윈도우 기본스타일
WindowStyle.py

14.4.4 wx.Frame 위에 위젯 올리기
버튼이나 텍스트 박스 같은 위젯을 윈도우 안에 채우는 법.
wx.Frame처럼 위젯을 담는 위젯을 컨테이너 위젯(Container Widget)
위젯을 컨테이너 위젯에 담을 때는 생성자의 parent매개변수에 컨테이너 위젯의 식별자만.
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="Simple Button")
        btnClick=wx.Button(self, label="Click Me!")
wx.Button()의 첫번째 매개변수는 버튼이 담겨질 컨테이너 위젯의 식별자.
MyFrame자신을 컨테이너 위젯으로 지정.
MyFrame객체를 wx.Button()생성자의 매개변수로 넘기면 버튼 객체는
컨테이너 위젯인 MyFrame안에 나타납니다.
wx.Button도 버튼 누름 이벤트(wx.EVT_BUTTON)에 대해 이벤트 처리기를 등록해서 사용
class MyFrame(wx.Frame):
    def __init__(self):
        btnClick.Bind(wx.EVT_BUTTON, self.OnBtnClickMe)
    def OnBtnClickMe(self, event):
        wx.MessageBox("Clicked!", "Simple Button", wx.OK)
SimpleButton.py

14.5 컨테이너 위젯 wx.Panel과 위젯 배치 도우미 wx.Sizer
GUI프로그래밍을 하면서 신경쓰는 부분이 위젯을 어떻게 배치할 것인가?
wxPython은 위젯 배치를 처리하는 wx.Sizer를 제공합니다.

14.5.1 컨테이너 위젯의 대표 선수 wx.Panel
wx.Panel은 wx.Frame처럼 다른 위젯을 담을 수 있는 컨테이너 위젯입니다.
보통 wx.Frame위에 wx.Panel을 얹고 그 위에 다른 위젯들을 얹습니다.
class MyFrame(wx.Frame):
    def __init__(self):
        panel=wxPanel(self) #wx.Panel 객체 생성

그런데 위젯을 패널 위에 얹을 때 자리를 정해주기 위해서는 패널에 대한 상대 좌표 필요.
카테시안 좌표계가 아닌 y축을 뒤집은 꼴의 좌표계. 우측 상단이 (0,0)
wxPython에서는 좌표의 단위는 화소, Pixel입니다.
wx.Panel 객체의 좌상단으로부터 x축으로 50픽셀, y축으로 50픽셀 떨어진 곳에 버튼을 위치
class MyFrame(wx.Frame):
    def __init__(self):
        self.panel=wx.Panel(self)
        self.button1=wx.Button(self.panel, label="(50,50)")
        self.button1.SetPosition((50,50))
Panel.py

14.5.2 위젯 배치 도우미:wx.Sizer와 그 파생 클래스의 이해
wx.Sizer는 추상기반 클래스여서 파생클래스들을 사용해야 합니다.
wx.Sizer의 파생 클래스들을 사이저(Sizer)라고 합니다.

수직이냐 수평이냐 그것이 문제로다:wx.BoxSizer
wx.BoxSizer는 상자를 쌓아가듯 위젯을 배치하는 사이저.
매개변수로 위젯 배치를 수직(wx.VERTICAL)인지 수평(wx.HORIZONTAL)인지 정함.
hBoxSizer=wx.BoxSizer(wx.HORIZONTAL) #수평
vBoxSizer=wx.BoxSizer(wx.VERTICAL) #수직

중요한 점은 '사이저는 그저 위젯의 배치만을 거들 뿐'
위젯은 컨테이너 위젯 안에 생성되고, 사이저는 이렇게 생성된 위젯의 정보를 등록해뒀다가
컨테이너의 크기가 달라질 때 위젯을 재배치합니다.
panel=wx.Panel(frame) #wx.Panel객체를 생성하고
button1=wx.Button(panel) #그 위에 wx.Button위젯을 생성합니다.
button2=wx.BUtton(panel) #위젯의 위치는 따로 지정하진 않습니다.

sizer=wx.BoxSizer(wx.HORIZONTAL)
sizer.Add(button1) #사이저의 Add()메소드를 호출해 사이저가 담당할 위젯정보를 등록.
sizer.Add(button2)

panel.SetSizer(sizer) #sizer를 매개변수로 입력.
#panel에 크기 변경 이벤트가 발생하면 sizer가 button들의 위치와 크기를 변경.

Add메소드는 wx.Sizer로부터 물려받은 것.
다른 사이저 클래스들도 모두 Add()메소드를 갖고 있습니다.
Add(self, item, propotion=0, flag=0, border=0, userData=None)
item은 사이저의 배치 대상 위젯을 나타냅니다.
proportion은 사이저의 방향(H or V)으로 해당 위젯이 얼마나 늘어나게 할 것인지 지정
0이면 늘어나지 않고 1이상이면 늘어납니다. BoxSizer에서만 의미가 있다.
border는 사이저의 경계너비.
userData는 위젯의 배치에 영향을 주진 않지만 이에 관해 따로 보관하고자 하는 데이터
flag는 사이저의 동작하는 방식을 제어하며 플래그들을 논리합 연산자로 조합하여 입력
wx.TOP #border 너비가 적용될 사이저의 면을 나타냅니다.
wx.BOTTOM
wx.LEFT
wx.RIGHT
wx.ALL
wx.EXPAND:사이저가 위젯에게 할당한 구역을 위젯이 모든 공간을 채웁니다.
공간이 늘어나면 위젯도 커지고, 공간이 줄면 위젯도 줍니다.
wx.SHAPED:위젯의 비율을 유지하며 확장하며 줄어듦
wx.ALIGN_CENTER #사이저가 할당한 구역안에서 어떤 방향으로 정렬할지 결정.
wx.ALIGN_LEFT
wx.ALIGN_RIGHT
wx.ALIGH_TOP
wx.ALIGN_BOTTOM
wx.ALIGN_CENTER_VERTICAL
wx.ALIGN_CENTER_HORIZONTAL

sizer=wx.BoxSizer(wx.HORIZONTAL)

#구역 채움 + 경계 너비 5를 모든 면에 적용
sizer.Add(button1, 0, wx.EXPAND|wx.ALL, 5)

#구역의 상단/중앙에 정렬
sizer.Add(button2, 0, wx.ALIGN_TOP|wx.ALIGN_CENTER)

wx.Panel위에 또 다른 wx.Panel과 wx.Button을 올리고 wx.BoxSizer를 이용해 배치
BoxSizer.py

제목이 있는 wx.BoxSizer:wx.StaticBoxSizer
wx.StaticBoxSizer는 제목이 상단에 붙는다는 것만 빼면 같다.
사이저에 제목을 붙이려면 생성자의 title 매개변수를 다음과 같이 지정.
panel=wx.Panel(frame)
sizer=wx.StaticBoxSizer(wx.HORIZONTAL, panel, "제목")
wx.StaticBoxSizer의 생성자는 제목 텍스트를 그려 넣을 wx.StaticBox()위젯을 생성하는데,
두 번째 매개변수는 이 제목 위젯이 놓일 컨테이너
StaticBoxSizer.py

격자 안에 위젯 담기:wx.GridSizer
배치를 수행할 컨테이너의 행과 열로 균등하게 나누고, 나눈 각 공간에 위젯을
배치하는 사이저입니다.
gridSizer=wx.GridSizer(rows=4, cols=3, hgap=5, vgap=5)
처음 두 매개변수는 행과 열의 개수, 나머지 두 개의 매개변수는 수평 간격과 수직 간격(px).
GridSizer.py

유연한 wx.GridSizer:wx.FlexGridSizer
특정 열 또는 행을 컨테이너 크기의 변화에 따라 늘어나거나 즐어들게 만들 수 있습니다.
1)사이저를 생성(wx.GridSizer와 매개변수 동일)
fgridSizer=wx.FlexGridSizer(rows=3, cols=3, hgap=5, vgap=5)
2)사이저에 위젯을 추가합니다.
fgridSizer.Add(widget1)
3)크기를 변경할 행 또는 열을 지정합니다.(지정안하면 GridSizer와 동일)
fgridSizer.AddGrowableCol(1) #두 번째 열을 유연하게
fgridSizer.AddGrowableRow(2) #세 번째 열을 유연하게
FlexGridSizer.py

14.6 다양한 위젯 사용해보기

14.6.1 wx.MenuBar와 wx.Menu, wx.MenuItem
주문대 위에 보이는 보드=>wx.MenuBar
종류별로 정리되어 있는 각 패널=>Menu
메뉴 내에 구체적인 메뉴 이름과 가격이 적혀 있는 것=>MenuItem
즉, GUI에서 메뉴바는 상단에 메뉴를 걸 수 있는 기다란 막대 위젯이고, 
메뉴 항목은 구체적인 명령을 나타내는 위젯.
메뉴는 이 메뉴 항목을 메뉴바에 연결하는 위젯
모두 컨테이너 위젯을 필요로 하지 않습니다.
class MyFrame(wx.Frame):
    def __init__(self):
        menuBar=wx.MenuBar() #wx.MenuBar 인스턴스 생성
        fileMenu=wx.Menu() #wx.Menu 인스턴스 생성
        fileNewMenu=wx.MenuItem(id=wx.ID_ANY, text="새 파일") #wx.MenuItem인스턴스생성

        fileMenu.Append(flileNewMenu) #메뉴에 메뉴항목 추가
        menuBar.Append(fileMenu,"&File") #메뉴바에 메뉴 추가
        self.SetMenuBar(menuBar) #윈도우의 메뉴바로 menuBar지정

wx.MenuItem은 클릭할 때 EVT_MENU이벤트가 발생.
class MyFrame(wx.Frame):
    def __init__(self):
        self.Bind(wx.EVT_MENU, self.OnNew, fileNewMenu)
    def OnNew(self,e):
        wx.MessageBox("OnNew() Clicked!")
Menu.py

14.6.2 wx.StaticText와 wx.TextCtrl
wx.StaticText는 텍스트를 정적으로 표시하는 위젯.
사용자로부터 입력을 받는다거나 이벤트 처리를 하기 위한 목적이 아님.
wx.TextCtrl은 텍스트의 입력/출력 기능을 모두하는 위젯.
생성자의 매개변수 label에 표시할 텍스트를 지정해서 인스턴스를 생성.
panel=wx.Panel()
staticName=wx.StaticText(panel, label="Name:")
실행중 wx.StaticText의 텍스트를 바꾸고 싶다면 SetLabelText()이용
staticName.SetLabelText("이름:")
wx.TextCtrl의 인스턴스 생성
panel=wx.Panel()
textRed=wx.TextCtrl(panel, value='Hello')
매개변수 value는 위젯이 표시할 텍스트를 나타냄. 생략하면 표시 없음.
프로그램 실행 중 텍스트를 바꾸거나 읽어오고 싶을 때는 SetValue()/GetValue()이용
textRed.SetValue('안녕하세요.') #표시 텍스트 수정
greeting=textRed.GetValue() #표시 텍스트 읽기
사용자가 텍스트를 입려갛거나 코드를 이용해 텍스트를 변경하면 EVT_TEXT이벤트
clss MyFrame(wx.Frame):
    def __init__(self):
        self.Bind(wx.EVT_TEXT, self.OnTextChange, textRed)
    def OnTextChange(self, e):
        pass
RGB를 각각 입력할 수 있는 wx.TextCtrl위젯을 배치하고, 텍스트가 바뀔 때마다 배경색을 바꿈
TextCtrl.py

14.6.3 wx.RadioButton
동그란 모양의 선택 여부를 표시하는 기능이 있는 '버튼' 위젯.
하나만 따로 사용하는 경우보단 여러 개를 하나의 그룹으로 묶어 사용.
이 그룹에서 위젯 하나를 선택하면 다른 위젯의 선택 표시가 사라집니다.
그래서 주로 사용자에게 옵션을 선택하게 하는 용도로 사용.
생성자 매개변수 중 label은 버튼이 표시할 텍스트를 나타내며
style은 버튼이 옵션 그룹을 새로 만들기 시작할지를 결정합니다.
style이후 부터 다른 style이 나오기 전까지 하나의 옵션 그룹으로 묶습니다.
panel=wx.Panel()
rdoRed=wx.RadioButton(panel,label="Red", style=wx.RB_GROUP)
rdoGreen=wx.RadioButton(panel,label="Green")
rdoBlue=wx.RadioButton(panel,label="Blue")

rdoEnable=wx.RadioButton(panel,label="Enable", style=wx.RB_GROUP)
rdoDisable=wx.RadioButton(panel,label="Disable")
라디오 버튼을 클릭하면 wx.EVT_RADIOBUTTON이벤트가 발생
class MyFrame(wx.Frame):
    def __init__(self):
        self.Bind(wx.EVT_RADIOBUTTON,self.OnRed,rdoRed)
    def OnRed(self, e):
        pass
사용자의 선택에 따라 윈도우의 배경색을 바꾸거나 위젯을 활성/비활성화하는 예제
RadioButton.py

14.6.4 wx.CheckBox
체크 기호를 표시하는 위젯.
각 위젯이 독립적으로 동작하기 때문에 복수 개의 옵션을 선택하는 GUI를 만들 수 있다.
panel=wx.Panel()
checkItalic=wx.CheckBox(panel,label="Italic")
체크 기호를 표시하고 싶으면 SetValue()를 이용, 체크됐는지 확인하고 싶으면 GetValue()
checkItalic.SetValue(wx.CHK_CHECKED) #체크
checkItalic.SetValue(wx.CHK_UNCHECKED) #체크 해제
isChecked=checkItalic.GetValue() #wx.CHK_UNCHECKED
사용자가 선택하면 EVT_CHECKBOX이벤트가 발생
class MyFrame(wx.Frame):
    def __init__(self):
        self.Bind(wx.EVT_CHECKBOX,self.OnCheck,self.checkBold)
    def OnCheck(self ,e):
        self.ChangeFont()
사용자가 옵션을 선택할 때마다 글꼴을 바꾸는 기능을 하는 예제
CheckBox.py

14.6.5 wx.ListBox와 wx.ComboBox
모두 목록형 데이터를 표시하는 기능.
ListBox는 이 목록을 전부 표시하는 반면, 
ComboBox는 목록 중 하나만 표시하다가 사용자가 해당 위젯을 선택했을 때 목록을 늘어뜨려 표시
데이터를 입력하는 방법은 비슷.
두 위젯 모두 인스턴스를 만들 때부터 데이터가 담겨있는 리스트 객체를 생성자의 매개변수로
넘길 수도 있고, 인스턴스 생성 후에 Append()메소드를 이용해 데이터를 따로 입력할 수도.
colors=["Red","Orange","Yellow","Green","Blue"]
comboColors=wx.ComboBox(panel,choices=colors)
listColors=wx.ListBox(panel,choices=colors)
comboColors.Append("Purple")
listColors.Append("Purple")
특정 항목을 선택했을 때 wx.ComboBox는 EVT_COMBOBOX, wx.ListBox는 EVT_LISTBOX
class MyFrame(wx.Frame):
    def __init__(self):
        self.Bind(wx.EVT_COMBOBOX,self.OnComboBox,self.colorCombo)
        self.Bind(wx.EVT_LISTBOX,self.OnListBox,self.colorListBox)
    def OnComboBox(self, e):
        pass
    def OnListBox(self,e):
        pass
ComboBox객체는 인스턴스를 만들때부터 데이터 리스트를 입력받고,
ListBox는 EVT_COMBOBOX가 발생할 때마다 Append()를 이용해 데이터를 추가
ListCombo.py

14.6.6 wx.TreeCtrl
나무처럼 뿌리에서부터 가지가 뻗어나가는 모습으로 데이터를 표현하는 위젯.
족보나 디렉토리 구조처럼 계층적인 데이터를 표현하는데 적합
1)wx.TreeCtrl의 인스턴스를 만들고나서 AddRoot()메소드를 호출하여 뿌리를 추가.
2)뿌리를 추가한 후에는 AppendItem()메소드를 호출해서 가지를 하나씩 붙여나간다.
panel=wx.Panel()

tree=wx.TreeCtrl(panel)
beverage=tree.AddRoot('음료수') #뿌리를 추가

coffee=tree.Append(beveage,'커피') #부모노드 첫번째 매개변수
tree.AppendItem(beverage,'주스')

tree.AppendItem(coffee,'아메리카노') #가지에 가지를 붙이기.
tree.AppendItem(coffee,'라떼')
음료수
  ㄴ커피
     ㄴ아메리카노
     ㄴ라떼
  ㄴ주스
위젯의 노드를 선택하면 EVT_TREE_SEL_CHANGED이벤트가 발생
class MyFrame(wx.Frame):
    def __init__(self):
        self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnNodeSelected, self.tree)
    def OnNodeSelected(self, e):
        pass
조선 왕조의 족보를 일부 표시하는 예제
TreeCtrl.py

14.6.7 wx.Slider와 wx.Gauge
wx.Slider는 볼륨이나 재생 위치를 옮기는 UI
wx.Gauge는 사용자의 조작을 입력받지는 않지만 현재의 상황을 막대 눈금으로 보여줌.
panel=wx.Panel()
slider=wx.Slider(panel,minValue=0,maxValue=100)
minValue와 maxValue는 슬라이더가 표현하고 저장하는 데이터의 최소 최대범위.
버튼이 가리키는 값을 읽고 싶거나 바꾸고 싶을 때는 GetValue()/SetValue()
slider=wx.Slider(panel,minValue=0,maxValue=100)
slider.SetValue(50) #값 변경
value=slider.GetValue() #값 읽기
슬라이더 버튼이 이동할 때마다 EVT_SLIDER 이벤트를 발생.
class MyFrame(wx.Frame):
    def __init__(self):
        self.Bind(wx.EVT_SLIDER, self.OnsliderChange, self.slider)
    def OnSliderChange(self,e):
        pass

wx.Gauge는 딱 range만 갖습니다.
panel=wx.Panel()
gauge=wx.Gauge(panel,range=100)
내용을 바꾸고 싶을 때는 SetValue()
gauge.SetValue(55)
wx.Slider를 왼쪽/오른쪽으로 옮길 때마다 wx.Gauge위젯의 모습도 따라 변경하는 예제
SliderGauge.py

14.6.8 wx.Dialog
사용자에게 표시하는 윈도우의 종류 중에 대화상자라는 것이 있습니다.
사용자에게 간단하게 정보를 띄우거나 응답을 받는 용도로 사용.
wx.MessageBox()도 대화상자.
wx.Dialog는 대화상자를 표현하는 클래스지만 wx.Frame을 이용해 하던 일들을 그대로 할수도
있고 그 반대로도 사용할 수 있습니다.
wx.Dialog는 wx.Frame이 가지지 않는 모달(Modal)이라는 속성.
부모 윈도우가 대화상자를 모달로 띄우면 사용자는 해당 대화상자를 닫기 전까지는
부모 윈도우에 접근할 수가 없습니다.
'파일 저징', '파일 열기' 대화상자가 모달의 예.
wx.MessageBox()도 모달 대화상자.
모달이 아닌경우 Modeless
wx.Dialog는 독립적으로 동작하는 wx.Frame과 달리 부모 윈도우가 필요함.
class MyDialog(wx.Dialog):
    def __init__(self, _parent, _title):
        #부모 윈도우와, 타이틀바에 표시할 텍스트
        wx.Dialog.__init__(self, parent=_parent, title=_title)
wx.Dialog의 파생클래스는 인스턴스를 생성하고 사용자에게 표시할 수 있습니다.
해당 인스턴스를 모달로 띄우고 싶으면 ShowModal() 아니면 Show()
class MyFrame(wx.Frame):
    def __init__(self):

    def OnModalButton(self, e):
        #부모 윈도우, 타이틀바에 표시할 텍스트
        dlg=MyDialog(self, "Modal Dialog")
        dlg.ShowModal() #모달 대화상자로 띄우기
    def OnModelessButton(self, e):
        dlg=MyDialog(self, "Modeless Dialog")
        dlg.Show() #모들리스 대화상자로 띄우기
Dialog.py

'''