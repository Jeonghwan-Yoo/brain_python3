import wx

class MyApp(wx.App): #wx.App을 상속하는 MyApp을 정의
    def OnInit(self): #오버라이드
        frame=wx.Frame(parent=None, title='Hello!')
        frame.Show(True) #Frame의 인스턴스를만들어 띄웁니다.
        return True

if __name__=='__main__':
    app=MyApp() #MyApp 클래스의 인스턴스를 만들고 이벤트 루프를 시작합니다.
    app.MainLoop()